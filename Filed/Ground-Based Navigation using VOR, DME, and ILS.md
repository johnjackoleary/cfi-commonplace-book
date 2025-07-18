# Key Takeaways
> [!quote] Paraphrased from [Navigation Programs](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices) by [[FAA]]
> - Based primarily on [[VOR]], [[DME]], and [[ILS]]
> - Intended as a resilient [[PBN]] backup to [[Satellite Navigation using GPS and GNSS]]

![[GBNA.jpeg]]

# Details
## VOR
### Introduction
1. Azimuth Information ('radial')
2. Types of VOR
	1. [[VOR]]
	2. [[VOR]]/[[DME]]
	3. [[VORTAC]]
5. Charts 
6. Limitations (line of sight, service volume)
	1. Service Volumes (New vs. Original) - T, L, H, VL, VH
7. Identifying
8. Distance with 10° Full Scale Deflection ([[60-to-1 Rule]])
9. Calculating 180° off bearing for VOR radial
	1. Look at where the 'tail' of the CDI is pointing
	2. +/- 200°, then -/+ 20° (e.g. 345-200 => 145 + 20 => 165)

### How VOR Works
VOR receivers detect the phase difference between a reference and variable signal. They use this difference to determine the radial an aircraft is on.^[VOR navigation technology uses a ground-based antenna at a station to send a directional signal that rotates clockwise 30 times a second, or 360 degrees in azimuth. A reference signal is also emitted timed to be in phase with the directional signal as the directional signal passes magnetic north. The "phase difference" between the reference signal and the directional signal is the bearing from the station to the aircraft position. This bearing or line of position is called the VOR radial.]

> [!tip] Some people like the [[Lighthouse Analogy for VOR]]


![[Reference vs Variable Signal Graphic]]

