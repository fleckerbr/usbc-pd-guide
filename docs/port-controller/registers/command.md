<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# COMMAND

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x23`                | [COMMAND]             | `Write`           | `0x00`            |

## Description

The [COMMAND] register is issued and written by the TCPM.
The [COMMAND] register is cleared by the TCPC after being acted upon.

The TCPM shall issue [COMMAND.Look4Connection] to enable the TCPC to autonomously toggle the Rp/Rd.
The initial Rp or Rd for toggling is determined by [ROLE_CONTROL.CC1] and [ROLE_CONTROL.CC2].
If [ROLE_CONTROL.CC1] and [ROLE_CONTROL.CC2] are not the same value, the [COMMAND.Look4Connection] shall have no effect.
If [POWER_CONTROL.AutoDischargeDisconnect] is not set to `0b`, the [COMMAND.Look4Connection] shall have no effect.

The TCPM shall issue [COMMAND.Look4Connection] to enable the TCPC to restart Connection Detection in cases where the role is fixed as Source or Sink, [ROLE_CONTROL.DRP]=`0b`.
An example of this is when a potential connection as a Source occurred but was further debounced by the TCPM to find the Sink disconnected.
In this case, a Source Only or DRP should go back to its Unattached.SRC state (as defined in [USB TC]).
This would result in [ROLE_CONTROL] staying the same.

[COMMAND.I2CIdle] is used to put the I2C interface into the idle state.
When the TCPC receives [COMMAND.I2CIdle], the TCPC may generate a bit-level Not Acknowledge signal
(a NAK where SDA remains HIGH during the ninth clock pulse) to its own slave address or any I2C commands.

The TCPM may send the [COMMAND.WakeI2C] as a throw away command to wake the I2C interface.
The [COMMAND.WakeI2C] requires no action by the TCPC other than to wake the I2C device interface in the TCPC.

[COMMAND.I2CIdle] is decoupled from other Alert status detection mechanisms (such as [CC_STATUS], [POWER_STATUS], [RECEIVE_DETECT], etc).
For example, writing [COMMAND.I2CIdle] has no effect on [ALERT.CCStatus], or the [CC_STATUS] register behavior.
[CC_STATUS] detection may be disabled by writing to the [ROLE_CONTROL] register, but its behavior is not affected by the [COMMAND.I2CIdle].

While there is a valid Source-to-Sink connection, the TCPM acting as a Sink shall write [COMMAND.DisableSinkVbus] (if [DEVICE_CAPABILITIES_1.SinkVbus]=`1b`)
to remove the Sink connection upon reception of or prior to transmitting a Power Role Swap or Hard Reset.

The TCPM shall issue [COMMAND.SourceVbusNondefaultVoltage] to enable the TCPC to transition the VBus source to a nondefault voltage level.
[VBUS_NONDEFAULT_TARGET] is an optional register declared in [DEVICE_CAPABILITIES_1] register.
The target voltage for [COMMAND.SourceVbusNondefaultVoltage] can be set in the [VBUS_NONDEFAULT_TARGET] register.
Alternatively, the target voltage level for [COMMAND.SourceVbusNondefaultVoltage] is set in a vendor defined manner.
The steps of transitioning to source a nondefault voltage over VBus using [VBUS_NONDEFAULT_TARGET] register shall be as follow:

  1.  TCPC supplies vSafe5V over VBus
  2.  TCPM writes to [VBUS_NONDEFAULT_TARGET] to set the target voltage level of [COMMAND.SourceVbusNondefaultVoltage]
  3.  TCPM issues [COMMAND.SourceVbusNondefaultVoltage]
  4.  TCPC starts the operation of transitioning to the target voltage level as given in [VBUS_NONDEFAULT_TARGET].
      For TCPC that integrates the power converter, the TCPC shall control the voltage transitioning and meet the power supply requirements in the USB PD Specification.

If the TCPM has a new target voltage level for [COMMAND.SourceVbusNondefaultVoltage], it shall repeat Step2.
The TCPM is not required to go back to vSafe5V and then to a different voltage.
It may go directly to the new voltage by writing new values to [VBUS_NONDEFAULT_TARGET] and then issuing the [COMMAND.SourceVbusNondefaultVoltage].

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..0`       | Wake I2C                                  | [COMMAND.WakeI2C]                         |
| `B7..0`       | Disable VBus Detect                       | [COMMAND.DisableVBusDetect]               |
| `B7..0`       | Enable VBus Detect                        | [COMMAND.EnableVBusDetect]                |
| `B7..0`       | Disable Sink VBus                         | [COMMAND.DisableSinkVBus]                 |
| `B7..0`       | Sink VBus                                 | [COMMAND.SinkVBus]                        |
| `B7..0`       | Disable Source VBus                       | [COMMAND.DisableSourceVBus]               |
| `B7..0`       | Source VBus Default Voltage               | [COMMAND.SourceVBusDefaultVoltage]        |
| `B7..0`       | Source VBus Nondefault Voltage            | [COMMAND.SourceVBusNondefaultVoltage]     |
| `B7..0`       | Look4Connection                           | [COMMAND.Look4Connection]                 |
| `B7..0`       | Receive One More                          | [COMMAND.RxOneMore]                       |
| `B7..0`       | Send FR Swap Signal                       | [COMMAND.SendFRSwapSignal]                |
| `B7..0`       | Reset Transmit Buffer                     | [COMMAND.ResetTransmitBuffer]             |
| `B7..0`       | Reset Receive Buffer                      | [COMMAND.ResetReceiveBuffer]              |
| `B7..0`       | I2C Idle                                  | [COMMAND.I2CIdle]                         |

