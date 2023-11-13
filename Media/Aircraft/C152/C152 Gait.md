---
tags: [gait]
has-carb-heat: true
Vs: 40
Vs0: 35
soft-takeoff-flaps :: 10°
cool-procedure: N/A for C152
engine-fire-speed: 85
power-on-stall-rpm: 2300
maneuver-rpm: ~2300
maneuver-speed: 90
speed-units: kts
---

| **(model::C152) Gaits** v1.1 |         **Flaps**          |           **RPM**            |          **IAS (kts)**           |
| ---------------------------- |:--------------------------:|:----------------------------:|:--------------------------------:|
| ⚠️ V<sub>G</sub>             |                            |             idle             |             (Vg::60)             |
| 🛫 V<sub>R</sub>             |                            |             max              |             (Vr::50)             |
| V<sub>X(10°)</sub>           |   (short-takeoff-flaps::10°)    |             max              |            (Vx-short::54)            |
| V<sub>X</sub>                |                            |             max              |             (Vx::55)             |
| 🛫 V<sub>Y</sub>             |                            |             max              |             (Vy::67)             |
| 🛫 V<sub>Climb</sub>         |                            |             max              |        (cruise-climb::80)        |
| Cruise                       |                            |      (cruise-rpm::2400)      |       (cruise-speed::100)        |
| Cruise Descent               |                            |      `=this.cruise-rpm`      |   (cruise-descent-speed::TBD)    |
| 🛬 Downwind                  |                            | (pattern-downwind-rpm::2100) | (pattern-downwind-speed::as req) |
| 🛬 Abeam Numbers             | (pattern-abeam-flaps::10°) |  (pattern-abeam-rpm::1500)   |    (pattern-abeam-speed::70)     |
| 🛬 Base                      | (pattern-base-flaps::20°)  |   (pattern-base-rpm::1500)   |     (pattern-base-speed::65)     |
| 🛬 Final                     | (pattern-final-flaps::30°) | (pattern-final-rpm::as req)  |            (Vref::60)            |
| Short                        | (pattern-short-flaps::30°) | (pattern-short-rpm::as req)  |           (Vshort::54)           |


| Topic         | Details                                                                                                       |
| ------------- |:------------------------------------------------------------------------------------------------------------- |
| Leaning       | Lean to RPM drop when above 3000'                                                                           | 
| V<sub>A</sub> | (Va-mgw::104) @ [mgw::1670]; (Va-dual::98) @ (dual-weight::1500) lb; (Va-single::93) @ (single-weight::1350) lb |
