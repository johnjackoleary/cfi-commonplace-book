---
tags: [gait]
has-carb-heat: true
Vs:
Vs0:
cool-procedure:
engine-fire-speed: TBD
power-on-stall-rpm: TBD
maneuver-rpm: 2100rpm
maneuver-speed: 
speed-units: mph
---

| **PA28-181 Gait** v1.0mph |         **Flaps**          | **Pitch** |           **RPM**            | **IAS (`=this.speed-units`)** | **VSI (fpm)** |
| ------------------------- |:--------------------------:|:---------:|:----------------------------:|:-----------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>          |                            |           |             idle             |           (Vg::87)            |               |
| 🛫 V<sub>R</sub>          |                            |           |             max              |           (Vr::68)            |               |
| V<sub>X(25°)</sub>        |            25°             |           |             max              |          (Vx25::57)           |               |
| V<sub>X</sub>             |                            |           |             max              |           (Vx::74)            |               |
| 🛫 V<sub>Y</sub>          |                            |   +10°    |             max              |           (Vy::87)            |     +600      |
| 🛫 V<sub>Climb</sub>      |                            |    +5°    |             max              |              100              |     +500      |
| Cruise                    |                            |    0°     |             2500             |                               |       0       |
| Cruise Descent            |                            |  \-2.5°   |             2500             |                               |     \-500     |
| 🌫️ IAF Inbound Level      |                            |    +2°    |             2200             |              105              |       0       |
| 🌫️ IAF Inbound Descent    |                            |   \-2°    |             2200              |              105              |     \-800     |
| 🌫️ Prec Appr to DA        |            10°             |   \-3°    |             2000             |              105              |     \-450     |
| 🌫️ Non-Prec Appr to MDA   |            10°             |   \-4°    |             2000              |              105              |     \-800     |
| 🛬 Downwind               |                            |           | (pattern-downwind-rpm::2000) | (pattern-downwind-speed::105) |       0       |
| 🛬 Abeam Numbers          | (pattern-abeam-flaps::10°) |           |            1400?             |   (pattern-abeam-speed::95)   |               |
| 🛬 Base                   | (pattern-base-flaps::25°)  |           |            1400?             |   (pattern-base-speed::85)    |               |
| 🛬 Final                  | (pattern-final-flaps::40°) |           |            1400?             |          (Vref::76)           |               |
| Short                     | (pattern-short-flaps::40°) |           |            1400?             |         (Vshort::70?)          |               |

| Topic         | Details                                                                                                                                              |
| ------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Leaning       | 100° ROP when above 5000'                                                                                                                            |
| V<sub>A</sub> | (Va-mgw::124) @ [mgw::2550]lb; (Va-dual::113) @ (dual-weight::2100)lb; (Va-single::108) @ (single-weight::1950)lb -> start with `=this.maneuver-rpm` |