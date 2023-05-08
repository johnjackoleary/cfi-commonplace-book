---
tags: [gait]
has-carb-heat: true
Vs: 40
Vs0: 35
cool-procedure: N/A for C152
engine-fire-kias: 85
power-on-stall-rpm: 2300
maneuver-rpm: ~2300
maneuver-kias: 90
---

| **(model::C152) Gaits** v1.0 |        **Flaps**        |          **RPM**          |       **IAS (kts)**        |
| ---------------------------- |:-----------------------:|:-------------------------:|:--------------------------:|
| ⚠️ V<sub>G</sub>             |                         |           idle            |          (Vg::60)          |
| 🛫 V<sub>R</sub>             |                         |            max            |           (Vr::50)           |
| V<sub>X(10°)</sub>           |           10°           |            max            |           (Vx10::54)           | 
| V<sub>X</sub>                |                         |            max            |           (Vx::55)           |
| 🛫 V<sub>Y</sub>             |                         |            max            |           (Vy::67)           |
| 🛫 V<sub>Climb</sub>         |                         |            max            |      (cruise-climb::80)      |
| Cruise                       |                         |      (cruise-rpm::2400)       |      (cruise-kias::100)       |
| Cruise Descent               |                         |    `=this.cruise-rpm`     |  (cruise-descent-kias::TBD)   |
| 🛬 Downwind                  |                         | (pattern-downwind-rpm::2100) | (pattern-downwind-kias::as req) |
| 🛬 Abeam Numbers             | (pattern-abeam-flaps::10°) |   (pattern-abeam-rpm::1600)   |   (pattern-abeam-kias::70)   |
| 🛬 Base                      | (pattern-base-flaps::20°)  |   (pattern-base-rpm::1600)    |   (pattern-base-kias::65)    |
| 🛬 Final                     | (pattern-final-flaps::30°) |  (pattern-final-rpm::as req)   |          (Vref::60)          |
| Short                        | (pattern-short-flaps::30°) |   (pattern-short-rpm::as req)   |         (Vshort::54)         |

| Topic         | Details                                                                                                       |
| ------------- |:------------------------------------------------------------------------------------------------------------- |
| Leaning       | Lean to RPM drop when above 3000'                                                                           | 
| V<sub>A</sub> | (Va-mgw::104) @ [mgw::1670]; (Va-dual::98) @ (dual-weight::1500) lb; (Va-single::93) @ (dual-single::1350) lb |
