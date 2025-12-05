---
tags: [gait]
has-carb-heat: false
Vs:
Vs0:
soft-takeoff-flaps:
cool-procedure:
engine-fire-speed:
power-on-stall-rpm:
maneuver-rpm:
maneuver-speed:
speed-units: kts
---

| **(model::PA32-301) Gaits** v0.0 | **Flaps** | **Pitch** | **MP** | **RPM** | **IAS (`=this.speed-units`)** |
| -------------------------------- |:---------:|:---------:|:------:|:-------:|:-----------------------------:|
| ⚠️ V<sub>G</sub>                 |           |           |        |  idle   |           (Vg::80)            |
| 🛫 V<sub>R</sub>                 |           |           |        |   max   |           (Vr::80)            |
| V<sub>X</sub>                    |           |           |        |   max   |           (Vx::76)            |
| 🛫 V<sub>Y</sub>                 |           |           |        |   max   |           (Vy::90)            |
| 🛫 V<sub>Climb</sub>             |           |           |        |   max   |              100              |
| Cruise                           |           |           |        |         |                               |
| Cruise Descent                   |           |           |        |         |                               |
| 🌫️ IAF Inbound Level             |           |           |        |         |                               |
| 🌫️ IAF Inbound Descent           |           |           |        |         |                               |
| 🌫️ Prec Appr to DA               |           |           |        |         |                               |
| 🌫️ Non-Prec Appr to MDA          |           |           |        |         |                               |
| 🛬 Downwind                      |           |           |        |         |                               |
| 🛬 Abeam Numbers                 |           |           |        |         |                               |
| 🛬 Base                          |           |           |        |         |                               |
| 🛬 Final                         |    40°    |           |        | as req  |          (Vref::95)           |
| Short                            |           |           |        |         |         (Vshort::79)          |

<br>

| Topic          | Details                                                                                                   |
| -------------- |:--------------------------------------------------------------------------------------------------------- |
| Leaning        | TBD                                                                                                       |
| V<sub>A</sub>  | (Va-mgw::134) @ [mgw::3600]; 104 @ 2225 lb                                                                |
| Short T.O.     | (short-takeoff-flaps::25°) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{66, 71}@`=this.mgw`lb; {58, 61}@2600lb |
| Fuel Burn Est. | 16.0 GPH                                                                                                  | 
| Magnetos       | max 175 RPM, diff 50 RPM                                                                                  |
