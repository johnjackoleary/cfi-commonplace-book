# Key Takeaways
- Knowing the crosswind component is critical for ensuring a landing can be safely attempted
- Since decisions about crosswind occur in flight, rules-of-thumb are appropriate

# Details
## Methods for Computing
### Chart
[[AFH Ch9]], [[E6B]]s, and many [[POH]]s have a circular chart for looking up the crosswind based on the wind angle.

While simple, this is slower and not helpful while in flight.

### Trigonometry
The most precise calculation comes from trigonometry.
$$
wind * sin(angle) = crosswind
$$

This is not very helpful while in flight.^[Plus, it's probably misleadingly precise given the rounded runway or wind angle measurements]

### Estimates at 30°, 45°, and 60°
The simplest practical version requires memorizing the sine at a few key angles.

| Angle | Sine | Memorize Approximate % of Crosswind |
| ----- | ---- | ----------------------------------- |
| 30    | 0.5  | 50%                                 |
| 45    | 0.7  | 75%                                 |
| 60    | 0.9 | 100%                                |

### Rule of Sixths
A slightly higher resolution rule-of-thumb uses the [[Rule of Sixths]].

![[Rule of Sixths]]

## [[True North vs Magnetic North]]
[[METAR]]s and [[TAF]]s are reported in true north, while runway heads are reported in magnetic north. To find the angle between them, we convert between these different 'norths' using the local [[magnetic variation]].

> [!note] 
> [[ATIS]]/[[AWOS]]s are reported in magnetic north, since they need to be used in flight where we use our magnetic compass for reference.
> 
> This leads to the memory aid: [[If It's Written It Must Be True]]

# Additional Resources
- [[AFH Ch9]]

#concept