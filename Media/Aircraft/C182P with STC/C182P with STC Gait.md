---
tags: [gait]
has-carb-heat: true
Vs:
Vs0:
cool-procedure: 23", <2450RPM, cowl open, CHT <380 (max 400)
engine-fire-speed: 115
power-on-stall-rpm:
maneuver-rpm: 18"-2300RPM
maneuver-speed: 
speed-units: mph
---

| **(model::C182P-STC)** v1.2 |         **Flaps**          |          **MP "**          |          **RPM**          | **IAS (`=this.speed-units`)** | **FPM** |
| --------------------------- |:--------------------------:|:--------------------------:|:-------------------------:|:-----------------------------:| ------- |
| ⚠️ V<sub>G</sub>            |                            |                            |           idle            |           (Vg::86)            |         |
| 🛫 V<sub>R</sub>            |                            |                            |            max            |           (Vr::60)            |         |
| V<sub>X(20°)</sub>          |            20°             |                            |            max            |          (Vx10::63)           |         |
| V<sub>X</sub>               |                            |                            |            max            |           (Vx::73)            |         |
| 🛫 V<sub>Y</sub>            |                            |                            |            max            |           (Vy::91)            |         |
| 🛫 V<sub>Climb</sub>        |                            |             23             |           2450            |      (cruise-climb::105)      |         |
| Cruise                      |                            |      (cruise-mp::23)       |    (cruise-rpm::2300)     |       (cruise-speed::)        |         |
| Cruise Descent              |                            |     `=this.cruise-mp`      |    `=this.cruise-rpm`     |  (cruise-descent-speed::)   |         |
| 🌫️ IAF Inbound Level        |                            |                            |                           |              90               | 0       |
| 🌫️ IAF Inbound Descent      |                            |                            |                           |              90               | \-800   |
| 🌫️ Prec Appr to DA          |            10°             |             14             |                           |              100              | \-600   |
| 🌫️ Non-Prec Appr to MDA     |            10°             |                            |                           |              90               | \-800   |
| 🛬 Downwind                 |                            | (pattern-downwind-mp::18)  | (pattern-downwind-rpm::)  | (pattern-downwind-speed::100) | 0       |
| 🛬 Abeam Numbers            | (pattern-abeam-flaps::10°) |   (pattern-abeam-mp::15)   |   (pattern-abeam-rpm::)   |  (pattern-abeam-speed::100)   |     |
| 🛬 Base                     | (pattern-base-flaps::20°)  |   (pattern-base-mp::15)    |   (pattern-base-rpm::)    |   (pattern-base-speed::90)    |         |
| 🛬 Final                    | (pattern-final-flaps::40°) |   (pattern-final-mp::17)   | (pattern-final-rpm::max)  |          (Vref::80)           | -350     |
| Short                       | (pattern-short-flaps::40°) | (pattern-short-mp::as req) | (pattern-short-rpm:: max) |         (Vshort::70)          |         |

| Topic         | Details                                                                                                           |
| ------------- |:----------------------------------------------------------------------------------------------------------------- |
| Leaning       | Peak EGT –75° F                                                                                                   |
| Cooling       | `=this.cool-procedure`                                                                                                                  |
| V<sub>A</sub> | (Va-mgw::128) @ [mgw::3100]; (Va-dual::115) @ (dual-weight::2500) lb; (Va-single::105) @ (single-weight::2100) lb -> start with `=this.maneuver-rpm` |
