---
tags: [gait]
has-carb-heat: true
Vs:
Vs0:
cool-procedure:
engine-fire-speed: TBD
power-on-stall-rpm:
maneuver-rpm: TBD
maneuver-speed: 
speed-units: kts
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



| **PA28-181  Gait** v1.0 | **Flaps** | **Pitch** |           **RPM**            | **IAS (`=this.speed-units`)** | **VSI (fpm)** |
| ----------------------- |:---------:|:---------:|:----------------------------:|:-----------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>        |           |           |             idle             |   (Vg::76 MGW/61 1631 lbs)    |               |
| 🛫 V<sub>R</sub>        |           |           |             max              |           (Vr::59)            |               |
| V<sub>X(25°)</sub>      |    25°    |           |             max              |          (Vx25::50)           |               |
| V<sub>X</sub>           |           |           |             max              |           (Vx::64)            |               |
| 🛫 V<sub>Y</sub>        |           |   +10°    |             max              |            (Vy::76            |     +600      |
| 🛫 V<sub>Climb</sub>    |           |    +5°    |             max              |                               |     +500      |
| Cruise                  |           |    0°     |             2500             |                               |       0       |
| Cruise Descent          |           |  \-2.5°   |             2500             |                               |     \-500     |
| 🌫️ IAF Inbound Level    |           |    +2°    |             2200             |              90               |       0       |
| 🌫️ IAF Inbound Descent  |           |   \-2°    |             TBD              |              90               |     \-800     |
| 🌫️ Prec Appr to DA      |    10°    |   \-3°    |             2000             |              90               |     \-450     |
| 🌫️ Non-Prec Appr to MDA |    10°    |   \-4°    |             TBD              |              90               |     \-800     |
| 🛬 Downwind             |           |           | (pattern-downwind-rpm::2000) | (pattern-downwind-speed::90)  |       0       |
| 🛬 Abeam Numbers        |    10°    |           |            1400?             |              (pattern-abeam-speed::75)               |               |
| 🛬 Base                 |    25°    |           |            1400?             |              (pattern-base-speed::70)               |               |
| 🛬 Final                |    40°    |           |            1400?             |              (Vref::66)               |               |
| Short                   |    40°    |           |            1400?             |              (Vshort::61)               |               |

| Topic              | Details                                   |
| ------------------ |:----------------------------------------- |
| Leaning            | 100° ROP when above 5000'                  | 
| V<sub>A</sub>      | 113 @ max<br>89 @ 1634 lb |