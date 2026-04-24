# PowerOnReset

Whenever the TCPM/TCPC is powered on or reset, the Configuration Channel state machine ***shall*** enter the [PowerOnReset] state.
The [USB TC] Specification does not define a CC state that is equivalent to [PowerOnReset] as this is an implementation-specific state.

## State Requirements

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
    - [x] [ALERT.Fault]
        - [x] [FAULT_STATUS.AllRegistersResetToDefault]
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
    - [x] [ALERT.PowerStatus]
        - [ ] [POWER_STATUS.DebugAccessoryConnected]
        - [x] [POWER_STATUS.TCPCInitializationStatus]
        - [ ] [POWER_STATUS.SourcingNondefaultVoltage]
        - [ ] [POWER_STATUS.SourcingVBus]
        - [ ] [POWER_STATUS.VBusDetectionEnabled]
        - [ ] [POWER_STATUS.VBusPresent]
        - [ ] [POWER_STATUS.VConnPresent]
        - [ ] [POWER_STATUS.SinkingVBus]
    - [ ] [ALERT.CCStatus]

**FAULT_STATUS.AllRegistersResetToDefault**

:   If this fault is asserted, perform any setup operations that are required by your TCPC.
    Generally this would include setting any [VENDOR_DEFINED] registers if your system relies on any non-default configurations.

    Additionally, if your TCPM caches any TCPC register values, they should be reset at this time.

    This flag shall be cleared once the TCPC has been reconfigured and cached register values have been reset.

**POWER_STATUS.TCPCInitializationStatus**

:   This alert is used to determine when to transition to the next state.

## State Transitions

**Looking4Connection**

:   The port shall transition to [Looking4Connection] if the TCPC has finished initialization ([POWER_STATUS.TCPCInitializationStatus]=`0b`)
    and there are no unhandled alerts ([Alert#] is not asserted).