### Using VOR
> [!tip]
> It can be helpful to practice using a [[VOR]] in a simulator beforehand. Consider [Fergo IFR Simulator](https://www.fergonez.net/projects/ifrsimulator/) or your favorite.

1. VOR, OBS, CDI, To/From indicator, [[HSI]], tuning, identification, and receiver check (logged in last 30 days) 
	1. Always tune and identify!
		1. > [!quote] From [[AIM 1]]-1-1c
		> Some VOR equipment decodes the identifier and displays it to the pilot for verification to charts, while other equipment simply displays the expected identifier from a database.... If your equipment automatically decodes the identifier, it is not necessary to listen to the audio identification.
	2. Can help to [[Think of VOR Radials as Two Not To]]
2. Determining relative location
	1. Where are you relative to the station? (Center CDI with FROM) 
	2. Where are you relative to assigned course? (Point your heading parallel to the course; set OBS to course; CDI needle points toward the course) 
	3. Where are you relative to intersection defined by VOR radial? (Set OBS to radial, confirm FROM, if CDI needle deflected toward station, you’re not there yet. For HSI, CDI needle ahead, you’re not there yet.)
3. VOR intercepts 
	1. Use 40° intercept heading if CDI fully deflected. 
	2. Use 20° intercept if CDI is alive
4. VOR course tracking 
	1. Wind correction angle – start with 20°s, at intercept, reduce to 10°s, keep reducing or increasing by half until it works. 
	2. Once tracking, use small heading adjustments (few degrees^[Consider at most the width of the heading bug.]) to maintain course
5. Flying direct to
	1. Rotate OBS until CDI centers and 'to', then turn to that heading
	2. Track course inbound to station
6. Station passage

#### VOR Holds
See [[IR.8 Holding Patterns and Entries]]

### Regulations and Requirements
#### VOR Checks
[[FAR 91.171 VOR Check|FAR 91.171]] requires a VOR check be performed within the preceding 30 days.

| Method            | Max Error |
| ----------------- | --------- |
| VOT               | 4°        |
| Ground Checkpoint | 4°        |
| Dual              | 4°        |
| Airborne          | 6°        |

This check must be recorded with the date, place, bearing error, and your signature.

#### [[VOR]] [[MON]]
> [!quote] [Navigation Programs - Very High Frequency Omnidirectional Range Minimum Operational Network (VOR MON)](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gbng/vormon)
> The VOR MON is designed to enable aircraft, having lost GPS service, to revert to conventional navigation procedures. This will allow users to continue through the outage area using VOR station-to-station navigation or to proceed to a MON airport where an Instrument Landing System (ILS), Localizer (LOC) or VOR approach procedure can be flown without the necessity of GPS, Distance Measuring Equipment (DME), Automatic Direction Finder (ADF), or surveillance. 
> Any airport with a suitable instrument approach may be used for landing, but the VOR MON assures that at least one airport will be within 100 Nautical Miles (NM).

### Common Issues
> [!warning] 
> [[VHF]] transmissions require line-of-sight

## DME
An aircraft sends interrogation pulses to a [[DME]] ground station, then the ground station transmits paired pulses back to the aircraft at same spacing but different frequency. The time required to receive a response is used to determine [[slant range]] distance to the ground station.

>[!warning] DME uses [[slant range]] distance.

### Identifying DME
1. Transmitted on 1350Hz
2. The DME can still work if [[VOR]] inoperative

### DME Arcs Procedure
1. "Turn 10, Twist 10"
2. Interception: Lead 90 heading perpendicular to the arc/radial by ~1 nm
3. On the arc: Every new 10 radial, turn 10° and twist OBS 10°
	1. If inside/outside arc: heading turn may be slightly more or less than 10°
4. Note how quickly the needle swings, and lead turn appropriately
	1. Should lead by ~1nm
	2. Consider (60 / DME distance) = degrees deflection to lead by
5. Alternatively, consider using a bearing pointer and keeping it pointed at 90° to your heading^[Although remember, you'll still need to account for wind]

## ILS
1. Localizer  (Lateral)
	1. 108.1-111.95 odd tenths
	2. Course width varies, 700ft wide over threshold, 5° width, 2.5° full scale deflection
	3. 90Hz Left side, 150Hz Right side
	4. 10° either side of course along radius of 18nm of antenna, 10-35° either side of course along radius of 10nm
2. Glideslope  (Vertical)
	1. Straight, sloped line guidance from FAF to TDZ
	2. Housed 750-1,250ft down runway from approach end, between 400-600 ft to one side of the centerline
	3. Like localizer on its side
	4. 2.5° to 3.5° slope Intercept [[OM]] 1,400 ft above runway, [[MM]] 200ft above runway
	5. False Glideslopes
3. Outer Marker (Distance)
	1. Can be subbed by compass locator, PAR, ASR, DME, VOR, NDB, [[RNAV]] in conjunction with a fix
	2. Identifies the Final Approach Fix ([[FAF]]) for nonprecision approach


## Less Common Navaids
### NDB and ADF
There are few examples of [[NDB]] use in navigation in modern aviation, but it can be helpful to understand them as a stepping stone in the evolution from [[Teach With Context - Pilotage, Dead Reckoning, NDB and VOR|pilotage and dead reckoning, to NDB, to VOR]].

If your airplane has a working [[ADF]], you can tune to a nearby AM radio station and try it out!^[Although be aware, there's no guarantee it'll direct you to the station. They may be using a backup transmitter elsewhere!] For more on how to use an [[ADF]], check out [[Rod Machado]]'s article [here](https://rodmachado.com/blogs/learning-to-fly/adf-navigation-the-basics).

### Marker Beacon Receiver/Indicators
1. Tells you how far along an approach or airway you are
2. rated power of 3 watts or less 
3. produces elliptical pattern with dimensions, at 1,000 feet above the antenna, of approximately 2,400 feet in width and 4,200 feet in length

# Additional Resources
- [[PHAK Ch16]]
- [[AIM 1]]
- Videos on using VOR: https://www.youtube.com/watch?v=RTxW1VB_Qog and https://www.youtube.com/watch?v=_j0dLlRwpvk
- Sim to practice with VOR: https://www.fergonez.net/projects/ifrsimulator/
- [[FAA]] article on [Navigation Programs - Ground-Based Navigation](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gbng)

***Related To***: [[Satellite Navigation using GPS and GNSS]]

#concept