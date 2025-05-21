---
cssclasses:
  - lesson
tags:
  - ir
  - lesson
---
### Objective
Develop detailed understanding of GPS system and navigation; become proficient with particular GPS installation, displays, and autopilot interfaces; become proficient at using GPS in-flight, including modifying flight plan and changing approaches. 

### Resources
- [[POH]]/[[AFM]]
- GPS manual

> [!tip] Pre-Lesson Reading/Homework here: [[~ IR Pre-Lesson Reading]]

### Builds On
[[IR.5A VOR Navigation]]

### Schedule
Ground 1-hour, simulator and/or airplane, 2 hours^[may need less time based on depth of PPL training]

### Lesson Elements
1. [[Satellite Navigation using GPS and GNSS]]
4. IFR flight Using GPS
	1. Required Preflight
		1. Check for DB alerts (e.g. [From Garmin](https://www.garmin.com/en-US/aviationalerts/))^[If an approach was published with errors, you want to know!]
		2. Review the self-test output: includes things like displaying a specific course, lateral/vertical deflection, etc^[This check is part of Section 4 added by the GPS [[STC]].]
		3. WAAS availability (https://www.nstb.tc.faa.gov/ and [[WAAS LPV.png]])
	2. Installation approval and operational approval required
	3. TSO 129/196 (Non-WAAS) requires alternate approved and operational means of navigation
	4. Expired database - https://www.ifr-magazine.com/charts-plates/is-expired-data-usable/
		1. IFR enroute/terminal - verification of data for correctness
		2. IFR approach - current database or verification procedure has not been amended since expiration of database
		3. Checkride - not allowed per [[Instrument ACS]]
5. GPS Sensitivity ([[RNP Precision per Approach Segment.jpeg]] and [[G1000 Automatic CDI Scaling.png]])
	1. Enroute  ±2nm, default
	2. Terminal - ±1nm
		1. Within 31nm of destination
		2. In term on dep until beyond 30nm from departure
	3. Approach - ±0.3nm 
		1. 2.0nm from [[FAF]]
	4. Missed - 0.3nm
6. GPS Functions
	1. GPS Approaches		  
		1. [[LNAV]], [[LP]]
		2. [[LPV]], LNAV/VNAV, LNAV+V
		3. [The 4 Different Types of Vertical Guidance in IFR Flying](https://www.boldmethod.com/shorts/shorts.ifr.0019/) from [[Bold Method]]
	2. Flight Plan
	3. Direct to
	4. [[OBS]]
	5. Airport/NAVAID Information
	6. Identifying waypoints (e.g. for [[DME]])
	7. Flight calculations
7. Managing risk of various GPS idiosyncrasies
	1. How to suspend GPS sequencing for multiple turns in a hold? 
	2. How to resume approach after holding? 
	3. Pop-up or other method to resume sequencing to missed approach point
	4. Use of vectors to final ([[VTF]]) with GPS (don’t do it!) 
		1. If ATC changes their mind, you've already deleted all your points^[This was most true of older GPS models, many newer ones don't automatically delete all points]
		2. Best to load full procedure and activate a specific leg along the approach when you're vectored in
	5. Using GPS for guidance on ILS and VOR approaches – how and when to transition from GPS guidance to VOR or Localizer? Auto or manual?
8. [[Autopilot Systems and Usage]]
9. Common Errors
	1. Not knowing your GPS (GPS simulation software for home practice is great!)
	2. VLOC vs GPS
		1. Can you use GPS to fly a ILS procedure turn? No, according to [[AC 90-108]], can't use for "Lateral Navigation on LOC-Based Courses"^[This has to do with GPS terminal mode being less precise then a LOC, and the impact it has on obstacle clearance. [[Max Trescott]] has a great writeup in [[AOPA]] published [here](https://www.aopa.org/news-and-media/all-news/2014/may/05/when-to-switch-to-vloc-on-an-ils-or-vor-approach).]
		2. Plus, want to practice flying ILS procedure turn without GPS, even though you can technically fly using GPS if you monitor ILS raw data
	3. Autoswitch GPS>VLOC errors
		1. Won't switch if vectored too close to FAF, or if GPS doesn't hear the morse code
		2. DPEs call this the $1000 button, since it's the most common cause of failures
	4. Switching autopilot between GPS, VOR, heading bug, etc. 
	5. Always practicing with GPS flight plan installed or as a backup monitoring -- you should be able to fly a full IFR flight plan with only VOR equipment
	6. Risk management - New or unfamiliar GPS demands significant practice with VFR conditions before using in IMC! GPS brings impressive capabilities and situational awareness, but at the risk of significant complexity and variability between systems! 

### Completion Standards
Student must understand the different types of GPS installations and “flavors” of GPS approaches. Student must become proficient at creating GPS flight plans, navigating with GPS, and modifying flight plans and approach selections. Student must understand particular GPS techniques for holding and flying missed approaches and using autopilot interfaces (if installed).

### Required Logbook Phraseology
For [[FAR 61.65 Instrument Rating Reqs]]:
- Navigation systems


*Return to [[~ IR Lesson Plan Outline|Table of Contents]]^*