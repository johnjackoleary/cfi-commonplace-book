---
tags: [gait]
has-carb-heat: true
---

| **(model::C152) Gaits** v0.0    | **Flaps** | **Pitch** |              **RPM**              |    **IAS (kts)**     | **VSI (fpm)** |
| ----------------------- |:---------:|:---------:|:---------------------------------:|:--------------------:|:-------------:|
| ⚠️ V<sub>G</sub>        |           |    TBD    |               idle                |          (Vg:: 60)          |      TBD      |
| 🛫 V<sub>R</sub>        |    10°    |    TBD    |                max                |          55          |      TBD      |
| V<sub>X(10°)</sub>      |    10°    |    TBD    |                max                |          56          |      TBD      |
| V<sub>X</sub>           |           |    TBD    |                max                |   `= this.data.Vx`   |      TBD      |
| 🛫 V<sub>Y</sub>        |           |   +10°    |                max                |   `= this.data.vy`   |     +600      |
| 🛫 V<sub>Climb</sub>    |           |    +5°    |                max                |          90          |     +500      |
| Cruise                  |           |    0°     |               2500                |         105          |       0       |
| Cruise Descent          |           |  \-2.5°   |               2500                |         115          |     \-500     |
| 🌫️ IAF Inbound Level    |           |    +2°    |               2200                |          90          |       0       |
| 🌫️ IAF Inbound Descent  |           |   \-2°    |               1700                |          90          |     \-800     |
| 🌫️ Prec Appr to DA      |    10°    |   \-3°    |               1900                |          90          |     \-450     |
| 🌫️ Non-Prec Appr to MDA |    10°    |   \-4°    |               1500                |          90          |     \-800     |
| 🛬 Downwind             |           |    TBD    | `=this.data.pattern-downwind-rpm` |          `=this.data.pattern-downwind-kias`          |       0       |
| 🛬 Abeam Numbers        |    `=this.data.pattern-abeam-flaps`    |    TBD    |               `=this.data.pattern-abeam-rpm`                |          `=this.data.pattern-abeam-kias`          |      TBD      |
| 🛬 Base                 |    `=this.data.pattern-base-flaps`    |    TBD    |               `=this.data.pattern-base-rpm`                |          `=this.data.pattern-base-kias`          |      TBD      |
| 🛬 Final                |    `=this.data.pattern-final-flaps`    |    TBD    |               `=this.data.pattern-final-rpm`                |  `= this.data.vref`  |      TBD      |
| Short                   |    30°    |    TBD    |               1500                | `= this.data.vshort` |      TBD      |

| Topic              | Details                                   |
| ------------------ |:----------------------------------------- |
| Leaning            | 50° ROP when above 3000'                  | 
| V<sub>A</sub>      | `= this.data.va-mgw` @ max<br>98 @ 2200 lb<br>90 @ 1900 lb |


### V Speeds (KIAS)
Vg :: 68
Vx :: 62
Vy :: 74
Va-mgw :: 105
Va-dual :: 100
Vref :: 65
Vshort :: 61

### Weights
mgw :: 2550

### Maneuvering
slow-flight-rpm :: 1600
Va-dual-rpm :: 2200
power-on-stall-rpm :: 2100
flaps-for-stall-recover :: 20°

### Emergency
engine-fire-speed :: 100

### Pattern Speeds
#todo :: Update [[C172S GAIT]] to use these formulas
pattern-downwind-kias :: 90
pattern-downwind-rpm :: 2000
pattern-abeam-kias :: 80
pattern-abeam-rpm :: 1600
pattern-abeam-flaps :: 10°
pattern-base-kias :: 70
pattern-base-rpm :: 1600
pattern-base-flaps :: 20°
pattern-final-kias :: 65
#todo :: Should I use vref instead?
pattern-final-rpm :: 1600
pattern-final-flaps :: 40°

cool-procedure :: N/A for C172SP