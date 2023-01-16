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
- Select suitable reference
- Enter 45° to the downwind leg, left or right traffic
- Aim for 1/4-1/2 mile from reference, account for wind
- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- This maneuver simulates flying the traffic pattern.
- Divide attention between airplane control, traffic, and ground references.
- Be aware of low altitude hazards like wires.
- Turn crosswind from downwind when you are abeam the crosswind reference line.
![[Rectangular Course.jpeg]]

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
