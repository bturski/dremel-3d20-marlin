#!/usr/bin/env python3
"""Build the importable slicer profiles from one set of values.

Edit the settings below or the G-code files in docs/downloads/gcode/, then run:

    python scripts/build_profiles.py

Outputs:
    docs/downloads/prusaslicer/Dremel3D20_Marlin_PrusaSlicer.ini
    docs/downloads/cura/definitions/dremel_3d20_marlin.def.json
    docs/downloads/cura/definitions/dremel_3d20_marlin_extruder_0.def.json
    docs/downloads/cura/Dremel3D20_Marlin_Cura.zip

Run with --check in CI to fail if the committed files are out of date.
"""

import io
import json
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DL = ROOT / "docs" / "downloads"
GCODE = DL / "gcode"

SITE = "https://bturski.github.io/dremel-3d20-marlin"
NAME = "Dremel 3D20 Marlin"

# ---------------------------------------------------------------- PrusaSlicer

PRUSA_PRINT = {
    "layer_height": "0.2", "first_layer_height": "0.25", "perimeters": "2",
    "top_solid_layers": "5", "bottom_solid_layers": "4",
    "fill_density": "15%", "fill_pattern": "gyroid",
    "top_fill_pattern": "monotonic", "bottom_fill_pattern": "monotonic",
    "seam_position": "aligned",
    "skirts": "2", "skirt_distance": "3", "skirt_height": "1", "brim_width": "0",
    "elefant_foot_compensation": "0.1", "support_material": "0",
    "perimeter_speed": "40", "small_perimeter_speed": "20", "external_perimeter_speed": "30",
    "infill_speed": "60", "solid_infill_speed": "45", "top_solid_infill_speed": "30",
    "support_material_speed": "40", "support_material_interface_speed": "100%",
    "bridge_speed": "30", "gap_fill_speed": "25", "ironing_speed": "15",
    "travel_speed": "120", "travel_speed_z": "0", "first_layer_speed": "20",
    "default_acceleration": "800", "external_perimeter_acceleration": "500",
    "perimeter_acceleration": "800", "infill_acceleration": "1000",
    "solid_infill_acceleration": "800", "top_solid_infill_acceleration": "600",
    "bridge_acceleration": "500", "first_layer_acceleration": "300", "travel_acceleration": "1000",
    "gcode_label_objects": "octoprint", "arc_fitting": "emit_center", "gcode_comments": "0",
    "output_filename_format": "{input_filename_base}_{layer_height}mm_{printing_filament_types}_{print_time}.gcode",
    "compatible_printers": "",
    "compatible_printers_condition": "printer_notes=~/.*DREMEL3D20MARLIN.*/",
}

PRUSA_FILAMENT = {
    "filament_type": "PLA", "filament_diameter": "1.75", "filament_density": "1.24",
    "filament_cost": "20", "extrusion_multiplier": "1",
    "temperature": "210", "first_layer_temperature": "215",
    "bed_temperature": "0", "first_layer_bed_temperature": "0",
    "filament_max_volumetric_speed": "7",
    "cooling": "1", "fan_always_on": "1", "min_fan_speed": "100", "max_fan_speed": "100",
    "bridge_fan_speed": "100", "disable_fan_first_layers": "1", "full_fan_speed_layer": "0",
    "fan_below_layer_time": "60", "slowdown_below_layer_time": "10", "min_print_speed": "10",
    "filament_notes": "Starting point for PLA on the unheated stock bed. Keep the nozzle at or below 230 C.",
    "compatible_printers": "",
    "compatible_printers_condition": "printer_notes=~/.*DREMEL3D20MARLIN.*/",
}

