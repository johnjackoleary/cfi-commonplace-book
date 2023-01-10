---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: \>3000' AGL
acs:
  ppl: 
    section: "VII.B"
    standards: "<font color=\"red\">Heading ±10°, or bank (<20°) ±10°</font>"
  cpl: 
    section: "VII.B"
    standards: "<font color=\"red\">Heading ±10°, or bank (<20°) ±5°</font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.config.aircraft.slow-flight-power`; Hold altitude; Slow to `= this.config.aircraft.Vref`kts w/ flaps as for landing
- Descend power-off at `= this.config.aircraft.Vref`kts
- Pitch up slowly for full stall
- Verbally acknowledge stall horn
- Continue pitch up for stall break
- Recover: pitch down, full power, flaps `= this.config.aircraft.flaps-on-stall-recover`, then up. Climb Vy
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- Verbally acknowledge the cues at the first indication of a stall.
- Recover, accelerate to Vy, then return to heading/altitude/airspeed.