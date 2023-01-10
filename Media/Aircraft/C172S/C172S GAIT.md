---
tags: [gait]
---

| **C172S Gaits** v0.3    | **Flaps** | **Pitch** | **RPM** |       **IAS (kts)**        | **VSI (fpm)** |
| ----------------------- |:---------:|:---------:|:-------:|:--------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>        |           |    TBD    |  idle   |             68             |      TBD      |
| 🛫 V<sub>R</sub>        |    10°    |    TBD    |   max   |             55             |      TBD      |
| V<sub>X(10°)</sub>      |    10°    |    TBD    |   max   |             56             |      TBD      |
| V<sub>X</sub>           |           |    TBD    |   max   |             62             |      TBD      |
| 🛫 V<sub>Y</sub>        |           |   +10°    |   max   | `= [[C172S Datasheet]].vy` |     +600      |
| 🛫 V<sub>Climb</sub>    |           |    +5°    |   max   |             90             |     +500      |
| Cruise                  |           |    0°     |  2500   |            105             |       0       |
| Cruise Descent          |           |  \-2.5°   |  2500   |            115             |     \-500     |
| 🌫️ IAF Inbound Level    |           |    +2°    |  2200   |             90             |       0       |
| 🌫️ IAF Inbound Descent  |           |   \-2°    |  1700   |             90             |     \-800     |
| 🌫️ Prec Appr to DA      |    10°    |   \-3°    |  1900   |             90             |     \-450     |
| 🌫️ Non-Prec Appr to MDA |    10°    |   \-4°    |  1500   |             90             |     \-800     |
| 🛬 Downwind             |           |    TBD    |  2000   |             90             |       0       |
| 🛬 Abeam Numbers        |    10°    |    TBD    |  1500   |             80             |      TBD      |
| 🛬 Base                 |    20°    |    TBD    |  1500   |             70             |      TBD      |
| 🛬 Final                |    30°    |    TBD    |  1500   |             `= [[C172S Datasheet]].vref`             |      TBD      |
| Short                   |    30°    |    TBD    |  1500   |             `= [[C172S Datasheet]].vshort`             |      TBD      |

| Topic              | Details                                   |
| ------------------ |:----------------------------------------- |
| Leaning            | 50° ROP when above 3000'                  | 
| V<sub>A</sub>      | 105 @ max<br>98 @ 2200 lb<br>90 @ 1900 lb |