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
---

| **(model::) Gaits** v0.0 |        **Flaps**        |          **RPM**          |       **IAS (kts)**        |
| ---------------------------- |:-----------------------:|:-------------------------:|:--------------------------:|
| ⚠️ V<sub>G</sub>             |                         |           idle            |          (Vg::)          |
| 🛫 V<sub>R</sub>             |                         |            max            |           (Vr::)           |
| V<sub>X(10°)</sub>           |           10°           |            max            |           (Vx10::)           | 
| V<sub>X</sub>                |                         |            max            |           (Vx::)           |
| 🛫 V<sub>Y</sub>             |                         |            max            |           (Vy::)           |
| 🛫 V<sub>Climb</sub>         |                         |            max            |      (cruise-climb::)      |
| Cruise                       |                         |      (cruise-rpm::)       |      (cruise-speed::)       |
| Cruise Descent               |                         |    `=this.cruise-rpm`     |  (cruise-descent-speed::)   |
| 🛬 Downwind                  |                         | (pattern-downwind-rpm::) | (pattern-downwind-speed::) |
| 🛬 Abeam Numbers             | (pattern-abeam-flaps::) |   (pattern-abeam-rpm::)   |   (pattern-abeam-speed::)   |
| 🛬 Base                      | (pattern-base-flaps::)  |   (pattern-base-rpm::)    |   (pattern-base-speed::)    |
| 🛬 Final                     | (pattern-final-flaps::) |  (pattern-final-rpm:: req)   |          (Vref::)          |
| Short                        | (pattern-short-flaps::) |   (pattern-short-rpm:: req)   |         (Vshort::)         |

| Topic         | Details                                                                                                       |
| ------------- |:------------------------------------------------------------------------------------------------------------- |
| Leaning       | TBD                                                                           | 
| V<sub>A</sub> | (Va-mgw::) @ [mgw::]; (Va-dual::) @ (dual-weight::) lb; (Va-single::) @ (single-weight::) lb |
