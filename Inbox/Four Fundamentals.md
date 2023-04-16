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

| | Timing | First | Then | Finally | Tune, then Trim |  
| -- | -- | -- | --| -- | -- |  
| Initiate Climb | | Pitch &#x21D1; | Power &#x21D1; (full) | wait until stable | tune, then trim |  
| Level Off Climb | lead by 10% of VSI | Pitch &#x21D2; | wait until cruise speed | Power &#x21BA; | tune, then trim |  
| Initiate Descent | | Power &#x21D3; | wait for natural Pitch &#x21D3; | wait until stable | tune, then trim |  
| Level Off Descent | lead by 10% of VSI | Power &#x21BA; | wait for natural Pitch &#x21D2; | wait until cruise speed | tune, then trim |


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
