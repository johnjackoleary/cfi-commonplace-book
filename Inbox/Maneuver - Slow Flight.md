---
tags: [maneuver]
altitude-limits: \>3000' AGL
cpl-acs: 
  section: "VII.A"
  standards: "altitude, ±50 feet; heading, ±10°; airspeed, +5/-0kts; bank, ±5° - without a stall warning"
aircraft-datasheet: "[[C172S Datasheet]]"
---
## Summary
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.aircraft-datasheet.slow-flight-power`
- Hold altitude; Add power < Vy
- Slow to stall horn, then +5 knots
- Power as needed to hold altitude

## Details
### Set-Up
Altitude: `= this.altitude-limits`
![[Maneuver Set-Up]]
### Execution
1. Reduce power, maintaining altitude while aircraft slows down, extend gear and flaps at appropriate speeds (if applicable)
2. 
### Success
- Accomplish coordinated straight-and-level flight, turns, climbs, and descents with the aircraft configured as specified by the evaluator.
- Maintain the specified **`= this.cpl-acs.standards`**.
#todo :: Figure out how to differentiate CPL from PPL criteria