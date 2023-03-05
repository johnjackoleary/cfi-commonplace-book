---
tags: [gait]
has-carb-heat: true
Vs:
Vs0:
cool-procedure: N/A for C152
engine-fire-speed:
power-on-stall-rpm: 
---

#todo confirm fire speed

| **(model::C152) Gaits** v0.0 |        **Flaps**        | **Pitch** |          **RPM**          |       **IAS (kts)**        | **VSI (fpm)** |
| ---------------------------- |:-----------------------:|:---------:|:-------------------------:|:--------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>             |                         |    TBD    |           idle            |          (Vg::60)          |      TBD      |
| 🛫 V<sub>R</sub>             |           10°           |    TBD    |            max            |             55             |      TBD      |
| V<sub>X(10°)</sub>           |           10°           |    TBD    |            max            |             56             |      TBD      |
| V<sub>X</sub>                |                         |    TBD    |            max            |           (Vx::)           |      TBD      |
| 🛫 V<sub>Y</sub>             |                         |   +10°    |            max            |           (Vy::)           |     +600      |
| 🛫 V<sub>Climb</sub>         |                         |    +5°    |            max            |             90             |     +500      |
| Cruise                       |                         |    0°     |           2500            |            105             |       0       |
| Cruise Descent               |                         |  \-2.5°   |           2500            |            115             |     \-500     |
| 🌫️ IAF Inbound Level         |                         |    +2°    |           2200            |             90             |       0       |
| 🌫️ IAF Inbound Descent       |                         |   \-2°    |           1700            |             90             |     \-800     |
| 🌫️ Prec Appr to DA           |           10°           |   \-3°    |           1900            |             90             |     \-450     |
| 🌫️ Non-Prec Appr to MDA      |           10°           |   \-4°    |           1500            |             90             |     \-800     |
| 🛬 Downwind                  |                         |    TBD    | (pattern-downwind-rpm:: ) | (pattern-downwind-kias:: ) |       0       |
| 🛬 Abeam Numbers             | (pattern-abeam-flaps::) |    TBD    |   (pattern-abeam-rpm::)   |   (pattern-abeam-kias::)   |      TBD      |
| 🛬 Base                      | (pattern-base-flaps::)  |    TBD    |   (pattern-base-rpm::)    |   (pattern-base-kias::)    |      TBD      |
| 🛬 Final                     | (pattern-final-flaps::) |    TBD    |  (pattern-final-rpm:: )   |          (Vref::)          |      TBD      |
| Short                        | (pattern-short-flaps::) |    TBD    |   (pattern-short-rpm::)   |         (Vshort::)         |      TBD      |

| Topic              | Details                                   |
| ------------------ |:----------------------------------------- |
| Leaning            | 50° ROP when above 3000'                  | 
| V<sub>A</sub>      | (va-mgw::) @ max<br>98 @ 2200 lb<br>90 @ 1900 lb |


### V Speeds (KIAS)
Vx :: 62
Vy :: 74
Va-mgw :: 105
Va-dual :: 100
Vref :: 65
Vshort :: 61

### Weights
mgw :: 2550

### Maneuvering
Va-dual-rpm :: 2200
flaps-for-stall-recover :: 20°
