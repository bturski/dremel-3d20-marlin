; Dremel 3D20 + Marlin 2 end G-code for PrusaSlicer
G1 E-2 F1500                          ; retract
M104 S0                               ; nozzle heater off
M107                                  ; part fan off
G1 Z{min(max_layer_z + 10, 140)} F800 ; lower the bed away from the part
G28 X Y                               ; park at the back right
M84                                   ; motors off
