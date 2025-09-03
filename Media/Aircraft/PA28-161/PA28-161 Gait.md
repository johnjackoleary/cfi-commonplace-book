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

| **(model::PA28-161) Gaits** v0.1 | **Flaps** | **RPM** | **IAS (`=this.speed-units`)** |
| ------------------------ |:---------:|:-------:|:-----------------------------:|
| ⚠️ V<sub>G</sub>         |           |  idle   |           (Vg::73)            |
| 🛫 V<sub>R</sub>         |           |   max   |           (Vr::55)            |
| V<sub>X</sub>            |           |   max   |           (Vx::63)            |
| 🛫 V<sub>Y</sub>         |           |   max   |           (Vy::79)            |
| 🛫 V<sub>Climb</sub>     |           |   max   |              ~87              |
| Cruise                   |           |  2400   |             ~110              |
| Cruise Descent           |           |  2500   |             ~126              |
| 🛬 Downwind              |     0     |  ~2100  |              90               |
| 🛬 Abeam Numbers         |    10     |  ~1500  |              80               |
| 🛬 Base                  |    25     |  ~1500  |              75               |
| 🛬 Final                 |    40     |  ~1500  |          (Vref::63)           |
| Short                    |    40     |  ~1500  |         (Vshort::60)          |

<br>

| Topic          | Details                                                                                                       |
| -------------- |:------------------------------------------------------------------------------------------------------------- |
| Leaning        | 50°F ROP, or lean until rough then enrich to smooth                                                           |
| V<sub>A</sub>  | (Va-mgw::111) @ [mgw::2440 lb]; 88 @ 1531 lb                                                                  |
| Short T.O.     | (short-takeoff-flaps::25°) Flaps, {*Rotate*, *50ft*} @ *weight*:<br>{52, 57}@`=this.mgw` lb; {48, 53}@ 2200lb |
| Fuel Burn Est. | ~10 GPH (pessimistic)                                                                                         |
| Magnetos  | 175 RPM max; 50 RPM diff                                                                                                               |
