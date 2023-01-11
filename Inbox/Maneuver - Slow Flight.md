---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: \>3000' AGL
acs:
  ppl: 
    section: "VII.A"
    standards: "<font color=\"red\">Altitude ±100 feet; heading ±10°; airspeed +10/-0kts; bank ±10° - without a stall warning</font>"
  cpl: 
    section: "VII.A"
    standards: "<font color=\"red\">Altitude ±50 feet; heading ±10°; airspeed +5/-0kts; bank ±5° - without a stall warning</font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.config.aircraft.slow-flight-power`; Hold altitude; Add power < Vy (`= this.aircraft-datasheet.vy`kt)
- Slow to stall horn, then +5kts
- Power as needed to hold altitude
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- Extend gear and flaps at appropriate speeds (if applicable)
- Accomplish coordinated straight-and-level flight, turns, climbs, and descents with the aircraft configured as specified by the evaluator.
