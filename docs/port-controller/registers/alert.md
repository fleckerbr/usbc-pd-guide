<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# ALERT

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x10`..`0x11`        | [ALERT]               | `Read`/`Write`    | `0x0000`          |

## Description

This register is set by TCPC and cleared by TCPM.

This register is used to communicate a status change from the TCPC to the TCPM.
After an event or condition occurs, the TCPC shall set the corresponding bit in the [ALERT] register.
The TCPC shall keep the bit associated with the [ALERT] asserted until the TCPM writes a `1b` to clear it.

The TCPC indicates an alert status change has occurred by presenting a `1b` in the corresponding
alert bit position in this register and asserting the [Alert#] pin.
The TCPM clears the [ALERT] bit by writing a `1b` to the respective [ALERT] bit position.
The TCPM can clear any number of [ALERT] bits in a single write by setting multiple bits to
`1b` and the rest of the bits in the register to `0b`.
The TCPM writing a `0b` to any [ALERT] bit has no effect, and therefore does not cause those [ALERT] bits to be set or cleared.
The [Alert#] pin remains asserted until all [ALERT] bits are cleared by the TCPM.
If the TCPM writes a `1b` to a bit that is already `0b`, the TCPC shall not change the value of that bit.

Writing a `1b` to [ALERT.RxBufferOverflow] does not clear it unless the TCPM also writes a `1b` to [ALERT.RxStatus].
The [ALERT.RxBufferOverflow] is always asserted if the SOP\* buffer registers are full,
and those registers can only be cleared by writing a `1b` to [ALERT.RxStatus].

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15`         | Vendor Defined Alert                      | [ALERT.VendorDefinedAlert]                |
| `B14`         | Alert Extended                            | [ALERT.AlertExtended]                     |
| `B13`         | Extended Status                           | [ALERT.ExtendedStatus]                    |
| `B12`         | Beginning SOP* Message Status             | [ALERT.RxBeginningStatus]                 |
| `B11`         | VBus Sink Disconnect Detected             | [ALERT.VBusSinkDisconnectDetected]        |
| `B10`         | Receive Buffer Overflow                   | [ALERT.RxBufferOverflow]                  |
| `B9`          | Fault                                     | [ALERT.Fault]                             |
| `B8`          | VBus Voltage Alarm Low                    | [ALERT.VBusVoltageAlarmLo]                |
| `B7`          | VBus Voltage Alarm High                   | [ALERT.VBusVoltageAlarmHi]                |
| `B6`          | Transmit SOP* Message Successful          | [ALERT.TxMessageSuccessful]               |
| `B5`          | Transmit SOP* Message Discarded           | [ALERT.TxMessageDiscarded]                |
| `B4`          | Transmit SOP* Message Failed              | [ALERT.TxMessageFailed]                   |
| `B3`          | Received Hard Reset                       | [ALERT.HardReset]                         |
| `B2`          | Received SOP* Message Status              | [ALERT.RxStatus]                          |
| `B1`          | Power Status                              | [ALERT.PowerStatus]                       |
| `B0`          | CC Status                                 | [ALERT.CCStatus]                          |

### `B15` Vendor Defined Alert { #vendor-defined-alert data-toc-label="Vendor Defined Alert" }

!!! success "ALERT.VendorDefinedAlert (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: A vendor defined alert has been detected.

    :   Defined in the [VENDOR_DEFINED] registers. Refer to the vendor datasheet for details.
        This bit can be cleared, regardless of the current status of the alert source.

### `B14` Alert Extended { #alert-extended data-toc-label="Alert Extended" }

!!! success "ALERT.AlertExtended (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: An extended interrupt event has occurred.

    :   Read the [ALERT_EXTENDED] register.

### `B13` Extended Status { #extended-status data-toc-label="Extended Status" }

!!! success "ALERT.ExtendedStatus (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: Extended Status changed.

### `B12` Beginning SOP\* Message Status { #beginning-sop-message-status data-toc-label="Beginning SOP* Message Status" }

!!! success "ALERT.RxBeginningStatus (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: The [RECEIVE_BUFFER] register changed.

    :   Setting [READABLE_BYTE_COUNT] to 0 does not set this bit.
        Set if [READABLE_BYTE_COUNT] is greater than 133 to indicate an extended USB PD message with
        more than 128 data bytes has been received. Not set if [READABLE_BYTE_COUNT] is 133 or less.