### `B7..0` Wake I2C { #wake-i2c data-toc-label="Wake I2C" }

!!! success "COMMAND.WakeI2C (Required)"
    `00010001b` :material-arrow-right-thin: No action is taken other than to wake the I2C interface.

### `B7..0` Disable VBus Detect { #disable-vbus-detect data-toc-label="Disable VBus Detect" }

!!! success "COMMAND.DisableVBusDetect (Required)"
    `00100010b` :material-arrow-right-thin: Disable VBus present and vSafe0V detection.

    :   This is an invalid [COMMAND] if the TCPC has sourcing or sinking power over VBus enabled.

### `B7..0` Enable VBus Detect { #enable-vbus-detect data-toc-label="Enable VBus Detect" }

!!! success "COMMAND.EnableVBusDetect (Required)"
    `00110011b` :material-arrow-right-thin: Enable VBus present and vSafe0V detection.

### `B7..0` Disable Sink VBus { #disable-sink-vbus data-toc-label="Disable Sink VBus" }

!!! success "COMMAND.DisableSinkVBus (Required)"
    `01000100b` :material-arrow-right-thin: Disable sinking power over VBus and discharge to vSave0V.

    :   This [COMMAND] does not disable [POWER_STATUS.VBusPresent] detection.

        The TCPC shall clear [FAULT_STATUS.InternalOrExternalOCP] and [FAULT_STATUS.InternalOrExternalOVP].

### `B7..0` Sink VBus { #sink-vbus data-toc-label="Sink VBus" }

!!! success "COMMAND.SinkVBus (Required)"
    `01010101b` :material-arrow-right-thin: Enable sinking power over VBus and enable VBus present detection.

    :   This is an invalid [COMMAND] if the TCPC has sourcing power over VBus enabled.

### `B7..0` Disable Source VBus { #disable-source-vbus data-toc-label="Disable Source VBus" }

!!! success "COMMAND.DisableSourceVBus (Required)"
    `01100110b` :material-arrow-right-thin: Disable sourcing power over VBus and discharge to vSave0V.

    :   The TCPC shall stop reporting [FAULT_STATUS].
        Internal or External OCP or OVP Faults.
        This [COMMAND] does not disable [POWER_STATUS.VBusPresent] detection.

### `B7..0` Source VBus Default Voltage { #source-vbus-default-voltage data-toc-label="Source VBus Default Voltage" }

!!! success "COMMAND.SourceVBusDefaultVoltage (Required)"
    `01110111b` :material-arrow-right-thin: Enable sourcing vSafe5V over VBus and enable VBus present detection.

    :   The TCPC shall transition to vSafe5V if it is sourcing nondefault voltage.
        This is an invalid [COMMAND] if the TCPC has sinking power over VBus enabled.

### `B7..0` Source VBus Nondefault Voltage { #source-vbus-nondefault-voltage data-toc-label="Source VBus Nondefault Voltage" }

!!! success "COMMAND.SourceVBusNondefaultVoltage (Required)"
    `10001000b` :material-arrow-right-thin: Execute transitioning VBus to a nondefault voltage level.

    :   This is an invalid [COMMAND] if the TCPC is currently sinking voltage from VBus,
        or the TCPC does not have the ability to source nondefault voltages (i.e. other than vSafe5V).
        This is also an invalid [COMMAND] if the TCPC is not already sourcing power over VBus.

        The target VBus voltage to be sourced may be set in a vendor defined manner.
        The TCPM may need to write to vendor defined register before sending this [COMMAND].

