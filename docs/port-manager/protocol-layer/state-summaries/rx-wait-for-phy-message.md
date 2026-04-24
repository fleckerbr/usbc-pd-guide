# Rx.WaitForPHYMessage

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
    - [x] [ALERT.RxStatus]
    - [ ] [ALERT.PowerStatus]
        - [ ] [POWER_STATUS.DebugAccessoryConnected]
        - [ ] [POWER_STATUS.TCPCInitializationStatus]
        - [ ] [POWER_STATUS.SourcingNondefaultVoltage]
        - [ ] [POWER_STATUS.SourcingVBus]
        - [ ] [POWER_STATUS.VBusDetectionEnabled]
        - [ ] [POWER_STATUS.VBusPresent]
        - [ ] [POWER_STATUS.VConnPresent]
        - [ ] [POWER_STATUS.SinkingVBus]
    - [ ] [ALERT.CCStatus]

## State Behavior

!!! quote ""
    Refer to `Section 6.9.2.2.1` `PRL_Rx_Wait_for_PHY_Message state` of the [USB PD R3.2] Specification and `Figure A-1` `Message Reception State Diagram Implemented in TCPM` of the [USB TCPCI R2.0 V1.3] Specification for more details.

This state shall be entered upon system startup, after receiving a Soft Reset from the Policy Engine, or after exiting from a Hard Reset event, and upon entry no actions are required.

When the TCPC replies to an incoming message a GoodCRC response [ALERT.RxStatus] will be asserted.
Once [Alert.RxStatus] is detected, the alert shall be cleared and the Rx state machine shall transition to the [Rx.CheckMessageType](./rx-check-message-type.md) state.
