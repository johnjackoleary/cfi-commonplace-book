---
tags: [maneuver]
altitude-limits: \>3000' AGL
ppl-acs: 
  section: "VII.A"
  standards: "<font color=\"red\">Altitude ±100 feet; heading ±10°; airspeed +10/-0kts; bank ±10° - without a stall warning</font>"
cpl-acs: 
  section: "VII.A"
  standards: "<font color=\"red\">Altitude ±50 feet; heading ±10°; airspeed +5/-0kts; bank ±5° - without a stall warning</font>"
aircraft-datasheet: "[[C172S Datasheet]]"
---
### Overview
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.aircraft-datasheet.slow-flight-power`; Hold altitude; Add power < Vy
- Slow to stall horn, then +5 knots
- Power as needed to hold altitude
- `= this.cpl-acs.standards`

### Additional Details
- Extend gear and flaps at appropriate speeds (if applicable)
- Accomplish coordinated straight-and-level flight, turns, climbs, and descents with the aircraft configured as specified by the evaluator.

#todo :: Figure out how to differentiate CPL from PPL criteria