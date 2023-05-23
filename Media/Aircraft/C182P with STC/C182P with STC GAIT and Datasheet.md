---
tags: [gait]
has-carb-heat: true
Vs:
Vs0:
cool-procedure: 23", <2450RPM, cowl open, CHT <380 (max 400)
engine-fire-speed: 100
power-on-stall-rpm:
maneuver-rpm:
maneuver-speed:
speed-units: mph
---

| **(model::C182P-STC)** v0.1 |         **Flaps**          |          **MP "**           |          **RPM**          | **IAS (`=this.speed-units`)** |
| --------------------------- |:--------------------------:|:---------------------------:|:-------------------------:|:-----------------------------:|
| ⚠️ V<sub>G</sub>            |                            |                             |           idle            |           (Vg::86)            |
| 🛫 V<sub>R</sub>            |                            |                             |            max            |           (Vr::60)            |
| V<sub>X(10°)</sub>          |            20°             |                             |            max            |          (Vx10::60)           |
| V<sub>X</sub>               |                            |                             |            max            |           (Vx::70)            |
| 🛫 V<sub>Y</sub>            |                            |                             |            max            |           (Vy::89)            |
| 🛫 V<sub>Climb</sub>        |                            |             23              |           2450            |      (cruise-climb::105)      |
| Cruise                      |                            |       (cruise-mp::23)       |    (cruise-rpm::2300)     |       (cruise-speed::)        |
| Cruise Descent              |                            |     `=this.cruise-mp`      |    `=this.cruise-rpm`     |  (cruise-descent-speed::90)   |
| 🛬 Downwind                 |                            |   (pattern-downwind-mp::)   | (pattern-downwind-rpm::)  | (pattern-downwind-speed::90)  |
| 🛬 Abeam Numbers            | (pattern-abeam-flaps::10°) |    (pattern-abeam-mp::)     |   (pattern-abeam-rpm::)   |   (pattern-abeam-speed::80)   |
| 🛬 Base                     | (pattern-base-flaps::20°)  |     (pattern-base-mp::)     |   (pattern-base-rpm::)    |   (pattern-base-speed::70)    |
| 🛬 Final                    | (pattern-final-flaps::40°) | (pattern-final-mp::as req) | (pattern-final-rpm::max)  |          (Vref::70)           |
| Short                       | (pattern-short-flaps::40°) | (pattern-short-mp::as req)  | (pattern-short-rpm:: max) |         (Vshort::69)          |

| Topic         | Details                                                                                                           |
| ------------- |:----------------------------------------------------------------------------------------------------------------- |
| Leaning       | Peak EGT –75° F                                                                                                   |
| Cooling       | `=this.cooling-procedure`                                                                                                                  |
| V<sub>A</sub> | (Va-mgw::128) @ [mgw::3100]; (Va-dual::115) @ (dual-weight::2500) lb; (Va-single::105) @ (single-weight::2100) lb -> start with 18"-2300RPM |
