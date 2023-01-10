---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: \>3000' AGL
ppl-acs: 
  section: "VII.A"
  standards: "<font color=\"red\">Altitude ±100 feet; heading ±10°; airspeed +10/-0kts; bank ±10° - without a stall warning</font>"
cpl-acs: 
  section: "VII.A"
  standards: "<font color=\"red\">Altitude ±50 feet; heading ±10°; airspeed +5/-0kts; bank ±5° - without a stall warning</font>"
aircraft-datasheet-source: "[[Maneuver Set-Up]]"
---
### Overview For `= this.aircraft-datasheet-source.aircraft-datasheet.model`
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.aircraft-datasheet.slow-flight-power`; Hold altitude; Add power < Vy (`= this.aircraft-datasheet.vy`kt)
- Slow to stall horn, then +5kts
- Power as needed to hold altitude
- PPL: `= this.ppl-acs.standards`
- CPL: `= this.cpl-acs.standards`

### Additional Details
- Extend gear and flaps at appropriate speeds (if applicable)
- Accomplish coordinated straight-and-level flight, turns, climbs, and descents with the aircraft configured as specified by the evaluator.