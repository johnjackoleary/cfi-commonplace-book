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

| **(model::C152) Gaits** v0.0 |        **Flaps**        |          **RPM**          |       **IAS (kts)**        |
| ---------------------------- |:-----------------------:|:-------------------------:|:--------------------------:|
| ⚠️ V<sub>G</sub>             |                         |           idle            |          (Vg::60)          |
| 🛫 V<sub>R</sub>             |                         |            max            |           (Vr::)           |
| V<sub>X(10°)</sub>           |           10°           |            max            |           (Vx10::)           | 
| V<sub>X</sub>                |                         |            max            |           (Vx::)           |
| 🛫 V<sub>Y</sub>             |                         |            max            |           (Vy::)           |
| 🛫 V<sub>Climb</sub>         |                         |            max            |      (cruise-climb::)      |
| Cruise                       |                         |      (cruise-rpm::)       |      (cruise-kias::)       |
| Cruise Descent               |                         |    `=this.cruise-rpm`     |  (cruise-descent-kias::)   |
| 🛬 Downwind                  |                         | (pattern-downwind-rpm:: ) | (pattern-downwind-kias:: ) |
| 🛬 Abeam Numbers             | (pattern-abeam-flaps::) |   (pattern-abeam-rpm::)   |   (pattern-abeam-kias::)   |
| 🛬 Base                      | (pattern-base-flaps::)  |   (pattern-base-rpm::)    |   (pattern-base-kias::)    |
| 🛬 Final                     | (pattern-final-flaps::) |  (pattern-final-rpm:: )   |          (Vref::)          |
| Short                        | (pattern-short-flaps::) |   (pattern-short-rpm::)   |         (Vshort::)         |

| Topic              | Details                                   |
| ------------------ |:----------------------------------------- |
| Leaning            | 50° ROP when above 3000'                  | 
| V<sub>A</sub>      | (va-mgw::) @ [mgw::]; (Va-dual::) @ (dual-weight::) lb; (Va-single::) @ (dual-single::) lb |
