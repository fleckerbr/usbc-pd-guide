# STANDARD_INPUT_SIGNAL

## Description

Support for any of these signals shall be declared in the [STANDARD_INPUT_CAPABILITIES] register.
This section defines the [STANDARD_INPUT_SIGNAL] to the TCPC.
Some of the input signals provide updates to the [FAULT_STATUS] register.
The TCPC shall set the [FAULT_STATUS] or [ALERT_EXTENDED] register based on the input level at the pin.

## Input Signals

### VBus External Over Current Fault

!!! abstract "STANDARD_INPUT_SIGNAL.VBusExternalOverCurrentFault"
    `Low` :material-arrow-right-thin: Set [STANDARD_INPUT] Register to 0.
    
    :   No Over Current Fault.
        
    `High` :material-arrow-right-thin: Set [STANDARD_INPUT] Register to 1.

    :   Over Current Fault present reported in [FAULT_STATUS.InternalOrExternalOCP].

### VBus External Over Voltage Fault

!!! abstract "STANDARD_INPUT_SIGNAL.VBusExternalOverVoltageFault"
    `Low` :material-arrow-right-thin: Set [STANDARD_INPUT] Register to 0.
    
    :   No Over Voltage Fault.
        
    `High` :material-arrow-right-thin: Set [STANDARD_INPUT] Register to 1.

    :   Over Voltage Fault present. Reported in [FAULT_STATUS.InternalOrExternalOVP].

### Force Off VBus

!!! abstract "STANDARD_INPUT_SIGNAL.ForceOffVBus"
    `Low` :material-arrow-right-thin: Set [STANDARD_INPUT] Register to 0.
    
    :   Do not force VBus off.
        
    `High` :material-arrow-right-thin: Set [STANDARD_INPUT] Register to 1.

    :   Force VBus off. Reported in [FAULT_STATUS.ForceOffVBus].

### Source Fast Role Swap

!!! abstract "STANDARD_INPUT_SIGNAL.SourceFastRoleSwap"
    `High` :material-arrow-right-thin: `Low` :material-arrow-right-thin: Send Fast Role Swap signal within tTCPCSendFRSwap.
    
    :   TCPC shall generate a bit-level NAK to the I2C write and then assert [FAULT_STATUS.I2CInterfaceError]
        when TCPC is transmitting the Fast Role Swap signal (as triggered by the [STANDARD_INPUT_SIGNAL]).
        
    `Low` :material-arrow-right-thin: `High` :material-arrow-right-thin: Reset.

    :   Reported in [ALERT_EXTENDED.SourceFRSwap].
