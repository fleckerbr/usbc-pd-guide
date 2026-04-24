# Configuration Channel

## Configuration Channel Pin States

The following two tables define the electrical states for a CC pin in both a Source and a Sink.
Every port has CC1 and CC2 pins, each with its own individual CC pin state.
The combination of a port's CC1 and CC2 pin states are used to define the conditions under which the
[Configuration Channel Manager](./port-manager/configuration-channel-manager/index.md) transitions from one state to another.

### Source Port CC Pin State

| CC Pin State      | Port Partner CC<br>Termination    | Voltage Detected on CC when<br>port asserts Rp                    |
| :---------------: | :-------------------------------: | :---------------------------------------------------------------: |
| `SRC.Open`        | Open, Rp                          | Above vOPEN                                                       |
| `SRC.Rd`          | Rd                                | Within the vRd range (i.e., between<br>minimum and maximum vRd)   |
| `SRC.Ra`          | Ra                                | Below maximum vRa                                                 |

### Sink Port CC Pin State

| CC Pin State      | Port Partner CC<br>Termination    | Voltage Detected on CC when<br>port asserts Rd                    |
| :---------------: | :-------------------------------: | :---------------------------------------------------------------: |
| `SNK.Open`        | Open, Ra, Rd                      | Below maximum vRa                                                 |
| `SNK.Default`     | Rp                                | Above minimum vRd-Connect                                         |
| `SNK.Power1.5`    | Rp 1.5A                           | Above minimum vRd-Connect                                         |
| `SNK.Power3.0`    | Rp 3.0A                           | Above minimum vRd-Connect                                         |

!!! note "SNK.Rp State"
    Whenever this documentation refers to the SNK.Rp pin state, it should be treated as an abbreviation for any of the
    pin states that detect a port partner advertising Rp (i.e., SNK.Default, SNK.Power1.5, or SNK.Power3.0)
