---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: 
acs:
  ppl: 
    section: ""
    standards: "<font color=\"red\"></font>"
  cpl: 
    section: ""
    standards: "<font color=\"red\"></font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- **A:** `= this.altitude-limits`; **P:** `=this.config.aircraft.maneuver-rpm` RPM; **A:** `=this.config.aircraft.maneuver-speed` `=this.config.aircraft.speed-units`
- 
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
