# Key Takeaways
> [!quote] Paraphrased from [Navigation Programs](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices) by [[FAA]]
> - Based primarily on [[VOR]], [[DME]], and [[ILS]]
> - Intended as a resilient [[PBN]] backup to [[Satellite Navigation using GPS and GNSS]]

![[GBNA.jpeg]]

# Details
## VOR
### Introduction
1. Azimuth Information
2. Types of VOR
	1. [[VOR]]
	2. [[VOR]]/[[DME]]
	3. [[VORTAC]]
4. Service Volumes (New vs. Original)
5. Charts 

### How VOR Works
VOR receivers detect the phase difference between a reference and variable signal. They use this difference to determine the radial an aircraft is on.

![[Reference vs Variable Signal Graphic]]

### Using VOR
> [!tip]
> It can be helpful to practice using a [[VOR]] in a simulator beforehand. Consider [Fergo IFR Simulator](https://www.fergonez.net/projects/ifrsimulator/) or your own favorite.

1. VOR, OBS, CDI, To/From indicator, HSI, tuning, identification, and receiver check (logged in last 30 days) 
	1. Always tune and identify!
2. Determining relative location
	1. Where are you relative to the station? (Center CDI with FROM) 
	2. Where are you relative to assigned course? (Parallel course, set OBS to course, CDI needle points toward the course) 
	3. Where are you relative to intersection defined by VOR radial? (Set OBS to radial, confirm FROM, if CDI needle deflected toward station, you’re not there yet. For HSI, CDI needle ahead, you’re not there yet.)
4. VOR intercepts 
	1. Use 45° intercept heading if CDI fully deflected. 
	2. Use 20° intercept if CDI is alive
5. VOR course tracking 
	1. Wind correction angle – start with 20°s, at intercept, reduce to 10°s, keep reducing or increasing by half until it works. 
	2. Once tracking, use small heading adjustments (few degrees^[Consider at most the width of the heading bug.]) to maintain course
6. Flying direct to
	1. Rotate OBS until CDI centers and 'to', then turn to that heading
	2. Track course inbound to station
7. Station passage

#### VOR Holds
#todo :: fill this out more, maybe including practice problems (like https://cdn.shopify.com/s/files/1/0556/5101/files/Holding.pdf?1141 from thebackseatpilot.com)

### Regulations and Requirements
#todo :: expand on this

#### [[VOR]] [[MON]]
> [!quote] [Navigation Programs - Very High Frequency Omnidirectional Range Minimum Operational Network (VOR MON)](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gbng/vormon)
> The VOR MON is designed to enable aircraft, having lost GPS service, to revert to conventional navigation procedures. This will allow users to continue through the outage area using VOR station-to-station navigation or to proceed to a MON airport where an Instrument Landing System (ILS), Localizer (LOC) or VOR approach procedure can be flown without the necessity of GPS, Distance Measuring Equipment (DME), Automatic Direction Finder (ADF), or surveillance. 
> Any airport with a suitable instrument approach may be used for landing, but the VOR MON assures that at least one airport will be within 100 Nautical Miles (NM).

### Common Issues
> [!warning] 
> [[VHF]] transmissions require line-of-sight

## DME
An aircraft sends a interrogation pulses to a [[DME]] ground station. The time required to receive a response is used to determine distance to the ground station.

>[!note] DME uses slant distance.

### DME Arcs Procedure
1. “Turn 10, Twist 10”
2. Interception: Lead 90 heading perpendicular to the arc/radial by ~1 nm
3. On the arc: Every new 10 radial, turn 10° and twist OBS 10°
	1. If inside/outside arc: heading turn may be slightly more or less than 10°
4. Note how quickly the needle swings, and lead turn appropriately
	1. Should lead by ~1nm
	2. Consider (60 / DME distance) = degrees deflection to lead by

## ILS
#todo :: add more info on [[ILS]]


## Less Common Navaids
### NDB and ADF
There are few examples of [[NDB]] use in navigation in modern aviation, but it can be helpful to understand them as a stepping stone in the evolution from [[Teach With Context - Pilotage, Dead Reckoning, NDB and VOR|pilotage and dead reckoning, to NDB, to VOR]].

If your airplane has a working [[ADF]], you can tune to a nearby AM radio station and try it out!^[Although be aware, there's no guarantee it'll direct you to the station. They may be using a backup transmitter elsewhere!] For more on how to use an [[ADF]], check out [[Rod Machado]]'s article [here](https://rodmachado.com/blogs/learning-to-fly/adf-navigation-the-basics).


# Additional Resources
- [[PHAK Ch16]]
- [[AIM 1]]
- Videos on using VOR: https://www.youtube.com/watch?v=RTxW1VB_Qog and https://www.youtube.com/watch?v=_j0dLlRwpvk
- [[FAA]] article on [Navigation Programs - Ground-Based Navigation](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gbng)

***Related To***: [[Satellite Navigation using GPS and GNSS]]

#concept