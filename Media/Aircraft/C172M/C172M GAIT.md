---
tags:
  - gait
has-carb-heat: true
Vs: 
Vs0: 
"soft-takeoff-flaps :": 25°
cool-procedure: 
engine-fire-speed: TBD
power-on-stall-rpm: 2400rpm
maneuver-rpm: 2100rpm
maneuver-speed: 
speed-units: mph
---

#todo :: everything here needs to be updated

| **(model::C172M)  Gait** v1.0 |         **Flaps**          | **Pitch** |           **RPM**           | **IAS (`=this.speed-units`)** | **VSI (fpm)** |
| ----------------------------- |:--------------------------:|:---------:|:---------------------------:|:-----------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>              |                            |           |            idle             |           (Vg::75)            |               |
| 🛫 V<sub>R</sub>              |                            |           |             max             |           (Vr::60)            |               |
| V<sub>X</sub>                 |                            |           |             max             |           (Vx::75)            |               |
| 🛫 V<sub>Y</sub>              |                            |   +10°    |             max             |           (Vy::90)            |     +TBD      |
| 🛫 V<sub>Climb</sub>          |                            |    +5°    |             max             |              90               |     +TBD      |
| Cruise                        |                            |    0°     |            TBD             |            TBD                   |       0       |
| Cruise Descent                |                            |  \-2.5°   |             TBD             |                               |     \-500     |
| 🛬 Downwind                   |                            |           | (pattern-downwind-rpm::TBD) | (pattern-downwind-speed::104)  |       0       |
| 🛬 Abeam Numbers              | (pattern-abeam-flaps::10°) |           |             TBD             |   (pattern-abeam-speed::86)   |               |
| 🛬 Base                       | (pattern-base-flaps::25°)  |           |             TBD             |   (pattern-base-speed::75)    |               |
| 🛬 Final                      | (pattern-final-flaps::40°) |           |             TBD             |          (Vref::66)           |               |
| Short                         | (pattern-short-flaps::40°) |           |             TBD             |         (Vshort::69)         |               |

<br>

| Topic         | Details                                                                                                                                              |
| ------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Leaning       | 100° ROP when above 5000'                                                                                                                            |
| V<sub>A</sub> | (Va-mgw::113) @ [mgw::2300]lb; (Va-dual::103) @ (dual-weight::2100)lb; (Va-single::100) @ (single-weight::1950)lb -> start with `=this.maneuver-rpm` |
| Short T.O.   | (short-takeoff-flaps::10°) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{-, 68}@`=this.mgw`lb; {-,63}@2000; {41,58}@1700lb                                                                                                                                                     |
