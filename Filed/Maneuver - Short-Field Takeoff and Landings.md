---
cssclasses:
  - maneuver
tags:
  - maneuver
  - ppl
  - cpl
altitude-limits: 
acs:
  ppl:
    section: ""
    standards: <font color="red">Land w/in 200' of specified point; parallel, cntrlin, nose up, no drift</font>
  cpl:
    section: ""
    standards: <font color="red"></font>
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- Takeoff:
	- Use full rwy length, flap `= this.config.aircraft.short-takeoff-flaps`
	- Hold brakes, add full power
	- Check gauges, release brakes
	- Climb `= this.config.aircraft.Vx-short`kts to agreed obst hgt
	- After obstacle, accel to Vy, flaps up
- Landing:
	- ID touchdown target
	- Approach `= this.config.aircraft.Vshort`kts (+gust factor)
	- Aiming point 100-200 feet short
	- Touchdown at or beyond target
	- Lower nose, apply brakes & aerodynamic braking, raise flaps
	- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
#### Takeoff
1. Set flaps according to POH/AFM
2. Position flight controls for existing wind conditions
3. Taxi into takeoff position using maximum available runway length, and align on runway centerline
4. Apply brakes and hold while applying takeoff power, check gauges
5. Release brakes, accelerate with POH recommended pitch technique, rotate at recommended [[IAS]], and accelerate to and climb at Vx
6. Retract gear/flaps after positive rate of climb, and in accordance with POH/AFM
7. Maintain Vx until obstacle is cleared (or 50' AGL), then accelerate to Vy

#### Landing
1. Complete pre-landing checklist ([[GUMPS]])
2. Establish POH-recommended approach configuration and airspeed, adjust pitch and power as required
3. Maintain stabilized approach and recommended airspeed (not more than 1.3Vso), applying gust factor (add half of gust difference) +10/-5 kts
4. Touch down smoothly, with minimal float, at or within 200 feet beyond the specified touchdown point
5. Apply brakes as necessary to stop in the shortest distance consistent with safety, using proper control deflections for existing wind conditions

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