### `B7..0` Look4Connection { #look4connection data-toc-label="Look4Connection" }

!!! success "COMMAND.Look4Connection (Required)"
    `10011001b` :material-arrow-right-thin: Start DRP Toggling if [ROLE_CONTROL.DRP]=`1b`.

    :   If [ROLE_CONTROL.CC1]/[CC2](/usbc-pd-buide/port-controller/registers/role-control/#cc2) = `01b` start with Rp,
        if [ROLE_CONTROL.CC1]/[CC2](/usbc-pd-buide/port-controller/registers/role-control/#cc2) = `10b` start with Rd.

        If [ROLE_CONTROL.CC1]/[CC2](/usbc-pd-buide/port-controller/registers/role-control/#cc2) are not both `01b` or `10b`,
        or if [POWER_CONTROL.AutoDischargeDisconnect] is not `0b`, then do not start toggling.

        The TCPM shall issue [COMMAND.Look4Connection] to enable the TCPC to restart Connection Detection
        in cases where the [ROLE_CONTROL] contents will not change.
        An example of this is when a potential connection as a Source occurred but was further debounced by the TCPM to find the Sink disconnected.
        In this case a Source Only or DRP should go back to its Unattached.SRC state (as defined in [USB TC]).
        This would result in [ROLE_CONTROL] staying the same.

### `B7..0` Receive One More { #receive-one-more data-toc-label="Receive One More" }

!!! success "COMMAND.RxOneMore (Required)"
    `10011001b` :material-arrow-right-thin: Disable PD message delivery after the next GoodCRC message is received.

    :   Configure the TCPC to automatically clear the [RECEIVE_DETECT] register after sending the next GoodCRC.
        This is used to disable message passing at a known point regardless of message separation or the depth of the [RECEIVE_BUFFER] in the TCPC.

### `B7..0` Send FR Swap Signal { #send-fr-swap-signal data-toc-label="Send FR Swap Signal" }

!!! success "COMMAND.SendFRSwapSignal (Required)"
    `11001100b` :material-arrow-right-thin: Send a Fast Role Swap signal within tTCPCSendFRSwap.

    :   Source TCPC sends Fast Role Swap signal after receiving this [COMMAND] if [POWER_CONTROL.FastRoleSwapEnable]=`1b`.
        This is an invalid [COMMAND] if [POWER_CONTROL.FastRoleSwapEnable]=`0b`.

### `B7..0` Reset Transmit Buffer { #reset-transmit-buffer data-toc-label="Reset Transmit Buffer" }

!!! success "COMMAND.ResetTransmitBuffer (Required)"
    `11011101b` :material-arrow-right-thin: The TCPC resets the pointer of the [TRANSMIT_BUFFER] register to offset 1.

    :   When this [COMMAND] is issued by the TCPM the contents of [TRANSMIT_BUFFER] becomes invalid.
        This [COMMAND] shall be supported by TCPC compliant with USB Port Controller Specification Revision 2.0.

### `B7..0` Reset Receive Buffer { #reset-receive-buffer data-toc-label="Reset Receive Buffer" }

!!! success "COMMAND.ResetReceiveBuffer (Required)"
    `11101110b` :material-arrow-right-thin: The TCPC resets the pointer of [RECEIVE_BUFFER] when this [COMMAND] is issued by the TCPM.

    :   If the pointer of [RX_BUF_BYTE_x] is at 132 or less, writing this [COMMAND] would reset the pointer to 1.
        If the pointer of [RX_BUF_BYTE_x] is at 133 or higher, writing this [COMMAND] would reset the pointer to 133.

        TCPC does not clear the content of the buffer upon receiving this [COMMAND].
        The TCPM issues this [COMMAND] in order to re-read the [RX_BUF_BYTE_x].

        This [COMMAND] shall be supported by TCPC compliant with USB Port Controller Specification Revision 2.0.

### `B7..0` I2C Idle { #i2c-idle data-toc-label="I2C Idle" }

!!! success "COMMAND.I2CIdle (Required)"
    `11111111b` :material-arrow-right-thin: Put the I2C interface to sleep.

    :   [COMMAND.WakeI2C] must be sent to re-enable the rest of the I2C interface after this [COMMAND] is sent.
