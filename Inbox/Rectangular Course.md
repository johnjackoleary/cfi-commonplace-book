---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: 600'-1000' AGL
acs:
  ppl: 
    section: 
    standards: "<font color=\"red\"></font>"
  cpl: 
    section: ""
    standards: "<font color=\"red\"></font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- 
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