PRUSA_PRINTER = {
    "printer_technology": "FFF", "printer_model": "", "printer_vendor": "",
    "printer_notes": "DREMEL3D20MARLIN\\nDremel 3D20 running moonglow FlashForge_Marlin 2.0.9.x. Origin is the bed center.",
    "bed_shape": "-115x-75,115x-75,115x75,-115x75", "max_print_height": "140", "z_offset": "0",
    "gcode_flavor": "marlin2", "binary_gcode": "0", "remaining_times": "0",
    "use_relative_e_distances": "1", "autoemit_temperature_commands": "0",
    "thumbnails": "", "silent_mode": "0",
    "machine_limits_usage": "time_estimate_only",
    "machine_max_feedrate_x": "300,300", "machine_max_feedrate_y": "300,300",
    "machine_max_feedrate_z": "20,20", "machine_max_feedrate_e": "27,27",
    "machine_max_acceleration_x": "1000,1000", "machine_max_acceleration_y": "1000,1000",
    "machine_max_acceleration_z": "150,150", "machine_max_acceleration_e": "4000,4000",
    "machine_max_acceleration_extruding": "1000,1000",
    "machine_max_acceleration_retracting": "1000,1000",
    "machine_max_acceleration_travel": "1000,1000",
    "machine_max_jerk_x": "10,10", "machine_max_jerk_y": "10,10",
    "machine_max_jerk_z": "0.3,0.3", "machine_max_jerk_e": "5,5",
    "machine_min_extruding_rate": "0,0", "machine_min_travel_rate": "0,0",
    "nozzle_diameter": "0.4", "min_layer_height": "0.08", "max_layer_height": "0.3",
    "retract_length": "1", "retract_speed": "25", "deretract_speed": "20",
    "retract_restart_extra": "0", "retract_before_travel": "1.5", "retract_layer_change": "1",
    "wipe": "1", "retract_before_wipe": "70%",
    "retract_lift": "0.2", "retract_lift_above": "0", "retract_lift_below": "0",
    "travel_ramping_lift": "0",
    "layer_gcode": "", "before_layer_gcode": "",
}

# ----------------------------------------------------------------------- Cura


def dv(v):
    return {"default_value": v}


def vv(v):
    return {"value": v}


CURA_OVERRIDES = {
    "machine_name": dv("Dremel 3D20 (Marlin)"),
    "machine_width": dv(230), "machine_depth": dv(150), "machine_height": dv(140),
    "machine_center_is_zero": dv(True), "machine_heated_bed": dv(False),
    "machine_shape": dv("rectangular"),
    "machine_gcode_flavor": dv("RepRap (Marlin/Sprinter)"),
    "machine_max_feedrate_x": dv(300), "machine_max_feedrate_y": dv(300),
    "machine_max_feedrate_z": dv(20), "machine_max_feedrate_e": dv(27),
    "machine_max_acceleration_x": dv(1000), "machine_max_acceleration_y": dv(1000),
    "machine_max_acceleration_z": dv(150), "machine_max_acceleration_e": dv(4000),
    "machine_acceleration": dv(800),
    "machine_max_jerk_xy": dv(10), "machine_max_jerk_z": dv(0.3), "machine_max_jerk_e": dv(5),
    "relative_extrusion": dv(False),
    "layer_height": dv(0.2), "layer_height_0": dv(0.25),
    "wall_line_count": vv(2), "top_thickness": vv(1.0), "bottom_thickness": vv(0.8),
    "infill_sparse_density": dv(15), "infill_pattern": vv("'gyroid'"),
    "xy_offset_layer_0": vv(-0.1),
    "speed_print": dv(50), "speed_infill": vv(60), "speed_wall_0": vv(30),
    "speed_wall_x": vv(40), "speed_topbottom": vv(30), "speed_support": vv(40),
    "speed_travel": vv(120), "speed_layer_0": vv(20),
    "acceleration_enabled": dv(True), "acceleration_print": vv(800),
    "acceleration_infill": vv(1000), "acceleration_wall_0": vv(500),
    "acceleration_wall_x": vv(800), "acceleration_topbottom": vv(600),
    "acceleration_support": vv(800), "acceleration_travel": vv(1000),
    "acceleration_layer_0": vv(300), "acceleration_travel_layer_0": vv(1000),
    "jerk_enabled": dv(False),
    "retraction_enable": dv(True), "retraction_amount": dv(1.0), "retraction_speed": dv(25),
    "retraction_retract_speed": vv("retraction_speed"), "retraction_prime_speed": vv(20),
    "retraction_hop_enabled": dv(True), "retraction_hop": dv(0.2),
    "retraction_combing": vv("'noskin'"),
    "cool_fan_enabled": dv(True), "cool_fan_speed": vv(100), "cool_fan_full_layer": vv(2),
    "cool_min_layer_time": dv(10),
    "adhesion_type": dv("skirt"), "skirt_line_count": dv(2), "skirt_gap": dv(3),
    "print_sequence": {"enabled": False},
}


