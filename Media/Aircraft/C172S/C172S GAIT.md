---
tags: [gait]
data: "[[C172S Datasheet]]"
---

| **C172S Gaits** v1.2          |            **Flaps**             | **Pitch** |              **RPM**              |            **IAS (kts)**            | **VSI (fpm)** |
| ------------------------------ |:--------------------------------:|:---------:|:---------------------------------:|:-----------------------------------:|:-------------:|
| ⚠️ V<sub>G</sub>               |                                  |    TBD    |               idle                |          `= this.data.Vg`           |      TBD      |
| 🛫 V<sub>R</sub>               |                                  |    TBD    |                max                |                 55                  |      TBD      |
| V<sub>X</sub>                  |                                  |    TBD    |                max                |          `= this.data.Vx`           |      TBD      |
| 🛫 V<sub>Y</sub>               |                                  |   +10°    |                max                |          `= this.data.vy`           |     +600      |
| 🛫 V<sub>Climb</sub>           |                                  |    +5°    |                max                |                 90                  |     +500      |
| Cruise                         |                                  |    0°     |               2500                |                 105                 |       0       |
| Cruise Descent                 |                                  |  \-2.5°   |               2500                |                 115                 |     \-500     |
| **🛬 Pattern**                 |                                  |           |                                   |                                     |               |
| Downwind                       |                                  |    TBD    | `=this.data.pattern-downwind-rpm` | `=this.data.pattern-downwind-speed` |       0       |
| Abeam Numbers                  | `=this.data.pattern-abeam-flaps` |    TBD    |  `=this.data.pattern-abeam-rpm`   |  `=this.data.pattern-abeam-speed`   |      TBD      |
| Base                           | `=this.data.pattern-base-flaps`  |    TBD    |   `=this.data.pattern-base-rpm`   |   `=this.data.pattern-base-speed`   |      TBD      |
| Final                          | `=this.data.pattern-final-flaps` |    TBD    |  `=this.data.pattern-final-rpm`   |         `= this.data.vref`          |      TBD      |
| **🌫️ IAP - Precision and CDFA** |                                  |           |                                   |                                     |               |
| ↘ Clean                        |                                  |   \-1°    |               1800                |                 90                  |     \-500     |
| ↘ Configured                   |               10°                |   \-3°    |               1900                |                 90                  |     \-500     |
| **🌫️ IAP - Step-Down**        |                                  |           |                                   |                                     |               |
| ↓ Dive - Clean                 |                                  |   \-2°    |               1700                |                 90                  |     \-800     |
| ➡ Drive - Clean                |                                  |    +2°    |               2200                |                 90                  |       0       |
| ↓ Dive - Configured            |               10°                |   \-4°    |               1500                |                 90                  |     \-800     |
| ➡ Drive - Configured           |               10°                |    +1°    |               2300                |                 90                  |       0       |

<br>

| Topic         | Details                                                    |
| ------------- |:---------------------------------------------------------- |
| Leaning       | 50° ROP when above 3000'                                   |
| V<sub>A</sub> | `= this.data.Va-mgw` @ max; 98@2200lb; 90@1900lb |
| Short T.O.    | (short-takeoff-flaps::10°) Flaps, {*Rotate*, *50ft*}@*weight*:<br>{51,56}@`=this.data.mgw`lb; {48,54}@2400lb; {44,50}@2200lb                                   |
| Short Ldg   |   (short-landing-flaps::30°) Flaps, 61kts@`=this.data.mgw`lb                                                                                                                                            |

