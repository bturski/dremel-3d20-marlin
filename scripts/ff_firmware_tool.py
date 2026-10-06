#!/usr/bin/env python3
"""Decrypt or encrypt FlashForge and Dremel 3D20 firmware files.

A plain Python port of moonglow/flashforge_firmware_tool (main.c), so Windows
users can make an unencrypted firmware file without compiling anything.
Needs only Python 3. No extra packages.

Decrypt a Dremel 3D20 file (for ST-Link recovery):
    python ff_firmware_tool.py decrypt dremel_2.0.9.5_01152023.bin dremel_unencrypted.bin

Encrypt a file you built yourself:
    python ff_firmware_tool.py encrypt firmware.bin dremel.bin

The default key is the Dremel key. Use --key flashforge790315 for FlashForge
and PowerSpec printers.

Original tool: https://github.com/moonglow/flashforge_firmware_tool
"""

import argparse
import struct
import sys

KEYS = {
    "dremel": "flashforge123456",
    "flashforge": "flashforge790315",
}

SBOX = bytes.fromhex(
    "637c777bf26b6fc53001672bfed7ab76ca82c97dfa5947f0add4a2af9ca472c0"
    "b7fd9326363ff7cc34a5e5f171d8311504c723c31896059a071280e2eb27b275"
    "09832c1a1b6e5aa0523bd6b329e32f8453d100ed20fcb15b6acbbe394a4c58cf"
    "d0efaafb434d338545f9027f503c9fa851a3408f929d38f5bcb6da2110fff3d2"
    "cd0c13ec5f974417c4a77e3d645d197360814fdc222a908846eeb814de5e0bdb"
    "e0323a0a4906245cc2d3ac629195e479e7c8376d8dd54ea96c56f4ea657aae08"
    "ba78252e1ca6b4c6e8dd741f4bbd8b8a703eb5664803f60e613557b986c11d9e"
    "e1f8981169d98e949b1e87e9ce5528df8ca1890dbfe6426841992d0fb054bb16"
)
INV_SBOX = bytes(SBOX.index(i) for i in range(256))


def xtime(b):
    return ((b << 1) ^ 0x1B) & 0xFF if b & 0x80 else (b << 1) & 0xFF


def expand_key(key):
    words = [list(key[i:i + 4]) for i in range(0, 16, 4)]
    rcon = 1
    for i in range(4, 44):
        w = list(words[i - 1])
        if i % 4 == 0:
            w = w[1:] + w[:1]
            w = [SBOX[b] for b in w]
            w[0] ^= rcon
            rcon = xtime(rcon)
        words.append([a ^ b for a, b in zip(w, words[i - 4])])
    flat = [b for w in words for b in w]
    return [bytes(flat[r * 16:(r + 1) * 16]) for r in range(11)]


def xor16(a, b):
    return bytes(x ^ y for x, y in zip(a, b))


def shift_rows(s, inverse):
    out = bytearray(s)
    for row in range(1, 4):
        vals = [s[4 * col + row] for col in range(4)]
        shift = (4 - row) if inverse else row
        for col in range(4):
            out[4 * col + row] = vals[(shift + col) % 4]
    return bytes(out)


def mix_columns(s, inverse):
    out = bytearray()
    for c in range(4):
        a = s[4 * c:4 * c + 4]
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        col = [xtime(a[j] ^ a[(j + 1) % 4]) ^ a[j] ^ t for j in range(4)]
        if inverse:
            u = xtime(xtime(a[0] ^ a[2]))
            v = xtime(xtime(a[1] ^ a[3]))
            w = xtime(u ^ v)
            col = [col[0] ^ w ^ u, col[1] ^ w ^ v, col[2] ^ w ^ u, col[3] ^ w ^ v]
        out.extend(col)
    return bytes(out)


def encrypt_block(block, rk):
    s = xor16(block, rk[0])
    for r in range(1, 11):
        s = bytes(SBOX[b] for b in s)
        s = shift_rows(s, False)
        if r != 10:
            s = mix_columns(s, False)
        s = xor16(s, rk[r])
    return s


def decrypt_block(block, rk):
    s = xor16(block, rk[10])
    for r in range(9, -1, -1):
        s = shift_rows(s, True)
        s = bytes(INV_SBOX[b] for b in s)
        s = xor16(s, rk[r])
        if r != 0:
            s = mix_columns(s, True)
    return s


CHUNK = 2048  # the original tool works in 2048 byte chunks, each with a zero IV


def process(data, key, encrypt):
    """AES-128 in CBC mode, restarted with a zero IV every 2048 bytes.

    This matches the original tool byte for byte. A trailing piece shorter
    than 16 bytes is copied through unchanged, as the original does.
    """
    rk = expand_key(key)
    out = bytearray(data)
    for start in range(0, len(data), CHUNK):
        chunk = data[start:start + CHUNK]
        if len(chunk) < 16:
            break
        usable = len(chunk) - len(chunk) % 16
        prev = bytes(16)
        for off in range(0, usable, 16):
            block = chunk[off:off + 16]
            pos = start + off
            if encrypt:
                enc = encrypt_block(xor16(block, prev), rk)
                out[pos:pos + 16] = enc
                prev = enc
            else:
                out[pos:pos + 16] = xor16(decrypt_block(block, rk), prev)
                prev = block
    return bytes(out)


def looks_like_firmware(data):
    """True if the first two words look like an STM32 vector table at 0x08010000."""
    if len(data) < 8:
        return False
    sp, reset = struct.unpack("<II", data[:8])
    return 0x20000000 <= sp <= 0x20020000 and 0x08010000 <= reset < 0x08100000


def main():
    p = argparse.ArgumentParser(description="Decrypt or encrypt FlashForge/Dremel firmware.")
    p.add_argument("mode", choices=["decrypt", "encrypt"])
    p.add_argument("input")
    p.add_argument("output")
    p.add_argument("--key", default="dremel",
                   help="dremel (default), flashforge, or a 16 character key")
    args = p.parse_args()

    key = KEYS.get(args.key, args.key).encode()
    if len(key) != 16:
        sys.exit("The key must be 16 characters.")

    with open(args.input, "rb") as f:
        data = f.read()
    result = process(data, key, args.mode == "encrypt")
    with open(args.output, "wb") as f:
        f.write(result)

    print(f"{args.mode}ed {len(data)} bytes -> {args.output}")
    if args.mode == "decrypt":
        if looks_like_firmware(result):
            print("Check passed: the output looks like valid firmware for address 0x08010000.")
        else:
            print("WARNING: the output does not look like valid firmware. "
                  "The file may be for another printer, or the key is wrong. Do not flash it.")
            sys.exit(2)


if __name__ == "__main__":
    main()
