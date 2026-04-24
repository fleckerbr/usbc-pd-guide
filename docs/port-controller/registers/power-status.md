<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# POWER_STATUS

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x1E`                | [POWER_STATUS]        | `Read`            |                   |

## Description

This register is set and cleared by the TCPC.
The TCPM reads this register upon detecting an [Alert#] and reading the [ALERT.PowerStatus] bit set to `1b`.
The TCPC indicates the current Power Status in this register.

The TCPM operating as a Sink at vSafe5V (with or without a USB PD Contract) shall detect VBus presence and removal by reading the [VBusPresent](/usbc-pd-buide/port-controller/registers/power-status/#vbus-present) bit.

The TCPM shall check the state of the TCPC Initialization Status bit when it starts or resets.
The TCPM shall not start normal operation until the TCPC Initialization Status bit is cleared.
The TCPC shall set the TCPC Initialization Status bit to zero when initialization or reset is complete and all registers are valid.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                    |
| ------------- | ----------------------------------------- | --------------------------------------------- |
| `B7`          | Debug Accessory Connected                 | [POWER_STATUS.DebugAccessoryConnected]        |
| `B6`          | TCPC Initialization Status                | [POWER_STATUS.TCPCInitializationStatus]       |
| `B5`          | Sourcing Nondefault Voltage               | [POWER_STATUS.SourcingNondefaultVoltage]      |
| `B4`          | Sourcing VBus                             | [POWER_STATUS.SourcingVBus]                   |
| `B3`          | VBus Detection Enabled                    | [POWER_STATUS.VBusDetectionEnabled]           |
| `B2`          | VBus Present                              | [POWER_STATUS.VBusPresent]                    |
| `B1`          | VConn Present                             | [POWER_STATUS.VConnPresent]                   |
| `B0`          | Sinking VBus                              | [POWER_STATUS.SinkingVBus]                    |

### `B7` Debug Accessory Connected { #debug-accessory-connected data-toc-label="Debug Accessory Connected" }

!!! warning "POWER_STATUS.DebugAccessoryConnected (Optional)"
    `0b` :material-arrow-right-thin: No Debug Accessory connected (default).

    `1b` :material-arrow-right-thin: Debug Accessory connected.

    Reflects the state of the [DebugConnectedAccessory#] output if supported.

### `B6` TCPC Initialization Status { #tcpc-initialization-status data-toc-label="TCPC Initialization Status" }

!!! success "POWER_STATUS.TCPCInitializationStatus (Required)"
    `0b` :material-arrow-right-thin: The TCPC has completed initialization and all registers are valid.

    `1b` :material-arrow-right-thin: The TCPC is still performing internal initialization.

    :   The only registers that are guaranteed to return the correct values are `0x00`..`0x0F`.

### `B5` Sourcing Nondefault Voltage { #sourcing-nondefault-voltage data-toc-label="Sourcing Nondefault Voltage" }

!!! warning "POWER_STATUS.SourcingNondefaultVoltage (Optional)"
    `0b` :material-arrow-right-thin: vSafe5V.

    `1b` :material-arrow-right-thin: Nondefault VBus voltage.

    This bit does not control the power path, it just provides a monitor of the status.
    This bit is asserted as long as the TCPC is sourcing nondefault voltage over VBus (i.e. not vSafe5V)
    as a response to TCPM writing to [COMMAND.SourceVBusNondefaultVoltage].

    Required if nondefault VBus voltage can be sourced.

    This bit is not valid if [POWER_STATUS.SourcingVBus]=`0b`.

### `B4` Sourcing VBus { #sourcing-vbus data-toc-label="Sourcing VBus" }

!!! success "POWER_STATUS.SourcingVBus (Required)"
    `0b` :material-arrow-right-thin: Sourcing VBus is disabled.

    `1b` :material-arrow-right-thin: Sourcing VBus is enabled.

    This bit does not control the power path, it just provides a monitor of the status.

### `B3` VBus Detection Enabled { #vbus-detection-enabled data-toc-label="VBus Detection Enabled" }

!!! success "POWER_STATUS.VBusDetectionEnabled (Required)"
    `0b` :material-arrow-right-thin: VBus detection disabled.

    `1b` :material-arrow-right-thin: VBus detection enabled (default).

    Indicates whether the TCPC is monitoring for [POWER_STATUS.VBusPresent] and vSafe0V level, or the detection circuits have been powered off.

### `B2` VBus Present { #vbus-present data-toc-label="VBus Present" }

!!! success "POWER_STATUS.VBusPresent (Required)"
    `0b` :material-arrow-right-thin: VBus disconnected.

    `1b` :material-arrow-right-thin: VBus connected.

    The TCPC shall report VBus present when TCPC detects VBus rises above 4V.
    The TCPC shall report VBus is not present when TCPC detects VBus falls below 3.5V.
    The TCPC may report VBus is not present if VBus is between 3.5V and 4V.

    This bit is not valid when [POWER_STATUS.VbusDetectionEnabled]=`0b`.

### `B1` VConn Present { #vconn-present data-toc-label="VConn Present" }

!!! success "POWER_STATUS.VConnPresent (Required)"
    `0b` :material-arrow-right-thin: VConn is not present.

    `1b` :material-arrow-right-thin: This bit is asserted when VConn present on CC1 or CC2.

    :   Threshold is fixed at 2.4V

    If [POWER_CONTROL.EnableVConn] is disabled this bit should be set to `0b`.

### `B0` Sinking VBus { #sinking-vbus data-toc-label="Sinking VBus" }

!!! success "POWER_STATUS.SinkingVBus (Required)"
    `0b` :material-arrow-right-thin: Sink is disconnected (default and if sinking VBus is not supported).

    `1b` :material-arrow-right-thin: TCPC is sinking VBus to the system load.
