---
aliases:
  - Surveillance Systems
  - Primary Radar
  - Secondary Radar
  - Primary Surveillance Radar
  - Secondary Surveillance Radar
  - PSR
  - SSR
---

# Key Takeaways
- Either primary (radio wave "bounces back" off aircraft) or secondary (using [[transponder]]s) radar
- Primary radar has several limitations, which secondary (and later, [[ADS-B]]) has helped address
- Either Airport Surveillance Radar ([[ASR]]) or Air Route Surveillance Radar ([[ARSR]])

> [!note] 
> See [[Weather Radar]] for information on this specific radar application

# Details
## Overview
| Problem                       | Solution                                                                                              | Technology Name                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Can't see aircraft visually   | Reflect radio energy pulses off metal objects to get distance and direction^[similar to echolocation] | [[#Primary Radar]]                                            |
| Unsure who the aircraft is    | Install [[transponder]] which listens for *interrogation* and sends a *response* to broadcaster       | [[#Secondary Radar/Radar Beacon ( ATCRBS )\|Secondary Radar]] |
| Unsure aircraft's altitude    | Transponders additionally responds with pressure altitude                                             | [[#Modes\|Mode C]]                                            |
| Want more aircraft info       | Transponders additionally responds with significantly more information                                | [[#Mode S]]                                                   |
| Radar limitations frustrating | Use satellites for position and have all aircraft broadcast their own location and data                            | [[#ADS-B]]                                                              |

## Primary Radar
> [!quote] From [[Pilot-Controller Glossary]]
> A radar system in which a minute portion of a radio pulse transmitted from a site is reflected by an object and then received back at that site for processing and display at an air traffic control facility.

> [!example] By <a href="https://commons.wikimedia.org/wiki/File:Radaroperation.gif">The original uploader was Averse at German Wikipedia.</a>, <a href="https://creativecommons.org/licenses/by-sa/2.0/de/deed.en">CC BY-SA 2.0 DE</a>, via Wikimedia Commons
> <img src="https://upload.wikimedia.org/wikipedia/commons/c/c6/Radaroperation.gif"></img>

### Limitations
Normally travels in a straight line, but can be bent^[e.g. by [[temperature inversion]]], reflected or attenuated^[e.g. by ground obstacles, precipitation, or heavy clouds], or screened^[by high terrain features].

Historically, screening has been dealt with by installing several radars in strategic locations, but now [[ADS-B]] provides a surveillance solution in areas with challenging terrain.

> [!caution]- Wind turbines are a radar problem for non-transponder, non-ADS-B Out aircraft
> ![[Figure 4-5-2 Wind Turbine Farm Area of Potential Interference.png]]
> From [[AIM 4]], Figure 4-5-2

Finally, tracking primary targets is significantly more workload on [[ATC]].

## Secondary Radar/Radar Beacon ([[ATCRBS]])
> [!quote] From [[Pilot-Controller Glossary]]
> A radar system in which the object to be detected is fitted with cooperative equipment in the form of a radio receiver/transmitter ([[transponder]]). Radar pulses transmitted from the searching transmitter/receiver ([[interrogator]]) site are received in the cooperative equipment and used to trigger a distinctive transmission from the transponder. This reply transmission, rather than a reflected signal, is then received back at the transmitter/receiver site for processing and display at an air traffic control facility.


### Components
- **Interrogator**: Scans (in synchronism with the primary radar) and transmits discrete radio signals which repetitiously request all transponders, on the mode being used, to reply.
- **Transponder**: Receives the signals from the interrogator and selectively^[only to those interrogations received on the mode to which it is set] replies. These replies are independent of, and much stronger than, a primary radar return.
- **Radarscope**: Used by controllers to view returns from both primary and secondary radar. Returns are called **targets**.

### Modes
| Mode   | Purpose                                              |
| ------ | ---------------------------------------------------- |
| Mode A | Identification (Squawk code)                         |
| Mode C | Identification (Squawk code) + [[Pressure Altitude]] | 

### Mode S
Intended to eventually replace [[ATCRBS]], as it allows for individual aircraft interrogation (instead of all aircraft in the radar beam responding).

Fully backwards compatible with Modes A or C.

## [[ADS-B]]
> [!quote] From [Ins and Outs](https://www.faa.gov/air_traffic/technology/equipadsb/capabilities/ins_outs) by [[FAA]]
> ADS-B replaces radar technology with satellites, bringing major advantages. Radar relies on radio signals and antennas to determine an aircraft's location. ADS-B uses satellite signals to track aircraft movements.

**Useful Terms**
- **ADS-B Out**: *transmission* of ADS-B information from an aircraft
- **ADS-B In**: *receipt* of ADS-B information by an aircraft
- **ADS-B Ground Stations**: smaller and more adaptable than radar towers and can be placed in locations not possible with radar



### ADS-B Out

> [!info] From [Getting to Know Your ADS-B System](https://www.faa.gov/air_traffic/technology/equipadsb/installation/know_adsb_system) by the [[FAA]]
> There are approximately 19 pieces of information that your ADS-B is required to transmit through the entire operation

> [!attention] ADS-B Out is required in all airspaces defined in [[FAR 91.225 ADS-B Use]]
> ![[ADS-B and Mode C Requirements.jpg]]

### ADS-B In
Aircraft equipped with ADS-B In can receive the following 3 useful services directly in the flight deck

#### 1) Traffic Information Services – Broadcast ([[TIS-B]])
Provides ADS-B Out/In equipped aircraft with surveillance information about aircraft that are not ADS-B equipped^[target must have a transponder and be within radar coverage, though]
![[TIS-B Overview.png]]

#### 2) Automatic Dependent Surveillance ‐ Rebroadcast ([[ADS-R]])
Relays ADS-B information transmitted by an aircraft broadcasting on one link (UAT or 1090ES) to aircraft equipped with ADS-B In on the other link.

> [!example]
> The information for an aircraft equipped with a 1090MHz ADS-B Out system will be re-broadcasted to an aircraft equipped with ADS-B In on the UAT (i.e. 978MHz) frequency, and vice versa.

![[ADS-R Overview.png]]

#### 3) Flight Information Services – Broadcast ([[FIS-B]])
Provides the meteorological and aeronautical data to the cockpit, broadcast on UAT frequency^[not on 1090MHz]

![[FIS-B Overview.png]]

Some of the currently available FIS-B products are:

- Airmen's Meteorological Information ([[AIRMET]])
- Significant Meteorological Information ([[SIGMET]])
- [[Convective SIGMET]]
- [[METAR]]
- CONUS [[NEXRAD]]
- Regional NEXRAD
- [[NOTAM]]
- [[PIREP]]
- Special Use Airspace (SUA) Status
- Terminal Aerodrome Forecast ([[TAF]])
- Winds & Temperatures Aloft
- [[TIS-B]] Service Status

> [!warning]
> In flight weather information will have a delay and can not be used for tactical navigation. See [[NEXRAD]]

# Additional Resources
- [[AIM 4]]-5
- [Ins and Outs](https://www.faa.gov/air_traffic/technology/equipadsb/capabilities/ins_outs) by [[FAA]]
- [[AC 90-114]]

***Definition***    :: A system that uses electromagnetic waves to identify the range, altitude, direction, or speed of both moving and fixed objects such as aircraft, weather formations, and terrain.
***Additional Info:*** The term RADAR was coined in 1941 as an acronym for Radio Detection and Ranging. The term has since entered the English language as a standard word, radar, losing the capitalization in the process.
***Source***         :: [[PHAK Glossary]]
***Meaning*** :: <u>Ra</u>dio <u>D</u>etection <u>A</u>nd <u>R</u>anging

#acronym #glossary #concept