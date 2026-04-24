# STANDARD_OUTPUT_SIGNAL

## Description

Support for any of these signals shall be declared in the [STANDARD_OUTPUT_CAPABILITIES] register.
This section defines the [STANDARD_OUTPUT_SIGNAL] from the TCPC.
The output signals may or may not be controlled by the TCPM.

Outputs may be Push/Pull or Open Drain. Refer to the TCPC datasheet for definition.
Outputs which are Push/Pull are referenced to VDDIO and may be the same or different than the VDD supply voltage for the I2C interface.
Outputs where noted are tri-stated on disconnect.

## Output Signals

### Alert#

!!! abstract "STANDARD_OUTPUT_SIGNAL.Alert# (Open Drain)"
    `Low` :material-arrow-right-thin: Alert.

    :   The TCPC is indicating an Alert Status change has occurred.
        The TCPM shall read the [ALERT] Register to determine what event triggered the Alert.

    `High` :material-arrow-right-thin: No Alert.

### Debug Connected Accessory#

!!! abstract "STANDARD_OUTPUT_SIGNAL.DebugConnectedAccessory# (Push/Pull or Open Drain)"
    `High` :material-arrow-right-thin: No Debug Accessory connected.

    `Low` :material-arrow-right-thin: Debug Accessory connected.

### VBus Present#

!!! abstract "STANDARD_OUTPUT_SIGNAL.VBusPresent# (Push/Pull or Open Drain)"
    `Low` :material-arrow-right-thin: VBus is present.

    `High` :material-arrow-right-thin: VBus is not present.

### Audio Connected Accessory#

!!! abstract "STANDARD_OUTPUT_SIGNAL.AudioConnectedAccessory# (Push/Pull or Open Drain)"
    `High` :material-arrow-right-thin: No Audio Accessory connected.

    `Low` :material-arrow-right-thin: Audio Accessory connected.

### Active Cable Connected

!!! abstract "STANDARD_OUTPUT_SIGNAL.ActiveCableConnected (Push/Pull or Open Drain)"
    `High` :material-arrow-right-thin: Active Cable connected.

    `Low` :material-arrow-right-thin: No Active Cable connected.

### MUX Control 1

!!! abstract "STANDARD_OUTPUT_SIGNAL.MUXControl1 (Push/Pull or Open Drain)"
    `Low` :material-arrow-right-thin: No DP Alternate Mode.

    `High` :material-arrow-right-thin: DP Alternate Mode.


### MUX Control 0

!!! abstract "STANDARD_OUTPUT_SIGNAL.MUXControl0 (Push/Pull or Open Drain)"
    `Low` :material-arrow-right-thin: No connection or no USB connection.

    `High` :material-arrow-right-thin: USB connection.

### Connection Present

!!! abstract "STANDARD_OUTPUT_SIGNAL.ConnectionPresent (Push/Pull or Open Drain)"
    `Low` :material-arrow-right-thin: No connection.

    `High` :material-arrow-right-thin: Connection.

### Connector Orientation

!!! abstract "STANDARD_OUTPUT_SIGNAL.ConnectorOrientation (Push/Pull or Open Drain)"
    `Low` :material-arrow-right-thin: Normal (default).

    `High` :material-arrow-right-thin: Flipped.

### VBus Sink Disconnect Detected

!!! abstract "STANDARD_OUTPUT_SIGNAL.VBusSinkDisconnectDetected (Push/Pull or Open Drain)"
    `Low` :material-arrow-right-thin: VBus Sink disconnect detected.

    :   The TCPC indicates VBus Sink disconnect has been detected and [ALERT.VBusSinkDisconnectDetected] has been asserted.
        This is either when [POWER_STATUS.VBusPresent] transitions from `1b` to `0b` (if [DEVICE_CAPABILITIES_2.SinkDisconnectDetection]=`0b`)
        or the TCPC detects VBus falling below [VBUS_SINK_DISCONNECT_THRESHOLD] (if [DEVICE_CAPABILITIES_2.SinkDisconnectDetection]=`1b`).

    `High` :material-arrow-right-thin: No VBus Sink disconnect detected.

    :   No VBus Sink disconnect has been detected or the TCPC has cleared the status of this signal by writing `1b` to [ALERT.VBusSinkDisconnectDetected].
