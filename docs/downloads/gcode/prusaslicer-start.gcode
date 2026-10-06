; Dremel 3D20 + Marlin 2 start G-code for PrusaSlicer
; Uses relative extrusion (M83). Turn on "Use relative E distances" in Printer Settings.
G90                               ; absolute XYZ moves
M83                               ; relative extrusion
M107                              ; part fan off
M104 S[first_layer_temperature]   ; start heating the nozzle
G28                               ; home X and Y to max, Z to min
M420 S1                           ; turn on the saved mesh (delete this line if you have not saved one)
G1 Z10 F800                       ; lower the bed
G1 X-108 Y-70 F3000               ; move to the front left corner
M109 S[first_layer_temperature]   ; wait for the nozzle to reach temperature
G1 Z0.3 F800
G1 Y60 E10 F1200                  ; purge line 1
G1 X-107.4 F1200
G1 Y-60 E8 F1200                  ; purge line 2
G1 E-0.8 F1500                    ; small retract
G1 Z2 F800
G92 E0
