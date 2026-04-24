# AttachWait.SNK

While in the [AttachWait.SNK] state, the port has detected the SNK.Rp state on at least one of its CC pins and is waiting for VBus.

## Timing Parameters

| Parameter     | Minimum   | Maximum   |
| :-----------: | :-------: | :-------: |
| tCCDebounce   | 100 ms    | 200 ms    |
| tPDDebounce   | 10 ms     | 20 ms     |

## Relevant Alerts

??? info "Alert List"
    - [ ] [ALERT.VendorDefinedAlert]
    - [x] [ALERT.AlertExtended]
        - [x] [ALERT_EXTENDED.TimerExpired]
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
    - [x] [ALERT.PowerStatus]
        - [ ] [POWER_STATUS.DebugAccessoryConnected]
        - [ ] [POWER_STATUS.TCPCInitializationStatus]
        - [ ] [POWER_STATUS.SourcingNondefaultVoltage]
        - [ ] [POWER_STATUS.SourcingVBus]
        - [x] [POWER_STATUS.VBusDetectionEnabled]
        - [x] [POWER_STATUS.VBusPresent]
        - [ ] [POWER_STATUS.VConnPresent]
        - [x] [POWER_STATUS.SinkingVBus]
    - [x] [ALERT.CCStatus]

## State Behavior

!!! quote ""
    Refer to `Section 4.5.2.6` `Connection States Summary` of the [USB TC R2.3] Specification and `Figure 4-24` `DRP Initialization and Connection Detection` of the [USB TCPCI R2.0 V1.3] Specification for more details.

!!! warning inline end "GENERIC_TIMER Support"
    Since the [GENERIC_TIMER] register is not required on all TCPCs, it may be necessary to replace it with an external timer.

Upon entry into this state the TCPM shall write [tCCDebounce](#timing-parameters) (minimum) to [GENERIC_TIMER] and clear [ALERT.CCStatus].
If the port is not a USB 3.2 SuperSpeed device then the TCPM shall also write [COMMAND.EnableVBusDetect].

The [USB TC] Specification recommends holding off VBus detection until at least one CC pin is in the SNK.Rp state for USB 3.2 SuperSpeed devices
since they may otherwise connect as a USB 2.0 device when attached to a legacy host or hub's DFP.

!!! tip "Masking [ALERT.PowerStatus]"
    When enabling VBus detection it may be convenient to silence [ALERT.PowerStatus] since it does not need to be checked until [ALERT_EXTENDED.TimerExpired] is asserted.

If [ALERT.CCStatus] is asserted while waiting on [ALERT_EXTENDED.TimerExpired], check if the state of CC1 and CC2 pins is SNK.Open.
If both pins are in the SNK.Open state, write [tPDDebounce](#timing-parameters) (minimum) to [GENERIC_TIMER] and clear [ALERT.CCStatus].[^1]
This may be the result of the port partner attempting to initiate USB PD communications and shall be debounced to verify whether it is a disconnect or not.

If one of the CC pins is showing SNK.Rp when [ALERT_EXTENDED.TimerExpired] is asserted restart [tCCDebounce](#timing-parameters) (minimum) on the [GENERIC_TIMER].

Once [tCCDebounce](#timing-parameters) expires, verify that one CC pin detects Rp and set [ROLE_CONTROL] and [TCPC_CONTROL] accordingly:

- Set [ROLE_CONTROL.DRP]=`0b`
- If [CC_STATUS.CC1State]=SNK.Rp
    - Set [ROLE_CONTROL.CC1]=`10b`(Rd)
    - Set [ROLE_CONTROL.CC2]=`00b`(Ra)
    - Set [TCPC_CONTROL.PlugOrientation]=`0b`(Use CC2 for VConn)
- If [CC_STATUS.CC2State]=SNK.Rp
    - Set [ROLE_CONTROL.CC1]=`00b`(Ra)
    - Set [ROLE_CONTROL.CC2]=`10b`(Rd)
    - Set [TCPC_CONTROL.PlugOrientation]=`1b`(Use CC1 for VConn)

After [ROLE_CONTROL] and [TCPC_CONTROL] have been successfully configured, set [POWER_CONTROL.AutoDischargeDisconnect]=`1b` and [POWER_CONTROL.EnableVConn]=`1b`.

At this point it is safe to write [COMMAND.EnableVBusDetect] if it was not done earlier and voltage monitoring can be enabled on
devices with [DEVICE_CAPABILITIES_1.VBusMeasurementAndAlarmCapable]=`1b` by setting [POWER_CONTROL.VBusVoltageMonitor]=`0b`.

Sinking VBus can now be enabled by writing [COMMAND.SinkVBus] and if power routing is not handled by your TCPC,
your Device Policy Manager shall also configure your power system to sink VBus at this time.

Once VBus is detected by [POWER_STATUS.VBusPresent], the port shall transition to the [Attached.SNK] state.

[^1]: Refer to the [GENERIC_TIMER] description for details on how to safely update the timer.
