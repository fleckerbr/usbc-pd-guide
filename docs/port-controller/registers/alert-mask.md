<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# ALERT_MASK

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x12`..`0x13`        | [ALERT_MASK]          | `Read`/`Write`    | `0x7FFF`          |

## Description

<<PLACEHOLDER>>

## Register Fields

| Bit(s)        | Name                                      | Identifier                                    |
| ------------- | ----------------------------------------- | --------------------------------------------- |
| `B15`         | Vendor Defined Alert Mask                 | [ALERT_MASK.VendorDefinedAlertMask]           |
| `B14`         | Alert Extended Mask                       | [ALERT_MASK.AlertExtendedMask]                |
| `B13`         | Extended Status Mask                      | [ALERT_MASK.ExtendedStatusMask]               |
| `B12`         | Beginning SOP* Message Status Mask        | [ALERT_MASK.RxBeginningStatusMask]            |
| `B11`         | VBus Sink Disconnect Detected Mask        | [ALERT_MASK.VBusSinkDisconnectDetectedMask]   |
| `B10`         | Receive Buffer Overflow Mask              | [ALERT_MASK.RxBufferOverflowMask]             |
| `B9`          | Fault Mask                                | [ALERT_MASK.FaultMask]                        |
| `B8`          | VBus Voltage Alarm Low Mask               | [ALERT_MASK.VBusVoltageAlarmLowMask]          |
| `B7`          | VBus Voltage Alarm High Mask              | [ALERT_MASK.VBusVoltageAlarmHighMask]         |
| `B6`          | Transmit SOP* Message Successful Mask     | [ALERT_MASK.TxMessageSuccessfulMask]          |
| `B5`          | Transmit SOP* Message Discarded Mask      | [ALERT_MASK.TxMessageDiscardedMask]           |
| `B4`          | Transmit SOP* Message Failed Mask         | [ALERT_MASK.TxMessageFailedMask]              |
| `B3`          | Received Hard Reset Mask                  | [ALERT_MASK.HardResetMask]                    |
| `B2`          | Received SOP* Message Status Mask         | [ALERT_MASK.RxStatusMask]                     |
| `B1`          | Power Status Mask                         | [ALERT_MASK.PowerStatusMask]                  |
| `B0`          | CC Status Mask                            | [ALERT_MASK.CCStatusMask]                     |

### `B15` Vendor Defined Alert Mask { #vendor-defined-alert-mask data-toc-label="Vendor Defined Alert Mask" }

!!! success "ALERT_MASK.VendorDefinedAlertMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B14` Alert Extended Mask { #alert-extended-mask data-toc-label="Alert Extended Mask" }

!!! success "ALERT_MASK.AlertExtendedMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B13` Extended Status Mask { #extended-status-mask data-toc-label="Extended Status Mask" }

!!! success "ALERT_MASK.ExtendedStatusMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B12` Beginning SOP\* Message Status Mask { #beginning-sop-message-status-mask data-toc-label="Beginning SOP* Message Status Mask" }

!!! success "ALERT_MASK.RxBeginningStatusMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B11` VBus Sink Disconnect Detected Mask { #vbus-sink-disconnect-detected-mask data-toc-label="VBus Sink Disconnect Detected Mask" }

!!! success "ALERT_MASK.VBusSinkDisconnectDetectedMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B10` Receive Buffer Overflow Mask { #receive-buffer-overflow-mask data-toc-label="Receive Buffer Overflow Mask" }

!!! success "ALERT_MASK.RxBufferOverflowMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B9` Fault Mask { #fault-mask data-toc-label="Fault Mask" }

!!! success "ALERT_MASK.FaultMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B8` VBus Voltage Alarm Low Mask { #vbus-voltage-alarm-low-mask data-toc-label="VBus Voltage Alarm Low Mask" }

!!! success "ALERT_MASK.VBusVoltageAlarmLowMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B7` VBus Voltage Alarm High Mask { #vbus-voltage-alarm-high-mask data-toc-label="VBus Voltage Alarm High Mask" }

!!! success "ALERT_MASK.VBusVoltageAlarmHighMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B6` Transmit SOP\* Message Successful Mask { #transmit-sop-message-successful-mask data-toc-label="Transmit SOP* Message Successful Mask" }

!!! success "ALERT_MASK.TxMessageSuccessfulMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B5` Transmit SOP\* Message Discarded Mask { #transmit-sop-message-discarded-mask data-toc-label="Transmit SOP* Message Discarded Mask" }

!!! success "ALERT_MASK.TxMessageDiscardedMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B4` Transmit SOP\* Message Failed Mask { #transmit-sop-message-failed-mask data-toc-label="Transmit SOP* Message Failed Mask" }

!!! success "ALERT_MASK.TxMessageFailedMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B3` Received Hard Reset Mask { #received-hard-reset-mask data-toc-label="Received Hard Reset Mask" }

!!! success "ALERT_MASK.HardResetMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

    The Hard Reset should generally *not* be masked.

### `B2` Received SOP\* Message Status Mask { #received-sop-message-status-mask data-toc-label="Received SOP* Message Status Mask" }

!!! success "ALERT_MASK.RxStatusMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B1` Power Status Mask { #power-status-mask data-toc-label="Power Status Mask" }

!!! success "ALERT_MASK.PowerStatusMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.

### `B0` CC Status Mask { #cc-status-mask data-toc-label="CC Status Mask" }

!!! success "ALERT_MASK.CCStatusMask (Required)"
    `0b` :material-arrow-right-thin: Interrupt masked.

    `1b` :material-arrow-right-thin: Interrupt unmasked.
