---
tags: [maneuver]
config: "[[Maneuvers Config]]"
content: "<font color=\"goldenrod\">APAMCO · ID Emgcy Field`=choice(this.config.aircraft.has-carb-heat, [[Maneuver Set-Up]].carb-heat-opt-text, \"\")`</font>"
carb-heat-opt-text :: " · Carb Heat On (If Below Green)"
---
`= this.content`