---
tags: [gait]
has-carb-heat: true
Vs:
Vs0:
soft-takeoff-flaps :: 25°
cool-procedure:
engine-fire-speed: TBD
power-on-stall-rpm: 2400 RPM
maneuver-rpm: 2100rpm
maneuver-speed: 
speed-units: kts
---

| **(model::PA28-181)  Gait** v1.1kts |         **Flaps**          | **Pitch** |           **RPM**            | **IAS (`=this.speed-units`)** | **VSI (fpm)** |
| ----------------------------------- |:--------------------------:|:---------:|:----------------------------:|:-----------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>                    |                            |           |             idle             |           (Vg::76)            |               |
| 🛫 V<sub>R</sub>                    |                            |           |             max              |           (Vr::59)            |               |
| V<sub>X(25°)</sub>                  | (short-takeoff-flaps::25°) |           |             max              |        (Vx-short::50)         |               |
| V<sub>X</sub>                       |                            |           |             max              |           (Vx::64)            |               |
| 🛫 V<sub>Y</sub>                    |                            |   +10°    |             max              |           (Vy::76)            |     +600      |
| 🛫 V<sub>Climb</sub>                |                            |    +5°    |             max              |              95               |     +500      |
| Cruise                              |                            |    0°     |             2500             |                               |       0       |
| Cruise Descent                      |                            |  \-2.5°   |             2500             |                               |     \-500     |
| 🌫️ IAF Inbound Level                |                            |    +2°    |             2400             |              90               |       0       |
| 🌫️ IAF Inbound Descent              |                            |   \-2°    |             1900             |              90               |     \-700     |
| 🌫️ Prec Appr to DA                  |            10°             |   \-3°    |             2000             |              90               |     \-450     |
| 🌫️ Non-Prec Appr to MDA             |            10°             |   \-4°    |             2000             |              90               |     \-800     |
| 🛬 Downwind                         |                            |           | (pattern-downwind-rpm::2000) | (pattern-downwind-speed::90)  |       0       |
| 🛬 Abeam Numbers                    | (pattern-abeam-flaps::10°) |           |            1400?             |   (pattern-abeam-speed::75)   |               |
| 🛬 Base                             | (pattern-base-flaps::25°)  |           |            1400?             |   (pattern-base-speed::70)    |               |
| 🛬 Final                            | (pattern-final-flaps::40°) |           |            1400?             |          (Vref::66)           |               |
| Short                               | (pattern-short-flaps::40°) |           |            1400?             |         (Vshort::61?)         |               |

| Topic         | Details                                                                                                                                              |
| ------------- |:---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Leaning       | 100° ROP when above 5000'                                                                                                                            |
| V<sub>A</sub> | (Va-mgw::113) @ [mgw::2550]lb; (Va-dual::103) @ (dual-weight::2100)lb; (Va-single::100) @ (single-weight::1950)lb -> start with `=this.maneuver-rpm` |