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
    standards: <font color="red">Min. sink, parallel, cntrlin, nose up, no drift; elevtr back thru exit</font>
  cpl:
    section: ""
    standards: <font color="red"></font>
config: "[[Maneuvers Config]]"
---
### Overview For `= this.config.aircraft.model` (`= upper(this.config.cert)`)
- Takeoff:
	- Taxi w/o stop, yoke back, `= this.config.aircraft.soft-takeoff-flaps` flap
	- Liftoff early; accl in ground effect
	- At Vx or Vy, start climb; flaps up
- Landing:
	- Approach `= this.config.aircraft.Vref`kts (+gust factor)
	- Smooth roundout & flare
	- Add power if needed for soft ldg
	- Nose high, minimal braking
	- `= choice(this.config.cert = "ppl", this.acs.ppl.standards, this.acs.cpl.standards)`

### Additional Details
#### Takeoff
1. Set flaps according to POH/AFM
2. Position flight controls for existing wind conditions
3. Elevator aft for light nose wheel
4. Taxi into takeoff position without stopping, with smooth power application for takeoff
5. Establish pitch attitude to rapidly transfer weight from wheels to wings
6. Lift off at lowest possible airspeed, accelerate to [[Vx]] or [[Vy]] in [[Ground Effect]]
7. Establish pitch attitude and airspeed for [[Vx]] or [[Vy]] climb
8. Retract gear/flaps after positive rate of climb, and in accordance with POH/AFM

#### Landing
1. Complete pre-landing checklist ([[GUMPS]])
2. Establish POH-recommended approach and landing configuration (flaps) and airspeed
3. Maintain stabilized approach and recommended airspeed (not more than 1.3Vso), applying [[Gust Factor]] (add half of gust difference) +10/-5 knots
4. Make smooth roundout and flare, with minimum sink rate. Use power as necessary to cushion descent and touchdown
5. Maintain full up elevator during rollout, and exit the runway without stopping and safe taxi speed, using proper control deflections for existing wind conditions

### Related Notes
```dataview
LIST WHERE contains(this.file.inlinks, file.link)
```
