# Key Takeaways
- Holds are used in various areas of IFR flying
- Standard holds are left turns with 1 minute (green needle) or 4 nm (DME/GPS)
- Hold entries are either teardrop, parallel, or direct

# Details
## Theory
1. Why Holds?
	1. Traffic or weather
	2. Keep aircraft in specified airspace awaiting clearance
	3. For course reversal: [[HILPT]]
2. Types of fixes:
	1. VOR, intersection, VOR/DME, GPS waypoint
	2. Published vs unpublished
	3. Using an [[EFB]]
3. Protected Area
4. Hold Geometry
	1. Standard Turns = Right!
	2. Leg length can be time-based or distance-based
		1. By default, holds are time-based
			1. If time is not specified, standard inbound leg is 1min below 14,000', 1.5min above. 
		2. Some holds are distance based, and require DME/GPS
			1. Example: [KSPZ RNAV RWY 24](https://cfijack.com/latest-plate-redirect/?plate=09917r24.PDF)
			2. Distance is measured diagonally. (extra info from IFR-Magazine)
	3. Turns: Standard Rate (3° per second)
5. Maximum airspeeds in protected airspace (slow to speed 3 min from hold)
	1. MHA-6,000’: 200kts
	2. 6,001’-14,000’: 230kts
	3. 14,001’+: 265kts
	4. Or as depicted/given by ATC

## Hold Entries
1. Types
	1. Direct (turn to outbound heading)
	2. Parallel (first turn direction is OPPOSITE of hold turns, fly for 1min, turn back to intercept inbound)
		1. VOR vs GPS turning to outbound
	3. Teardrop (turn with 30° offset from outbound leg)
2. Tips for determining hold entry
	1. Method 1: Cover top right/left with thumb, depending on right/left turns 
		1. If outbound leg in that 70° section, **teardrop**.
		2. Below the thumb and for the next 180°, **direct**.
		3. Opposite side from the inbound heading for 110°, **parallel**
	2. Method 2: Use right/left hand, depending on turn direction, and rotate to wrist to outbound heading
		1. If it's "painful" (wrist rotating to outside of body), **teardrop**^[Tears for the pain 😢]
		2. If not painful (wrist rotating toward body), **parallel**
		3. For anything beyond 70° of teardrop and 110° of parallel, **direct**
	3. Method 3: No-Math Hold Entry / Visualize the approach
		1. [[TLAR]] method, and not amusing to a [[DPE]]
		2. > [!quote] *Holding Entry* from [[IFR Magazine]], Feb 2025
> 1. If your heading to the holding fix takes you across the fix and outside the hold, that is a parallel. You would turn as appropriate, to parallel the inbound course for one minute before turning back towards the hold to the holding fix, again, per the [[AIM]].
> 2. If your heading takes you across the holding fix and then into the hold, that is a teardrop entry. Crossing the holding fix, proceed as per the [[AIM]].
> 3. If your heading is taking you directly to the fix or navaid that makes up the hold, and you are able to simply, directly make the correct turn entering the hold, then that is a direct entry.
	1. Method 4: 'Draw' the entry on the heading indicator
		1. 'Draw' inbound leg from radial to center of aircraft on [[HI]], so the holding fix is where the airplane is.
		2. Then build out rest of hold.
	2. Method 5: Draw the entry in a notebook
		1. Generally too slow to do in flight
	3. Method 6: [[MFD]] or [[EFB]] plotting
		1. Learn to program them efficiently to provide a backup on one of the above
3. ![[Dinner Plate Holds Practice]]

## Flying the Hold
1. Workload Management
	1. [[5 Ts]]: Time, Turn, Twist, Throttle, Talk 
2. Crosswind correction during pattern
	1. Determine cross-wind correction on inbound leg, and TRIPLE it on outbound leg ([[AIM 5]]-3-8)
	2. ![[Example Hold Wind Correction.jpeg]]^[Shows an initial direct entry without knowledge of the winds. While flying on the outbound heading, the student realized they had been blown outside the protected area and made a heading change to allow a turn inbound. The next two laps were learning the inbound and outbound headings.]

## Clearances
> [!tip] See [[Sample Holding Clearances]] for some examples

> [!quote] From [[AIM 5]]-3
> 1. Direction of holding from the fix in terms of the eight cardinal compass points (i.e., N, NE, E, SE, etc.).
> 2. Holding fix (the fix may be omitted if included at the beginning of the transmission as the clearance limit).
> 3. Radial, course, bearing, airway or route on which the aircraft is to hold.
> 4. Leg length in miles if [[DME]] or [[RNAV]] is to be used (leg length will be specified in minutes on pilot request or if the controller considers it necessary).
> 5. Direction of turn if left turns are to be made, the pilot requests, or the controller considers it necessary.
> 6. Time to expect further clearance ([[EFC]]) and any pertinent additional delay information.

What if you reach a clearance limit without holding instruction?^[E.g. On the [O69 VOR 29](https://cfijack.com/latest-plate-redirect/?plate=06838V29.PDF) missed.]
> [!quote] From [[AIM 5]]-3
> If the holding pattern is charted and the controller doesn't issue complete holding instructions, the pilot is expected to hold as depicted on the appropriate chart. 
> ...
> If no holding pattern is charted and holding instructions have not been issued, the pilot should ask ATC for holding instructions prior to reaching the fix. This procedure will eliminate the possibility of an aircraft entering a holding pattern other than that desired by ATC. If unable to obtain holding instructions prior to reaching the fix (due to frequency congestion, stuck microphone, etc.), then enter a standard pattern on the course on which the aircraft approached the fix and request further clearance as soon as possible.

#### Logging
1. Required to be logged for [[6 HITS]]
2. > [!quote] [[AIM 5]]-4-9, on [[HILPT]]
   > The holding pattern maneuver is completed when the aircraft is established on the inbound course after executing the appropriate entry.

# Additional Resources
- [[AIM 5]]-3-8
- [On Instruments: Flying in Place](https://www.aopa.org/news-and-media/all-news/2020/september/pilot/on-instruments-holding-patterns) from [[AOPA]]
- [Aircraft Holding Procedures, Explained](https://www.boldmethod.com/learn-to-fly/maneuvers/what-you-should-know-about-holding-for-ifr-pilots/) from [[Bold Method]]
- [Practice problems](https://cdn.shopify.com/s/files/1/0556/5101/files/Holding.pdf?1141) from thebackseatpilot.com
- [Pilot's Cafe Trainer App](https://www.pilotscafe.com/hold-trainer/)

#concept