def read_gcode(name):
    return (GCODE / name).read_text().rstrip("\n")


def build():
    files = {}

    # PrusaSlicer bundle
    printer = dict(PRUSA_PRINTER)
    printer["start_gcode"] = read_gcode("prusaslicer-start.gcode").replace("\n", "\\n")
    printer["end_gcode"] = read_gcode("prusaslicer-end.gcode").replace("\n", "\\n")
    lines = [
        "# PrusaSlicer config bundle for the Dremel 3D20 running Marlin 2 (moonglow FlashForge_Marlin).",
        "# Import with File > Import > Import Config Bundle.",
        f"# Guide: {SITE}/slicers/prusaslicer/",
        "# Generated by scripts/build_profiles.py. Edit that script, not this file.",
        "",
    ]
    for section, name, values in [
        ("print", f"{NAME} 0.20mm QUALITY", PRUSA_PRINT),
        ("filament", f"{NAME} PLA", PRUSA_FILAMENT),
        ("printer", NAME, printer),
    ]:
        lines.append(f"[{section}:{name}]")
        lines += [f"{k} = {v}" for k, v in values.items()]
        lines.append("")
    lines += ["[presets]", f"print = {NAME} 0.20mm QUALITY", f"filament = {NAME} PLA",
              f"printer = {NAME}", ""]
    files[DL / "prusaslicer" / "Dremel3D20_Marlin_PrusaSlicer.ini"] = "\n".join(lines).encode()

    # Cura definitions
    overrides = dict(CURA_OVERRIDES)
    overrides["machine_start_gcode"] = dv(read_gcode("cura-start.gcode") + "\n")
    overrides["machine_end_gcode"] = dv(read_gcode("cura-end.gcode") + "\n")
    printer_def = {
        "version": 2,
        "name": "Dremel 3D20 (Marlin)",
        "inherits": "fdmprinter",
        "metadata": {
            "visible": True,
            "author": "dremel-3d20-marlin guide",
            "manufacturer": "Dremel",
            "file_formats": "text/x-gcode",
            "has_materials": True,
            "preferred_quality_type": "normal",
            "machine_extruder_trains": {"0": "dremel_3d20_marlin_extruder_0"},
        },
        "overrides": overrides,
    }
    extruder_def = {
        "version": 2,
        "name": "Extruder 1",
        "inherits": "fdmextruder",
        "metadata": {"machine": "dremel_3d20_marlin", "position": "0"},
        "overrides": {
            "extruder_nr": dv(0),
            "machine_nozzle_size": dv(0.4),
            "material_diameter": dv(1.75),
        },
    }
    defs = DL / "cura" / "definitions"
    p_json = (json.dumps(printer_def, indent=2) + "\n").encode()
    e_json = (json.dumps(extruder_def, indent=2) + "\n").encode()
    files[defs / "dremel_3d20_marlin.def.json"] = p_json
    files[defs / "dremel_3d20_marlin_extruder_0.def.json"] = e_json

    # Zip with fixed timestamps so the bytes only change when the content does
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        for name, data in [("dremel_3d20_marlin.def.json", p_json),
                           ("dremel_3d20_marlin_extruder_0.def.json", e_json)]:
            info = zipfile.ZipInfo(name, date_time=(2024, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    files[DL / "cura" / "Dremel3D20_Marlin_Cura.zip"] = buf.getvalue()
    return files


def main():
    check = "--check" in sys.argv
    stale = []
    for path, data in build().items():
        if check:
            if not path.exists() or path.read_bytes() != data:
                stale.append(path.relative_to(ROOT))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            print(f"wrote {path.relative_to(ROOT)}")
    if stale:
        print("These files are out of date. Run: python scripts/build_profiles.py")
        for p in stale:
            print(f"  {p}")
        sys.exit(1)


if __name__ == "__main__":
    main()
