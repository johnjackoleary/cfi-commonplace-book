---
tags: [gait]
has-carb-heat:
Vs:
Vs0:
soft-takeoff-flaps:
cool-procedure:
engine-fire-speed:
power-on-stall-rpm:
maneuver-rpm:
maneuver-speed:
speed-units:
---

| **(model::) Gaits** v0.0 | **Flaps** | **Pitch** | **RPM** | **IAS (`=this.speed-units`)** | **FPM** |
| ------------------------ |:---------:| --------- |:-------:|:-----------------------------:| ------- |
| ⚠️ V<sub>G</sub>         |           |           |  idle   |           (Vg::68)            |         |
| 🛫 V<sub>R</sub>         |           |           |   max   |           (Vr::55)            |         |
| V<sub>X</sub>            |           |           |   max   |           (Vx::62)            |         |
| 🛫 V<sub>Y</sub>         |           | 10°       |   max   |           (Vy::74)            |         |
| 🛫 V<sub>Climb</sub>     |           | 7°        |   max   |              90               | 1100    |
| Cruise                   |           |           |         |                               |         |
| Cruise Descent           |           |           |         |                               |         |
| 🌫️ IAF Inbound Level     |           | 2°        |  2100   |              90               | 0       |
| 🌫️ IAF Inbound Descent   |           | -4°       |  1600   |              90               | -800    |
| 🌫️ Prec Appr to DA       |    10°    | -3°       |  1900   |              90               | -450    |
| 🌫️ Non-Prec Appr to MDA  |    10°    | -6°       |  1800   |              90               | -800    |
| 🛬 Downwind              |           |           |         |                               |         |
| 🛬 Abeam Numbers         |           |           |         |                               |         |
| 🛬 Base                  |           |           |         |                               |         |
| 🛬 Final                 |           |           |         |           (Vref::)            |         |
| Short                    |           |           |         |          (Vshort::)           |         |

<br>

| Topic          | Details                                                                                      |
| -------------- |:-------------------------------------------------------------------------------------------- |
| Leaning        | TBD                                                                                          |
| V<sub>A</sub>  | (Va-mgw::) @ [mgw::]; (Va-dual::) @ (dual-weight::) lb; (Va-single::) @ (single-weight::) lb |
| Short T.O.     | (short-takeoff-flaps::) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{, }@`=this.mgw`lb; {,}@lb    |
| Fuel Burn Est. |                                                                                              |