### `B11` VBus Sink Disconnect Detected { #vbus-sink-disconnect-detected data-toc-label="VBus Sink Disconnect Detected" }

!!! success "ALERT.VBusSinkDisconnectDetected (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: The TCPC in [Attached.SNK] state has detected a Sink disconnect.

    :   This bit shall only be asserted when [POWER_CONTROL.AutoDischargeDisconnect] is set.
        The Sink TCPC asserts this bit either when [POWER_STATUS.VbusPresent] transitions from `1b` to `0b`
        (if [DEVICE_CAPABILITIES_2.SinkDisconnectDetection]=`0b`) or the TCPC detects VBUS falling below
        [VBUS_SINK_DISCONNECT_THRESHOLD] (if [DEVICE_CAPABILITIES_2.SinkDisconnectDetection]=`1b`).

### `B10` Receive Buffer Overflow { #receive-buffer-overflow data-toc-label="Receive Buffer Overflow" }

!!! success "ALERT.RxBufferOverflow (Required)"
    `0b` :material-arrow-right-thin: TCPC Rx buffer is functioning properly.

    `1b` :material-arrow-right-thin: TCPC Rx buffer has overflowed.

    :   Future GoodCRC shall not be sent.
        Writing 1 to this register acknowledges the overflow.
        The overflow is cleared by writing to [ALERT.RxStatus].

### `B9` Fault { #fault data-toc-label="Fault" }

!!! success "ALERT.Fault (Required)"
    `0b` :material-arrow-right-thin: No fault.

    `1b` :material-arrow-right-thin: A fault has occurred.

    :   Read the [FAULT_STATUS] register.

### `B8` VBus Voltage Alarm Low { #vbus-voltage-alarm-low data-toc-label="VBus Voltage Alarm Low" }

!!! success "ALERT.VBusVoltageAlarmLo (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: A low-voltage alarm has occurred.

### `B7` VBus Voltage Alarm High { #vbus-voltage-alarm-high data-toc-label="VBus Voltage Alarm High" }

!!! success "ALERT.VBusVoltageAlarmHi (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: A high-voltage alarm has occurred.

### `B6` Transmit SOP\* Message Successful { #transmit-sop-message-successful data-toc-label="Transmit SOP* Message Successful" }

!!! success "ALERT.TxMessageSuccessful (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: Reset or SOP\* message transmission successful.

    :   GoodCRC response received on SOP\* message transmission.
        Transmit SOP\* message buffer registers are empty.

### `B5` Transmit SOP\* Message Discarded { #transmit-sop-message-discarded data-toc-label="Transmit SOP* Message Discarded" }

!!! success "ALERT.TxMessageDiscarded (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: Reset or SOP\* message transmission not sent due to an incoming receive message.

    :   Transmit SOP\* message buffer registers are empty.

### `B4` Transmit SOP\* Message Failed { #transmit-sop-message-failed data-toc-label="Transmit SOP* Message Failed" }

!!! success "ALERT.TxMessageFailed (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: SOP\* message transmission not successful.

    :   No GoodCRC response received on SOP\* message transmission.
        Transmit SOP\* message buffer registers are empty.

### `B3` Received Hard Reset { #received-hard-reset data-toc-label="Received Hard Reset" }

!!! success "ALERT.HardReset (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: Received Hard Reset message.

### `B2` Received SOP\* Message Status { #received-sop-message-status data-toc-label="Received SOP* Message Status" }

!!! success "ALERT.RxStatus (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: [RECEIVE_BUFFER] register changed.

    :   [READABLE_BYTE_COUNT] being set to 0 does not set this bit.

### `B1` Power Status { #power-status data-toc-label="Power Status" }

!!! success "ALERT.PowerStatus (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: Power Status changed.

    :   Read the [POWER_STATUS] register.

### `B0` CC Status { #cc-status data-toc-label="CC Status" }

!!! success "ALERT.CCStatus (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: CC Status changed.

    :   TCPC shall not assert this bit when [CC_STATUS.Looking4Connection] changes state
        if [TCPC_CONTROL.EnableLooking4ConnectionAlert] is set to `0b`.
