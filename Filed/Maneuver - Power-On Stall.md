---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: \>3000' AGL
acs:
  ppl: 
    section: "VII.C"
    standards: "<font color=\"red\">Heading ±10°, or bank (<20°) ±10°</font>"
  cpl: 
    section: "VII.C"
    standards: "<font color=\"red\">Heading ±10°, or bank (<20°) ±10°</font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.config.aircraft.slow-flight-power`; Hold altitude; Slow to Vx (`= this.config.aircraft.Vx`kts)
- Add >65% power (`= this.config.aircraft.power-on-stall-power`)
- Pitch up slowly for stall; Verbally acknowledge stall horn
- `= choice(this.config.cert = "ppl", "Continue pitch up to full stall", "Recover at first indication")`
- Recover: pitch down, full power. Climb Vy (`= this.config.aircraft.Vy`kts)
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- Use rudder to maintain coordinated flight (ball in center); poor coordination causes wing to drop during stall, entering spin
- Avoid secondary stall due to aggressive pitch up during recovery