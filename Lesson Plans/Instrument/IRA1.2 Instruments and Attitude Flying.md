---
tags:
  - ir
  - lesson
aliases:
- IR.2
---
### Introduction
Instrument flying, at its core, is attitude flying. Without visual references outside the cockpit, the instrument pilot must constantly refer to their instruments to be sure the airplane is maintaining the desired heading and altitude. This instrument scan is critical for attitude flying, as even a 5-second distraction can leave the plane in an undesired attitude. 

So, the instrument pilot must develop a habit of continuously scanning the instruments, while also multitasking to perform every other action required in flight. In this lesson, we'll review the instrument systems and pre-flight procedures you learned in [[PPL]] training, then we'll discuss several instrument scan techniques. The goal is for this scan to become second nature.

**Pre-Lesson Reading/Homework:** [[~ IR Pre-Lesson Reading]]
**Builds On:** [[IRA1.1 Introduction and Roadmap]]
**Resources:** Flight Deck Poster/Diagram ([Sporty's](https://www.sportys.com/cessna-172r-cockpit-poster.html) or from [[Rectangular Scan.jpeg|IFH]])
**Schedule:** Ground 1-2 hours, depending on recall from PPL; simulator and/or airplane, 0.5 hours 

> [!note] 
> Can often be completed at the same time as [[IRA1.1 Introduction and Roadmap]].

### 

### Lesson Elements
#### Aircraft Systems and Instruments
> [!question] 
> For each system and instrument, what are the relevant power sources, flight characteristics, limitations, errors, pre-flight check methods, etc? 

1. Required equipment for IFR flight, and IFR airworthiness requirements ([[FAR 91.205 Instrument and Equipment Requirements]])
	1. Mnemonic [[GRABCARDD]]
2. [[FAR 91.213 Inop Equip]]
3. Instruments
	1. Pitot-Static instruments: Altimeter (+/- 75’), Airspeed Indicator, Vertical Speed Indicator, pitot heat (use below 10C or 50F, in visible moisture) 
		1. Pitot Heat check during preflight
	2. Gyro instruments: Attitude indicator, Heading Indicator, Turn Coordinator, vacuum systems 
		1. [[DG]] precession limit - 3° in 15 minutes (industry suggestion)
		2. Horizontal Situation Indicator ([[HSI]])
	3. Magnetic [[Compass Errors]]: check freely turns during taxi check
	4. Electronic flight instrument display
		1. normally includes primary flight display ([[PFD]]) and multi-function display ([[MFD]]), sometimes on a single screen
		2. [[AHRS]] (Attitude and Heading Reference System) replaces conventional gyroscopic instrument
			1. AHRS uses Inertial Measurement Units (IMUs) to detect roll, pitch, and yaw. It corrects for drift over time using magnetometers (to find magnetic north) and accelerometers (to find “down” from Earth’s gravity).
			2. > [!warning] Synthetic vision can cause pitch scale change
		3. [[ADC]] does computations using pitot/static
	5. Flight management system ([[FMS]]) (AIM 1-2-1)
		1. Suite of sensors, receivers, and computers couples with navigation database
		2. Provide performance and RNAV guidance to displays and automation
		3. Inputs can be accepted from multiple sources - [[GPS]], [[DME]], [[VOR]], LOC
		4. Inputs may be applied to navigation solution one at a time or with any combination
	6. Multifunction display, if installed
		1. Used in conjunction with PFD
		2. Contains various additional information (maps, weather, engine performance, etc)
		3. Often can be used as a backup to PFD (e.g. [[reversionary mode]])
	7. Technically Advanced Aircraft ([[Technically Advanced Aircraft|TAA]]) definition
4. [[Transponder]] and altitude encoders
	1. Blind Encoder (cheaper, not integrated with altimeter) vs. Encoding Altimeter (transponder integrated with altimeter)
	2. Connected to static line
	3. Mode A (squawk code + position) vs Mode C (squawk code + position + altitude)
	4. OFF (no power), STBY (no interrogation responses), ON (responses in Mode A), ALT (responds in Mode C), GND
		1. Use ALT mode on the ground^[[[AIM 4]]-1-20]
	5. Mode S - transmits additional info like heading, speed
	6. Set to ALT ([[Lights, Camera, Action, Time]] check)
5. [[ADS-B]] weather/traffic
6. Radio: Look for [[TX]], [[RX]]
7. #G1000 specific topics: 
	1. [[AHRS]] vs [[ADC]] – what are they, what do you do if they fail?
	2. Electrical system – how do you know if the alternator has failed? 
		1. [[C172 G1000 Electrical System Interactive Tool]]
	3. If you are running on Standby battery – what still functions?
		1. [[PFD]], [[AHRS]], [[ADC]], Com1, Nav1, standby instrument lights, essentials bus
		2. (NOTHING ELSE, like flaps, transponder, lights, audio panel, etc) 
8. Power Instruments: Engine gauges, Electronic engine instruments
9. Electrical instruments: ammeter, voltmeter, alternator 
10. Navigation radios and databases 
	1. Covered in depth as part of [[IRA1.5 Ground-Based Navigation]] and [[IRA1.6 Satellite Navigation]]
11. [[Autopilot Systems and Usage]]

#### Attitude Instrument Flight
1. Fundamentals of instrument flight, in order: <u>C</u>ross check, <u>I</u>nstrument interpretation, <u>A</u>ircraft control ([[CIA]] as a memory aid)
2. Control/Performance ([[IFH]] Ch6)
	1.  Pitch + Power = Performance
	2. Control Instruments depict immediate attitude and power changes
		1. Attitude Indicator
		2. Turn Coordinator
		3. Tachometer and Manifold Pressure (set by sound, then verify)
	3. Performance Instruments reflect the performance the aircraft is achieving
		1. Airspeed
		2. Altimeter and [[VSI]]
		3. Heading
3. Introduction to Instrument Scan (ground portion) 
	1. Instrument cross check, types of scans 
	2. 4-step scan procedure to initiate any maneuver (*[4 Step Instrument Scan](https://www.aopa.org/news-and-media/all-news/2003/october/flight-training-magazine/4-step-instrument-scan)* from [[AOPA]])
		1. Set approximate attitude and power ([[Aircraft Gait Charts]])
		2. [[Inverted V-Scan]] to check trends 
		3. [[Music Scan]] primary instruments 
		4. [[Rectangular Scan]] all instruments 
	3. G1000 scan (pitch horizontal line, bank vertical line)
	4. Instrument interpretation
4. Common Errors: 
	1. [[Illusions Leading to Spatial Disorientation|Spatial disorientation]] 
	2. Distraction 
	3. Fixation or omission 
	4. Doing things while turning – should do nothing else 
	5. Heavy touch, over-controlling 
	6. Improper trim control

#### Airplane or Sim Activity
1. Attitude Instrument Flight Basics 
	1. Pitch-Power-Trim sequence for climb initiate and level off, Power-Pitch-Trim for descent initiate and level off
	2. Straight and Level flight ([[IFH]] 7-2)
	3. Straight climbs and descents ([[IFH]] 7-14)
	4. Turns ([[IFH]] 7-19)
2. Learn and make gait chart (see also [[Aircraft Gait Charts]])
	1. Make rows of table for Vx, Vy, cruise climb, cruise, cruise descent, slow cruise (holding, initial approach), slow descent (final approach)
	2. Make columns of table for pitch (# bars on A/I), Manifold Pressure, RPM, airspeed 
	3. Or use the [[Aircraft Blank Gait]]
	4. > [!tip] It's easiest to find these settings while using an autopilot
3. Use of [[Autopilot Systems and Usage|autopilot]]

### Required Homework
- [ ] Memorize the [[Aircraft Gait Charts|gait chart]] and/or have printed on kneeboard

### Completion Standards
Learner must demonstrate understanding of: control and performance instruments; instrument scan methods. Learner should become proficient in S&L flight by reference to instruments, and transitions to straight climbs, descents, and turns. (ACS standards: +/- 10 kts, +/- 10°s, +- 100 feet)

*Return to [[~ IR Lesson Plan Outline|Table of Contents]]^*