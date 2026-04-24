from __future__ import annotations

from usb.port_controller import B, Field, Register


class AlertMask(Register):
    __address__ = 0x12
    __alias__ = "Alert Mask"
    __identifier__ = "ALERT_MASK"
    __readable__ = True
    __writable__ = True

    VENDOR_DEFINED_ALERT_MASK = Field(
        bits=B(15),
        alias="Vendor Defined Alert Mask",
        identifier="VendorDefinedAlertMask",
        reset=0b0,
        required=True,
    )
    ALERT_EXTENDED_MASK = Field(
        bits=B(14),
        alias="Alert Extended Mask",
        identifier="AlertExtendedMask",
        reset=0b1,
        required=True,
    )
    EXTENDED_STATUS_MASK = Field(
        bits=B(13),
        alias="Extended Status Mask",
        identifier="ExtendedStatusMask",
        reset=0b1,
        required=True,
    )
    RX_BEGINNING_STATUS_MASK = Field(
        bits=B(12),
        alias="Beginning SOP* Message Status Mask",
        identifier="RxBeginningStatusMask",
        reset=0b1,
        required=True,
    )
    VBUS_SINK_DISCONNECT_DETECTED_MASK = Field(
        bits=B(11),
        alias="VBus Sink Disconnect Detected Mask",
        identifier="VBusSinkDisconnectDetectedMask",
        reset=0b1,
        required=True,
    )
    RX_BUFFER_OVERFLOW_MASK = Field(
        bits=B(10),
        alias="Receive Buffer Overflow Mask",
        identifier="RxBufferOverflowMask",
        reset=0b1,
        required=True,
    )
    FAULT_MASK = Field(
        bits=B(9),
        alias="Fault Mask",
        identifier="FaultMask",
        reset=0b1,
        required=True,
    )
    VBUS_VOLTAGE_ALARM_LOW_MASK = Field(
        bits=B(8),
        alias="VBus Voltage Alarm Low Mask",
        identifier="VBusVoltageAlarmLowMask",
        reset=0b1,
        required=True,
    )
    VBUS_VOLTAGE_ALARM_HIGH_MASK = Field(
        bits=B(7),
        alias="VBus Voltage Alarm High Mask",
        identifier="VBusVoltageAlarmHighMask",
        reset=0b1,
        required=True,
    )
    TX_MESSAGE_SUCCESSFUL_MASK = Field(
        bits=B(6),
        alias="Transmit SOP* Message Successful Mask",
        identifier="TxMessageSuccessfulMask",
        reset=0b1,
        required=True,
    )
    TX_MESSAGE_DISCARDED_MASK = Field(
        bits=B(5),
        alias="Transmit SOP* Message Discarded Mask",
        identifier="TxMessageDiscardedMask",
        reset=0b1,
        required=True,
    )
    TX_MESSAGE_FAILED_MASK = Field(
        bits=B(4),
        alias="Transmit SOP* Message Failed Mask",
        identifier="TxMessageFailedMask",
        reset=0b1,
        required=True,
    )
    HARD_RESET_MASK = Field(
        bits=B(3),
        alias="Received Hard Reset Mask",
        identifier="HardResetMask",
        reset=0b1,
        required=True,
    )
    RX_STATUS_MASK = Field(
        bits=B(2),
        alias="Received SOP* Message Status Mask",
        identifier="RxStatusMask",
        reset=0b1,
        required=True,
    )
    POWER_STATUS_MASK = Field(
        bits=B(1),
        alias="Power Status Mask",
        identifier="PowerStatusMask",
        reset=0b1,
        required=True,
    )
    CC_STATUS_MASK = Field(
        bits=B(0),
        alias="CC Status Mask",
        identifier="CCStatusMask",
        reset=0b1,
        required=True,
    )
