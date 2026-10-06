; Dremel 3D20 + Marlin 2 end G-code for UltiMaker Cura
G91                ; relative moves
G1 E-2 F1500       ; retract
G1 Z10 F800        ; lower the bed 10 mm (Marlin stops it at the 140 mm limit)
G90                ; absolute moves
M104 S0            ; nozzle heater off
M107               ; part fan off
G28 X Y            ; park at the back right
M84                ; motors off
