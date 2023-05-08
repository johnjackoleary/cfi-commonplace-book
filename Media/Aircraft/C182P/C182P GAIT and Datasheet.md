---
tags: [gait]
has-carb-heat:
Vs:
Vs0:
cool-procedure:
engine-fire-kias:
power-on-stall-rpm:
maneuver-rpm:
maneuver-kias:
---

| **(model::) Gaits** v0.0 |        **Flaps**        |          **RPM**          |       **IAS (kts)**        |
| ---------------------------- |:-----------------------:|:-------------------------:|:--------------------------:|
| ⚠️ V<sub>G</sub>             |                         |           idle            |          (Vg::)          |
| 🛫 V<sub>R</sub>             |                         |            max            |           (Vr::)           |
| V<sub>X(10°)</sub>           |           10°           |            max            |           (Vx10::)           | 
| V<sub>X</sub>                |                         |            max            |           (Vx::)           |
| 🛫 V<sub>Y</sub>             |                         |            max            |           (Vy::)           |
| 🛫 V<sub>Climb</sub>         |                         |            max            |      (cruise-climb::)      |
| Cruise                       |                         |      (cruise-rpm::)       |      (cruise-kias::)       |
| Cruise Descent               |                         |    `=this.cruise-rpm`     |  (cruise-descent-kias::)   |
| 🛬 Downwind                  |                         | (pattern-downwind-rpm::) | (pattern-downwind-kias::) |
| 🛬 Abeam Numbers             | (pattern-abeam-flaps::) |   (pattern-abeam-rpm::)   |   (pattern-abeam-kias::)   |
| 🛬 Base                      | (pattern-base-flaps::)  |   (pattern-base-rpm::)    |   (pattern-base-kias::)    |
| 🛬 Final                     | (pattern-final-flaps::) |  (pattern-final-rpm:: req)   |          (Vref::)          |
| Short                        | (pattern-short-flaps::) |   (pattern-short-rpm:: req)   |         (Vshort::)         |

| Topic         | Details                                                                                                       |
| ------------- |:------------------------------------------------------------------------------------------------------------- |
| Leaning       | Lean to RPM drop when above 3000'                                                                           | 
| V<sub>A</sub> | (Va-mgw::) @ [mgw::3100]; (Va-dual::) @ (dual-weight::) lb; (Va-single::) @ (dual-single::) lb |
