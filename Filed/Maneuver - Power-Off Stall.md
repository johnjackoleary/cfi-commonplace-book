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
- Power - IDLE; Hold altitude; Slow to `= this.config.aircraft.Vref`kts w/ flaps as for landing
- Descend power-off at `= this.config.aircraft.Vref`kts
- Pitch up slowly for full stall; Verbally acknowledge stall horn
- `= choice(this.config.cert = "ppl", "Continue pitch up to full stall", "Recover at first indication")`
- Recover: pitch down, full power, raise flaps one notch, then incrementally up. Climb Vy (`= this.config.aircraft.Vy`kts)
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- Use rudder to maintain coordinated flight (ball in center); poor coordination causes wing to drop during stall, entering spin
- In recovery, level wings primarily with rudder, ailerons also as airspeed increases
- Avoid secondary stall due to aggressive pitch up during recovery