# Key Takeaways
- [[FAR 91.185 Lost Comms|91.185]] defines the process to follow if you loss comms
	- In VMC, continue the flight under VFR and land as soon as practicable
	- In IMC, use [[AVE-F]], [[MEA (Lost Comms)|MEA]], and know when to leave your [[clearance limit]]
- It's helpful to think separately about the regulatory expectations and the reality of any given situation
- ***Be predictable!*** 

# Details
## Basic Flow
1. [[Squawk 7600]]
2. Debug the comms problem
	1. Try both radios (Com1, Com2)
	2. Try left and right headsets, which are each triggered by their own PTT switch
	3. Are headset plugs securely inserted?
	4. Do you see 'TX' on transmit? If not, you may have a stuck mic, or a bad PTT switch
	5. Consider calling [[TRACON]] or Center on your cell phone!
	6. Consider using a backup handheld radio
3. In [[VMC]], continue VFR, land as soon as practicable. 
4. In [[IMC]]: 
	1. For Route, use mnemonic [[AVE-F|AVE-F]] – Assigned, Vectored, Expected, then Filed (in that order of priority) 
	2. For Altitude **on each route segment**, use highest of mnemonic [[MEA (Lost Comms)]] – Minimum IFR altitude, Expected, Assigned 
	3. Leave [[Clearance Limit]]^[See also [[How Far Can You Go]]]
		1. When at fix from which approach begins, leave at EFC time if given, otherwise commence descent as close as possible to ETA
		2. When not at a fix from which approach begins, leave clearance limit at the EFC time if received and proceed to a fix from which an approach begins; commence descent or descent and approach as close as possible to the ETA. Otherwise upon arrival over the clearance limit, proceed to a fix from which an approach begins; commence descent or descent and approach as close as possible to the ETA

> [!summary]- Overview Image
> ![[IFR Radio Comm Part 2 Two-Way Radio Failure.jpeg]]

## Expanded Procedures
### Choosing a Route
We select a route using the items of [[AVE-F]], in that priority order.

1. **Assigned**: If ATC gave you a [[CRAFT]] clearance, or updated your clearance en route, this is your assigned route
2. **Vectored**: If ATC gave you a heading to fly, continue flying it until you intercept back on your route
3. **Expected**: If ATC gave you an expected next instruction, follow that instruction
4. **Filed**: If none of the other options are available, fly the route you filed^[In practice, it would be impossible or nearly impossible to end up using Filed]

[[SID]]s often also include instructions for lost comms, which should be briefed before departure and followed as applicable.

