---
cssclass: maneuver
tags: [maneuver, ppl]
altitude-limits: 1000' AGL
acs:
  ppl: 
    section: "V.B"
    standards: "<font color=\"red\">Altitude ±100, airspeed ±10</font>"
  cpl: 
    section: "NA"
    standards: "NA"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- Altitude `= this.altitude-limits`
- Power - `= this.config.aircraft.Va-dual-rpm` (`= this.config.aircraft.Va-dual`kts)
- Select suitable reference, perpendicular to wind
- Enter downwind
- Tailwind: Steeper bank
- Headwind: Shallower bank
- Use 5 points on S-turn to help maintain correct 1/2mi radius
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- Divide attention between airplane control, traffic, and ground references.
- Be aware of low altitude hazards like wires.
![[S-Turns.jpeg]]

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
