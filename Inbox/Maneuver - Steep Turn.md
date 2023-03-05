---
cssclass: maneuver
tags: [maneuver, ppl, cpl]
altitude-limits: ≥3000' AGL
acs:
  ppl:
    bank: 45°
    section: "V.A"
    standards: "<font color=\"red\">±100ft, ±10kts, bank ±5°, heading ±10°</font>"
  cpl: 
    bank: 50°
    section: "V.A"
    standards: "<font color=\"red\">±100ft, ±10kts, bank ±5°, heading ±10°</font>"
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- `= [[Maneuver Set-Up]].content`
- **A:** `= this.altitude-limits`; **P:** `=this.config.aircraft.maneuver-rpm` RPM; **A:** `=this.config.aircraft.maneuver-kias`kts
- Crisp roll into `=choice(this.config.cert="ppl", this.acs.ppl.bank, this.acs.cpl.bank)` bank; add power; aft pressure for altitude
- `=choice(this.config.cert="ppl", "Rollout on entry heading", "Repeat 360° in other direction")`
- `=choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
- May notice (subtle) opposite aileron during turn to prevent over-banking tendency
- There's a lot of debate on if you should or shouldn't use trim. I suggest not, but you may want to.

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
