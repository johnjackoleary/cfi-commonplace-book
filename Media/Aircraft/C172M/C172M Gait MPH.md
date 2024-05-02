---
tags:
  - gait
has-carb-heat: true
Vs: 54
Vs0: 47
soft-takeoff-flaps: tbd
cool-procedure: 
engine-fire-speed: tbd
power-on-stall-rpm: tbd
maneuver-rpm: 2200RPM
maneuver-speed: 
speed-units: mph
---

| **(model::C172M)  Gait** v1.0 |         **Flaps**          | **Pitch** |           **RPM**           | **IAS (`=this.speed-units`)** | **VSI (fpm)** |
| ----------------------------- |:--------------------------:|:---------:|:---------------------------:|:-----------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>              |                            |           |            idle             |           (Vg::75)            |               |
| 🛫 V<sub>R</sub>              |                            |           |             max             |           (Vr::63)            |               |
| V<sub>X</sub>                 |                            |           |             max             |           (Vx::68)            |               |
| 🛫 V<sub>Y</sub>              |                            |   +10°    |             max             |           (Vy::84)            |     +tbd      |
| 🛫 V<sub>Climb</sub>          |                            |    +5°    |             max             |              tbd               |     +tbd      |
| Cruise                        |                            |    0°     |            tbd             |            tbd                   |       0       |
| Cruise Descent                |                            |  \-2.5°   |             tbd             |                               |     \-500     |
| 🛬 Downwind                   |                            |           | (pattern-downwind-rpm::tbd) | (pattern-downwind-speed::104)  |       0       |
| 🛬 Abeam Numbers              | (pattern-abeam-flaps::10°) |           |             tbd             |   (pattern-abeam-speed::tbd)   |               |
| 🛬 Base                       | (pattern-base-flaps::25°)  |           |             tbd             |   (pattern-base-speed::86)    |               |
| 🛬 Final                      | (pattern-final-flaps::30°) |           |             tbd             |          (Vref::75)           |               |
| Short                         | (pattern-short-flaps::40°) |           |             tbd             |         (Vshort::69)         |               |

<br>

| Topic         | Details                                                                                                     |
| ------------- |:----------------------------------------------------------------------------------------------------------- |
| Leaning       | Lean for peak RPM                                                                                           |
| V<sub>A</sub> | (Va-mgw::112) @ [mgw::2300]lb; (Va-single::92) @ (single-weight::1600)lb -> start with `=this.maneuver-rpm` | 
| Short T.O.    | (short-takeoff-flaps::0°) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{`=this.Vr`, 68}@`=this.mgw`lb; {`=this.Vr`,63}@2000lb        |
