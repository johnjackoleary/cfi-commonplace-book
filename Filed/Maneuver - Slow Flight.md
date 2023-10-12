---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: ≥3000' AGL
acs:
  ppl: 
    section: "VII.A"
    airspeed: 10
    standards: "<font color=\"red\">Altitude ±100 feet; heading ±10°; airspeed +`=this.acs.ppl.airspeed`/-0kts; bank ±10°; no stall warning</font>"
  cpl: 
    section: "VII.A"
    airspeed: 5
    standards: "<font color=\"red\">Altitude ±50 feet; heading ±10°; airspeed +5/-0kts; bank ±5°; no stall warning</font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- **A:** `= this.altitude-limits`; **P:** Any; **A:** Any
- Power `= this.config.aircraft.pattern-base-rpm`rpm; hold altitude; add power approaching specified speed, then as needed to hold alt
- If slowing to stall horn, find it and fly  +`=choice(this.config.cert = "ppl", this.acs.ppl.airspeed, this.acs.cpl.airspeed)/2`kts
- `=choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- Extend gear and flaps at appropriate speeds (if applicable)
- Accomplish coordinated straight-and-level flight, turns, climbs, and descents with the aircraft configured as specified by the evaluator.

#todo :: Pull in notes from [[6. Maneuvering During Slow Flight]]