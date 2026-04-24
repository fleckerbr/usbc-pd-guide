# Looking4Connection

This state encompases the functionality of the `Unattached.SNK` and `Unattached.SRC` states from the [USB TC] Specification.

## State Requirements

Upon entry into this state the TCPM shall perform the following actions:

1. Set [ROLE_CONTROL] to your perferred default configuration if the previous state was not [AttachWait.SNK] or [AttachWait.SRC]
    - Set [ROLE_CONTROL.DRP]=`1b` if the port can both sink and source power
    - Set [ROLE_CONTROL.CC1]=[ROLE_CONTROL.CC2]=`01b` to advertise power sourcing capabilities by default
    - Set [ROLE_CONTROL.CC1]=[ROLE_CONTROL.CC2]=`10b` to advertise power sinking capabilities by default
2. Write [COMMAND.Look4Connection]

While in this state the TCPM shall not drive VBus or VConn.

## Relevant Alerts

??? info "Alert List"
    - [ ] [ALERT.VendorDefinedAlert]
    - [ ] [ALERT.AlertExtended]
        - [ ] [ALERT_EXTENDED.TimerExpired]
        - [ ] [ALERT_EXTENDED.SourceFRSwap]
        - [ ] [ALERT_EXTENDED.SinkFRSwap]
    - [ ] [ALERT.ExtendedStatus]
        - [ ] [EXTENDED_STATUS.vSafe0V]
    - [ ] [ALERT.RxBeginningStatus]
    - [ ] [ALERT.VBusSinkDisconnectDetected]
    - [ ] [ALERT.RxBufferOverflow]
    - [ ] [ALERT.Fault]
        - [ ] [FAULT_STATUS.AllRegistersResetToDefault]
        - [ ] [FAULT_STATUS.ForceOffVBus]
        - [ ] [FAULT_STATUS.AutoDischargeFailed]
        - [ ] [FAULT_STATUS.ForceDischargeFailed]
        - [ ] [FAULT_STATUS.InternalOrExternalOCP]
        - [ ] [FAULT_STATUS.InternalOrExternalOVP]
        - [ ] [FAULT_STATUS.VConnOverCurrentFault]
        - [ ] [FAULT_STATUS.I2CInterfaceError]
    - [ ] [ALERT.VBusVoltageAlarmLo]
    - [ ] [ALERT.VBusVoltageAlarmHi]
    - [ ] [ALERT.TxMessageSuccessful]
    - [ ] [ALERT.TxMessageDiscarded]
    - [ ] [ALERT.TxMessageFailed]
    - [ ] [ALERT.HardReset]
    - [ ] [ALERT.RxStatus]
    - [ ] [ALERT.PowerStatus]
        - [ ] [POWER_STATUS.DebugAccessoryConnected]
        - [ ] [POWER_STATUS.TCPCInitializationStatus]
        - [ ] [POWER_STATUS.SourcingNondefaultVoltage]
        - [ ] [POWER_STATUS.SourcingVBus]
        - [ ] [POWER_STATUS.VBusDetectionEnabled]
        - [ ] [POWER_STATUS.VBusPresent]
        - [ ] [POWER_STATUS.VConnPresent]
        - [ ] [POWER_STATUS.SinkingVBus]
    - [x] [ALERT.CCStatus]

**ALERT.CCStatus**

:   Whenever this alert is asserted, read [CC_STATUS] to determine which state to enter next.

## State Transitions

**AttachWait.SNK**

:   The TCPC shall enter [AttachWait.SNK] if it is no longer looking for a connection ([CC_STATUS.Looking4Connection]=`0b`)
    and `SRC.Rp` is detected on either CC pin ([CC_STATUS.CC1State]=`SRC.Rp` or [CC_STATUS.CC2State]=`SRC.Rp`).

**AttachWait.SRC**

:   The TCPC shall enter [AttachWait.SRC] if it is no longer looking for a connection ([CC_STATUS.Looking4Connection]=`0b`)
    and `SRC.Rd` is detected on either CC pin ([CC_STATUS.CC1State]=`SRC.Rd` or [CC_STATUS.CC2State]=`SRC.Rd`).