> [!example]-
> ATC gave us a CRAFT clearance including the route *[PYE V25 PRB](https://skyvector.com/?ll=37.846168006955345,-122.7672930730165&chart=403&zoom=3&fpl=%20O69%20PYE%20V25%20PRB%20KPRB)*. While crossing PYE, we are instructed: "fly heading 130 vectors for traffic". Shortly after, we lose our radio.
> 
> Since we are not currently on an **assigned** route, we go to the next priority. We are being **vectored**, so we'll continue following that vector until it intercepts our original course.^[What if the vector did not have us on an intercept path? Be predictable, and make your way to a reasonable place to pick up the route.] Somewhere around SFO, we are back on an **assigned** route, and thus will prioritize following that route.

> [!example]-
> On a flight from KSAC to KPAO, ATC cleared us for [SAC V6 OA](https://skyvector.com/?ll=37.78591078047763,-121.86227417205406&chart=302&zoom=2&fpl=%20KSAC%20SAC%20V6%20OAK%20BUSHY%20DOCAL%20KPAO)K. While on V6, ATC instructs: "cleared direct BUSHY, expect DOCAL after."^[They may not be able to clear us for the full route initially] Then, we lose our radio.
> 
> Direct BUSHY is our **assigned** route, so the first segment is easy. Reaching BUSHY, we do not have an **assigned** or **vectored** route, so we go to the next highest priority of **expected** and turn direct to DOCAL.

### Choosing an Altitude
After selecting our route, we select an altitude, ***per segment***, from whichever is the highest of [[MEA (Lost Comms)|MEA]].

- **Minimum Altitude** for IFR: on airways is the [[MEA]], and off airways is 1000' or 2000' over obstacles, depending on the region
- **Expected**: what we were told to expect, and it applies only after the time we were given
- **Assigned**: whatever we were told to climb or descend to by ATC in our last clearance

> [!tip] Finding Minimum Altitudes Off Airway
> When off the airway, the minimum altitude for IFR is 1000' over terrain in non-mountainous areas and 2000' over terrain in mountainous areas.^[[[FAR 91.177 Minimum Altitudes for IFR]]] 
> 
> 1. One way to estimate this altitude is look at your VFR chart for the segment, find the highest obstacle on the route, and add 1000' or 2000' (depending on where you are).
> 2. Another simple approach is using Profile view in ForeFlight with the two-finger pinch ([[ForeFlight Highest Point.jpeg|image]]) to determine the highest obstacle on a route.
> 3. The [[MSA]] for an approach is another reasonable option, once you're close enough.
> 4. The [[OROCA]], though tempting, is rarely a good option in mountainous areas because it can be significantly higher than required.^[Consider [V338 between LIN and HNW](https://skyvector.com/?ll=38.3522110786003,-120.93159485079757&chart=302&zoom=2&fpl=%20KSCK%20LIN%20V338%20HNW%20KPVF). The MEA is 5200, while the OROCA is 12700!]

> [!example]- On Airways Example
> Flying from KAST to KALW, we are "Cleared to [KALW via AST3 departure, AST V112 PDT direct](https://skyvector.com/?ll=45.94121877629587,-120.8292846701371&chart=302&zoom=6&fpl=%20KAST%20AST%20V112%20PDT%20KALW), climb and maintain 3000', expect 5000' 5 minutes after departure." Almost immediately after takeoff, we lose our radio.
> 
> We are currently on the [[ODP]] from KAST ([AST3.AST](https://cfijack.com/latest-plate-redirect/?plate=00024ASTORIA.PDF)), which does not have specific lost comms procedures.
> 
> 1. The first segment is completing the ODP. 
> 	1. Assuming less then 5 minutes since departure, MEA on this climbout gives **Minimum Altitude** of 2000' on ODP, **Expected** not yet applicable, and **Assigned** of 3000'. 
> 	2. 3000' is the highest of the three, so we'll climb to 3000'.
> 2. The second segment is AST to PITER. 
> 	1. Suppose we reach AST at 4 minutes since departure, then **M** is 5000' for the V112 MEA, **E** is not applicable, and **A** is 3000'. 5000' is the highest, so we'll start to climb to 5000' after crossing AST.
> 	2. While on this second segment, still en route to PITER, we reach 5 minutes after departure. Now **M** is 5000', **E** is 5000', and **A** is 3000'. 5000' is still highest, so maintain 5000'.
> 3. The third segment is PITER to BTG. 
> 	1. M is 4400', E is 5000', and A is 3000'. 5000' is still highest, so we'll stay there.
> 	2. Notice the [[MCA]] at BTG. If we had been at 4400' (maybe if our original clearance didn't have an expected climb), we would need to climb before BTG to cross as 5000'. Normally, we'd start to climb after crossing.
> 4. BTG to LTJ: M is 7000', E is 5000', A is 3000'. So after crossing BTG, climb to 7000'.
> 5. LTJ to LOAMS: M is 5400', E is 5000', A is 3000'. So after crossing LTJ, descend to 5400'.
> 6. LOAMS to PDT: M is 4100', E is 5000', A is 3000'. So after crossing LOAMS, descend to 5000'.
> 7. PDT to KALW: M is 4100' on V536, E is 5000', A is 3000'. Maintain 5000' until reaching our [[clearance limit]].

> [!example]- Off Airways Example
> Flying from KPAO to KJAQ, we are "Cleared to [KJAQ via 31 ODP, SJC V334 SUNOL LIN direct](https://skyvector.com/?ll=37.92036783985792,-121.45454406952925&chart=302&zoom=2&fpl=%20KPAO%20SJC%20V334%20SUNOL%20LIN%20KJAQ), climb and maintain 3000', expect 4000' 5 minutes after departure." Just after crossing SJC, about 3 minutes after departure, we lose our radio.
> 
> 1. The first segment is SJC to SUNOL. 
> 	1. It is a victor airway, V334 with an MEA of 5000'. We have not yet hit 5 minutes for our expected time.
> 	2. **Minimum Altitude** is 5000', **Expected** is not yet applicable, and **Assigned** is 3000'. 
> 	3. 5000' is the highest of the three, so we climb to 5000'.
> 2. Along V334, before reaching SUNOL, we hit 5 minutes after departure
> 	1. **M** is still 5000', **E** is now applicable at 4000', and **A** is 3000'.
> 	2. We are already at the highest of these three, 5000', so no altitude change is needed.
> 3. Next segment is SUNOL to LIN
> 	1. The [[MCA]] does not apply since we're not on V301 SE bound
> 	2. This is an off-airway route in a [[Designated Mountainous Areas|mountainous areas]], so [[FAR 91.177 Minimum Altitudes for IFR|91.177]] requires 2000' clearance above the highest obstacle.
> 	3. Let's look at four options for finding height (although in practice, almost always use 1 or 2):
> 		1. Scanning the [[Sectional Highest Point.jpeg|obstacle/terrain height on a sectional]], we see windfarms up to 1970' and terrain colored to 2000'. 2000' is a reasonable highest obstacle, so a minimum altitude of 4000'.
> 		2. Using ForeFlight, we get a more precise [[ForeFlight Highest Point.jpeg|highest obstacle in the 4nm corridor]] or [[ForeFlight Highest on Route.jpeg|highest terrain/obstacle on a route leg]] of 2411'. This gives a minimum altitude of ~4500'.
> 		3. We're too far from the destination to use an MSA.
> 		4. The [[OROCA]] near SUNOL is 6600', then 4900' near LIN. We could plausibly use this, but usually avoid it for reasons we'll see shortly.
> 	4. In this case, let's use the ForeFlight minimum altitude of ~2500'+2000' = 4500'.
> 	5. **M** is 4500', **E** is 4000', and **A** is 3000'. Crossing SUNOL, we'll descend to 4500'.
> 4. Last, LIN to KJAQ
> 	1. ForeFlight gives us the highest terrain of ~2300'.
> 	2. M is 4300', E is 4000', A is 3000'. We descend to 4300'.
^KPAO-to-KJAQ

### Leaving Your Clearance Limit
Once you've reached your [[clearance limit]], the next step depends on three questions:
1. Is the clearance limit a fix from which an approach begins (an [[IAF]])?
2. Did you receive an [[EFC]] time?
3. Are you noticeably ahead of your filed or amended ETA?

**In the vast majority of cases**, the answer to all three questions is no. Usually your clearance limit is the airport (not an IAF), you will not have an EFC time, and you will not be ahead of time.

Therefore, in the vast majority of cases,
> [!quote] From [[FAR 91.185 Lost Comms]]
> \[L\]eave the clearance limit... upon arrival over the clearance limit, and proceed to a fix from which an approach begins and commence descent or descent and approach....

Said more plainly, you will typically leave your clearance limit right after you arrive there, and head to any [[IAF]]. Once you reach the IAF, you will descend^[perhaps in a holding pattern or a spiral] to an altitude to start the approach, then begin the approach.

> [!example]- Cleared to an airport, on schedule, no EFC
> Continuing the example from [[#^KPAO-to-KJAQ|KPAO to KJAQ above]], we've just reached KJAQ at 4300'. KJAQ is not an [[IAF]], we do not have an [[EFC]], and we are on time.
> 
> We next choose our preferred approach.^[This may be difficult without a radio to get the local weather.] We'll use the [KJAQ GPS 1](https://cfijack.com/latest-plate-redirect/?plate=09086G1.PDF).
> 
> After reaching KJAQ, we turn back to either [[IAF]]. HOYCO is closer and has an easier intercept angle, so we'll turn towards HOYCO still at 4300'.
> 
> After reaching HOYCO, we'll start a descent to the initial segment altitude of 4000' and begin the approach.

For all other cases, it's helpful to use a flowchart. Feel free to carry a physical or digital one to reference if you ever need it!
> [!summary] Leave Clearance Limit Flowchart
> ![[IFR Radio Comm Part 2 Two-Way Radio Failure.jpeg]]


> [!example]- Cleared to an [[IAF]], on schedule, no EFC
> On our way to KSCK, 5nm east of OXJEF, ATC gives us the clearance: "cleared direct OXJEF, maintain 3000', expect the [RNAV 29R](https://cfijack.com/latest-plate-redirect/?plate=00407R29R.PDF)". Then our radio fails.
> 
> We have an **assigned** route, direct, to our [[clearance limit]] of OXJEF.
> 
> This approach is a [[TAA]], so we have those altitudes for Minimum Altitude. We do not have an expected altitude, but we've been assigned 3000'. We're 5nm east of OXJEF, so M is 2000', E is N/A, and A is 3000'. We'll hold 3000'.
> 
> Reaching OXJEF, we are not yet at our ETA (since we didn't fly all the way to the airport). We'll enter the published hold at 3000'.^[See [[Holding Procedures]] for how to hold when not given a holding clearance. If there's a published hold, we prefer that.] We'll start the descent and approach as close as possible to our ETA.

## Additional Examples
> [!youtube] [Lost Communications Procedures | FAR 91.185](https://www.youtube.com/watch?v=RNVh1QtHrQs) is a great practical example from [[FlightInsight]]
> ![](https://www.youtube.com/watch?v=RNVh1QtHrQs)

> [!example]
> Several complete examples can be found in [[Lost Communication Procedure Practice]] from [[EAA]]

## Reality of Lost Comms
There is a lot of debate about lost comms in a real flight. If it's an emergency, [[FAR 91.3 PIC Responsibility and Authority|91.3]] gives the pilot the authority to deviate from the rules to get down safely.

Many pilots would consider losing radio contact in IMC an emergency. The AIM also groups it under the emergency procedures ([[AIM 6]]). However, the FAA has been less committed in their answer.

> [!caution]
> If you use your [[FAR 91.3 PIC Responsibility and Authority|91.3]] authority to deviate from [[FAR 91.185 Lost Comms|91.185]], **do so in a predictable way** so ATC can accommodate. For example, if an [[IAP]] is along the route, you could decide to hold over the IAP for several minutes to allow ATC to clear traffic away, then start your approach (instead of flying to your clearance limit).

> [!tip] On your checkride
> The [[DPE]] is a representative of the FAA, and on the checkride they are looking for a deep understanding and ability to apply [[FAR 91.185 Lost Comms|91.185]]. 
> 
> The correct answer, on a checkride, is what the regulation says -- it is better to avoid discussing [[FAR 91.3 PIC Responsibility and Authority|91.3]] unless the DPE brings it up.
> 
> See [[Scott Rohlfing's Advice on Lost Comms]] for a good discussion on this.

# Additional Resources
- [[AIM 6]]-4
- [Lost Communications Procedures | FAR 91.185](https://www.youtube.com/watch?v=RNVh1QtHrQs) - a really good practical example from [[FlightInsight]]
- [[Lost Communication Procedure Practice]]
- Video of [Real Lost Comms in IMC](https://pilotworkshop.com/lost-comm-imc-video/)
- [[IFR Radio Comm Part 1 General.jpeg]] and [[IFR Radio Comm Part 2 Two-Way Radio Failure.jpeg]]
- [[FAR 91.185 Lost Comms]]
- [[Turri 2011]], [[Van West 2018]]
- [Handling A Radio Failure In IMC](https://www.boldmethod.com/learn-to-fly/regulations/handling-a-radio-failure-in-imc/) from [[Bold Method]]

#concept
