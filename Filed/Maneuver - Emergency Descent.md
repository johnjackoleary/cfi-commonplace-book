---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: \>3000' AGL
acs:
  ppl: 
    section: "IX.A"
    standards: "<font color=\"red\">Bank 30°-45° w/ positive load factor</font>"
  cpl: 
    section: ""
    standards: "<font color=\"red\"></font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Simulate engine fire flow (touch each control)
- Start descent (bank 30°-45°; airspeed >=`= this.config.aircraft.engine-fire-speed` `=this.config.aircraft.speed-units`)
- Execute forced landing
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
