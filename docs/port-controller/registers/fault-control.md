<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# FAULT_CONTROL

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x1B`                | [FAULT_CONTROL]       | `Read`/`Write`    | `0x00`            |

## Description

After the TCPC has set the power on reset default values, this register is set and cleared only by the TCPM.
The TCPM writes to [FAULT_CONTROL] to enable/disable the fault circuitry.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                            |
| ------------- | ----------------------------------------- | ----------------------------------------------------- |
| `B7..5`       | Reserved                                  |                                                       |
| `B4`          | Force Off VBus                            | [FAULT_CONTROL.ForceOffVBus]                          |
| `B3`          | VBus Discharge Fault Detection Timer      | [FAULT_CONTROL.VBusDischargeFaultDetectionTimer]      |
| `B2`          | VBus Over Current Protection Fault        | [FAULT_CONTROL.InternalOrExternalOCPFault]            |
| `B1`          | VBus Over Voltage Protection Fault        | [FAULT_CONTROL.InternalOrExternalOVPFault]            |
| `B0`          | VConn Over Current Fault                  | [FAULT_CONTROL.VConnOverCurrentFault]                 |

### `B4` Force Off VBus { #force-off-vbus data-toc-label="Force Off VBus" }

!!! warning "FAULT_CONTROL.ForceOffVBus (Optional)"
    `0b` :material-arrow-right-thin: Allow [STANDARD_INPUT_SIGNAL.ForceOffVBus] control.

    `1b` :material-arrow-right-thin: Block [STANDARD_INPUT_SIGNAL.ForceOffVBus] control.

    This enables or disables the [STANDARD_INPUT_SIGNAL] Force Off VBus functionality for debug purposes.

    Required if [STANDARD_INPUT_CAPABILITIES.ForceOffVBUS]=`1b`.

### `B3` VBus Discharge Fault Detection Timer { #vbus-discharge-fault-detection-timer data-toc-label="VBus Discharge Fault Detection Timer" }

!!! success "FAULT_CONTROL.VBusDischargeFaultDetectionTimer (Required)"
    `0b` :material-arrow-right-thin: VBus Discharge Fault Detection Timer enabled.

    `1b` :material-arrow-right-thin: VBus Discharge Fault Detection Timer disabled.

    This enables the timers for both [FAULT_STATUS.AutoDischargeFailed] and [FAULT_STATUS.ForceDischargeFailed].

### `B2` VBus Over Current Protection Fault { #vbus-over-current-protection-fault data-toc-label="VBus Over Current Protection Fault" }

!!! warning "FAULT_CONTROL.InternalOrExternalOCPFault (Optional)"
    `0b` :material-arrow-right-thin: Internal and External OCP circuit enabled.

    `1b` :material-arrow-right-thin: Internal and External OCP circuit disabled.

    Required if [DEVICE_CAPABILITIES_1.VBusOCPReporting]=`1b`.

### `B1` VBus Over Voltage Protection Fault { #vbus-over-voltage-protection-fault data-toc-label="VBus Over Voltage Protection Fault" }

!!! warning "FAULT_CONTROL.InternalOrExternalOVPFault (Optional)"
    `0b` :material-arrow-right-thin: Internal and External OVP circuit enabled.

    `1b` :material-arrow-right-thin: Internal and External OVP circuit disabled.

    Required if [DEVICE_CAPABILITIES_1.VBusOVPReporting]=`1b`.

### `B0` VConn Over Current Fault { #vconn-over-current-fault data-toc-label="VConn Over Current Fault" }

!!! warning "FAULT_CONTROL.VConnOverCurrentFault (Optional)"
    `0b` :material-arrow-right-thin: Fault detection circuit enabled.

    `1b` :material-arrow-right-thin: Fault detection circuit disabled.

    Required if [DEVICE_CAPABILITIES_2.VConnOvercurrentFaultCapable]=`1b`.
