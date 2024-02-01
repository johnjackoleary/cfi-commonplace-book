---
cssclasses:
  - lesson
tags:
  - ir
  - lesson
---
### Objective
Understand the infrastructure and instruments used for navigation, how each system works, and how to determine if the system is functional. Additionally, to understand the tools available for ice.

#todo :: split into [[IR.1 Introduction and Instrument Systems]] and [[IR.6 Intercepting and Tracking VOR, HSI, Autopilot Usage]] and [[IR.7 GPS Navigation and Autopilot Usage]]

### References
None


### Builds On
[[IR.1 Introduction and Instrument Systems]]

### Schedule
Ground 3 hours

### Lesson Elements
1. VHF omnirange (VOR)
	1. How it works
		1. 108.0 – 117.95 MHz
		2. Azimuth via Reference vs Variable Signal (Lighthouse analogy)
			1. [[Reference vs Variable Signal Graphic|Graphic]]
			2. VOR navigation technology uses a ground-based antenna at a station to send a directional signal that rotates clockwise 30 times a second, or 360 degrees in azimuth. A reference signal is also emitted timed to be in phase with the directional signal as the directional signal passes magnetic north. 
			3. The “phase difference” between the reference signal and the directional signal is the bearing from the station to the aircraft position. This bearing or line of position is called the VOR radial.
	3. [[VOR]] Types - T, L, H, VL, VH
	4. Limitations (line of sight, service volume)
	5. Identifying
	6. Distance with 10° Full Scale Deflection (60-to-1 rule)
2. Distance measuring equipment (DME)
	1. Pulses are sent from A/C, ground station transmits paired pulses back to the aircraft at same spacing but different frequency
	2. Time required for round trip of signal exchange is translated into slant range distance
	3. Identifying
		1. Transmitted on 1350Hz
		2. The DME can work if VOR inoperative
	4. VOR/DME, VORTAC, ILS/DME, LOC/DME
	5. #todo :: combine this with [[Satellite Navigation using GPS and GNSS]] and [[Ground-Based Navigation using VOR, DME, and ILS]]
3. Instrument landing system ([[ILS]]) (AIM 1-1-9)
	1. Localizer  (Lateral)
		1. 108.1-111.95 odd tenths
		2. Course width varies, 700ft wide over threshold, 5° width, 2.5° full scale deflection
		3. 90Hz Left side, 150Hz Right side
		4. 10° either side of course along radius of 18nm of antenna, 10-35° either side of course along radius of 10nm
	2. Glideslope  (Vertical)
		1. Straight, sloped line guidance from FAF to TDZ
		2. Housed 750-1,250ft down runway from approach end, between 400-600 ft to one side of the centerline
		3. Like localizer on its side
		4. 2.5° to 3.5° slope Intercept OM 1,400 ft above runway, MM 200ft above runway
	3. Outer Marker (Distance)
		1. Can be subbed by compass locator, PAR, ASR, DME, VOR, NDB, RNAV in conjunction with a fix
		2. Identifies the Final Approach Fix (FAF) for nonprecision approach
4. Marker beacon receiver/indicators
	1. Tells you how far along an approach or airway you are
	2. rated power of 3 watts or less 
	3. produces elliptical pattern with dimensions, at 1,000 feet above the antenna, of approximately 2,400 feet in width and 4,200 feet in length
5. Automatic direction finder ([[ADF]])
	1. Non-directional beacon ([[NDB]]) consists of two parts: ADF equipment on the aircraft that detects an NDB's signal, and the NDB transmitter
	2. ADF displays the relative bearing from the aircraft to an NDB (or suitable radio station)
	3. Determines bearing to NDB station using combo of directional and non-directional antennae to sense the strongest signal direction.
	4. (Relative Bearing to station + Magnetic Heading) mod 360 = Magnetic Bearing
6. Transponder/altitude encoding
	1. Blind Encoder (cheaper, no integrated with altimeter) vs. Encoding Altimeter (transponder integrated with altimeter)
	2. Connected to static line
	3. Mode A (squawk code + position) vs Mode C (squawk code + position + altitude)
	4. OFF (no power), STBY (no interrogation responses), ON (responses in Mode A), ALT (responds in Mode C)
	5. Set to ALT (Lights, Camera, Action, Time check)
7. Electronic flight instrument display
	1. normally includes primary flight display (PFD) and multi-function display (MFD), sometimes on a single screen
	2. AHRS (Attitude and Heading Reference System) replaces conventional gyroscopic instrument
		1. AHRS uses Inertial Measurement Units (IMUs) to detect roll, pitch, and yaw. It corrects for drift over time using magnetometers (to find magnetic north) and accelerometers (to find “down” from Earth’s gravity).
	3. ADC does computations using pitot/static
8. Flight management system (FMS) (AIM 1-2-1)
	1. Suite of sensors, receivers, and computers couples with navigation database
	2. Provide performance and RNAV guidance to displays and automation
	3. Inputs can be accepted from multiple sources - GPS, DME, VOR, LOC
	4. Inputs may be applied to navigation solution one at a time or with any combination
9. Multifunction display, if installed
	1. Used in conjunction with PFD
	2. Contains various additional information (maps, weather, engine performance, etc)
	3. Often can be used as a backup to PFD (e.g. reversionary mode)


### Completion Standards
Student can explain the systems used in navigation, and the tools available for dealing with ice. 

### Required Logbook Phraseology
None

### Required Homework
- [ ] 

### Recommended Homework
- [ ] 

*Return to [[~ IR Lesson Plan Outline|Table of Contents]]^*