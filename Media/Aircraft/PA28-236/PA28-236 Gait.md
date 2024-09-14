---
tags:
  - gait
has-carb-heat: true
Vs: 
Vs0: 
soft-takeoff-flaps: 25°
cool-procedure: 
engine-fire-speed: 
power-on-stall-rpm: 
maneuver-rpm: 
maneuver-speed: 
speed-units: kts
---

| **(model::PA28-236) Gaits** v2.0 | **Flaps** | **MP** | **RPM** | **IAS (`=this.speed-units`)** |
| -------------------------------- |:---------:|:------:|:-------:|:-----------------------------:|
| ⚠️ V<sub>G</sub>                 |           |        |  idle   |           (Vg::85)            |
| 🛫 V<sub>R</sub>                 |           |  max   |   max   |           (Vr::60)            |
| V<sub>X</sub>                    |           |  max   |   max   |           (Vx::73)            |
| 🛫 V<sub>Y</sub>                 |           |  max   |   max   |           (Vy::85)            |
| 🛫 V<sub>Climb</sub>             |           |  max   |   max   |              100              |
| Cruise                           |           |  23"   |  2200   |              120              |
| Cruise Descent                   |           |  16"   |  2200   |            110-120            |
| 🌫️ IAF Inbound Level             |           |        |         |                               |
| 🌫️ IAF Inbound Descent           |           |        |         |                               |
| 🌫️ Prec Appr to DA               |    10°    |  13"   |   max   |              90               |
| 🌫️ Non-Prec Appr to MDA          |    10°    |        |         |                               |
| 🛬 Downwind                      |    10°    |  16"   |   max   |              90               |
| 🛬 Abeam Numbers                 |    10°    |  13"   |   max   |              90               |
| 🛬 Base                          |    25°    |  13"   |   max   |              80               |
| 🛬 Final                         |    25°-40°    | as req |   max   |          (Vref::72)           |
| Short                            |    40°    |  as req      |   max   |        (Vshort::59-72)        |

<br>

| Topic          | Details                                                                                   |
| -------------- |:----------------------------------------------------------------------------------------- |
| Leaning        | Peak EGT for economy cruise                                                                                       |
| V<sub>A</sub>  | (Va-mgw::124)kts @ [mgw::3000]lb; 96kts @ 1761lb                                          |
| Short T.O.     | (short-takeoff-flaps::25°) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{59, 63}@`=this.mgw`lb; {48,52}@2000lb |
| Fuel Burn Est. | 15 gph @ 75% power economy cruise                                                                                        |
