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

| **(model::) Gaits** v0.0 | **Flaps** | **RPM** | **IAS (`=this.speed-units`)** |
| ------------------------ |:---------:|:-------:|:-----------------------------:|
| ⚠️ V<sub>G</sub>         |           |  idle   |            (Vg::)             |
| 🛫 V<sub>R</sub>         |           |   max   |            (Vr::)             |
| V<sub>X</sub>            |           |   max   |            (Vx::)             |
| 🛫 V<sub>Y</sub>         |           |   max   |            (Vy::)             |
| 🛫 V<sub>Climb</sub>     |           |   max   |                               |
| Cruise                   |           |         |                               |
| Cruise Descent           |           |         |                               |
| 🛬 Downwind              |           |         |                               |
| 🛬 Abeam Numbers         |           |         |                               |
| 🛬 Base                  |           |         |                               |
| 🛬 Final                 |           |         |           (Vref::)            |
| Short                    |           |         |          (Vshort::)           |

<br>

| Topic          | Details                                                                                      |
| -------------- |:-------------------------------------------------------------------------------------------- |
| Leaning        | TBD                                                                                          |
| V<sub>A</sub>  | (Va-mgw::) @ [mgw::]; (Va-dual::) @ (dual-weight::) lb; (Va-single::) @ (single-weight::) lb |
| Short T.O.     | (short-takeoff-flaps::) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{, }@`=this.mgw`lb; {,}@lb    |
| Fuel Burn Est. |                                                                                              |
