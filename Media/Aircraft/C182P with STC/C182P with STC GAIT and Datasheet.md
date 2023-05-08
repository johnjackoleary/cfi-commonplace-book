---
tags: [gait]
has-carb-heat:
Vs:
Vs0:
cool-procedure:
engine-fire-speed:
power-on-stall-rpm:
maneuver-rpm:
maneuver-speed:
speed-units: mph
---

| **(model::C182P-STC)** v0.0 |        **Flaps**        |          **RPM**          |       **IAS (`=this.speed-units`)**       |
| --------------------------------- |:-----------------------:|:-------------------------:|:-------------------------:|
| ⚠️ V<sub>G</sub>                  |                         |           idle            |         (Vg::86)          |
| 🛫 V<sub>R</sub>                  |                         |            max            |          (Vr::)           |
| V<sub>X(10°)</sub>                |           10°           |            max            |         (Vx10::)          |
| V<sub>X</sub>                     |                         |            max            |          (Vx::)           |
| 🛫 V<sub>Y</sub>                  |                         |            max            |          (Vy::)           |
| 🛫 V<sub>Climb</sub>              |                         |            max            |     (cruise-climb::)      |
| Cruise                            |                         |      (cruise-rpm::)       |      (cruise-speed::)      |
| Cruise Descent                    |                         |    `=this.cruise-rpm`     |  (cruise-descent-speed::)  |
| 🛬 Downwind                       |                         | (pattern-downwind-rpm::)  | (pattern-downwind-speed::) |
| 🛬 Abeam Numbers                  | (pattern-abeam-flaps::) |   (pattern-abeam-rpm::)   |  (pattern-abeam-speed::)   |
| 🛬 Base                           | (pattern-base-flaps::)  |   (pattern-base-rpm::)    |   (pattern-base-speed::)   |
| 🛬 Final                          | (pattern-final-flaps::) | (pattern-final-rpm:: req) |         (Vref::)          |
| Short                             | (pattern-short-flaps::) | (pattern-short-rpm:: req) |        (Vshort::69)         |

| Topic         | Details                                                                                                       |
| ------------- |:------------------------------------------------------------------------------------------------------------- |
| Leaning       |                                                                           | 
| V<sub>A</sub> | (Va-mgw::128) @ [mgw::3100]; (Va-dual::115) @ (dual-weight::2500) lb; (Va-single::105) @ (single-weight::2100) lb |
