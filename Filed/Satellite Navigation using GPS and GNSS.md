# Key Takeaways
> [!quote] From [Navigation Programs — Satellite Navigation](https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gnss) by [[FAA]]
> - The [[FAA]] is transforming the [[NAS]] to Performance Based Navigation ([[PBN]]) to address the shortfalls of conventional [[Ground-Based Navigation using VOR, DME, and ILS|ground-based navigation]].
> - PBN allows aircraft to fly flexible point-to-point routes and parallel tracks to reduce en-route chokepoints and delays.
> - [[GPS]], [[WAAS]], and [[RAIM]]^[Technically this is any Aircraft Based Augmentation Systems (ABAS), but RAIM is the most well known.] are referred to collectively as Global Navigation Satellite System ([[GNSS]])

# Details

1. Infrastructure and Features
	1. [[GNSS]]
		1. [[GPS]] Constellation
			1. 31 Satellite, ~11,000 miles above sfc of earth, each orbit earth 2x per 24 hours
			2. Minimum of 24 satellites is required in full constellation
		2. Calculating position
			1. Calculates distance between satellites and receivers via atomic clock
	2. [[RAIM]] + Satellites Required
		1. Receiver Autonomous Integrity Monitoring
		2. 4 Satellites for 3D
		3. RAIM requires 5 satellites or 4 + barometric altimeter input
		4. FDE (Fault Detection + Exclusion) 
			1. Excludes a failed satellite from the position solution; GPS receivers capable of FDE require 6 satellites or 5 satellites with baro-aiding
	4. [[WAAS]] (TSO-145,TSO-146)
		1. Wide Area Augmentation System
		2. Uses reference stations with known locations to determine GPS error for a wide area
		3. Error info sent to WA Master Station, then uplinked to Geosynchronous Satellite that broadcasts to WAAS receivers
2. VFR Waypoints: Named as *VPxxx* and can be used to aid in GPS navigation^[A lot more information is available at [VFR Waypoint Chart Program](https://www.faa.gov/air_traffic/publications/atpubs/foa_html/chap12_section_8.html)]

## GPS
### How GPS Works
https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gnss/gps/howitworks

### Using an Aircraft's GPS
1. Preflight
2. Using and entering flight plans

> [!tip] Many GPS devices have simulators you can use to practice at home. For instance, for the [GNC 355 simulator](https://www.garmin.com/en-US/p/685256) from Garmin.

### Using and Interpreting [[CDI]]
- Distance from route (in nm), unlike angular displacement from [[VOR]]

### Common Issues
#todo :: add to this

## WAAS
### How WAAS Works
#todo :: add to this
https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gnss/waas/howitworks

## RAIM
#todo :: add info on [[RAIM]]

### Common Issues
Well, not so common, is a WAAS outage: https://www.nstb.tc.faa.gov/

E.g. ![[WAAS LPV.png]]

# Additional Resources
- [[PHAK Ch16]]
- https://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/navservices/gnss
- https://download.aopa.org/epilot/2007/sa01.pdf "GPS Technology" #safety-advisors

***Related To***: [[Ground-Based Navigation using VOR, DME, and ILS]]

#concept