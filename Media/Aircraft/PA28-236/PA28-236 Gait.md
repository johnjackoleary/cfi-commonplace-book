---
tags:
  - gait
has-carb-heat: true
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

| **(model::PA28-236) Gaits** v0.1 | **Flaps** | **MP** | **RPM** | **IAS (`=this.speed-units`)** |
| -------------------------------- |:---------:| ------ |:-------:|:-----------------------------:|
| ⚠️ V<sub>G</sub>                 |           |        |  idle   |            (Vg::)             |
| 🛫 V<sub>R</sub>                 |           | max    |   max   |           (Vr::60)            |
| V<sub>X</sub>                    |           | max    |   max   |           (Vx::73)            |
| 🛫 V<sub>Y</sub>                 |           | max    |   max   |           (Vy::85)            |
| 🛫 V<sub>Climb</sub>             |           | max    |   max   |              100              |
| Cruise                           |           |        |  2200   |                               |
| Cruise Descent                   |           | 16"    |         |            110-120            |
| 🛬 Downwind                      |           | 16"    |         |                               |
| 🛬 Abeam Numbers                 |           | 13"    |         |                               |
| 🛬 Base                          |           |        |         |                               |
| 🛬 Final                         |    40°    |        |         |          (Vref::72)           |
| Short                            |    40°    |        |         |          (Vshort::72-59)           |

<br>

| Topic          | Details                                                                                   |
| -------------- |:----------------------------------------------------------------------------------------- |
| Leaning        | 150F ROP EGT                                                                                       |
| V<sub>A</sub>  | (Va-mgw::124)kts @ [mgw::3000]lb; 96kts @ 1761lb                                          |
| Short T.O.     | (short-takeoff-flaps::25°) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{59, 63}@`=this.mgw`lb; {48,52}@2000lb |
| Fuel Burn Est. | 14 gph @ 75% power                                                                                         |

<br>

Specific tips for N3038B are [available here](https://docs.google.com/document/d/1TckLuBS34hkWiAkEOl1KFzfXaApoDq8JF07a0z7psXs/edit#heading=h.g2wja4d55w93).