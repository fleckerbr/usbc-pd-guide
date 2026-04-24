from __future__ import annotations

from usb.port_controller import B, Field, Register


class Alert(Register):
    __address__ = 0x10
    __alias__ = "Alert"
    __identifier__ = "ALERT"
    __readable__ = True
    __writable__ = True

    VENDOR_DEFINED_ALERT = Field(
        bits=B(15),
        alias="Vendor Defined Alert",
        identifier="VendorDefinedAlert",
        reset=0b0,
        required=True,
    )
    ALERT_EXTENDED = Field(
        bits=B(14),
        alias="Alert Extended",
        identifier="AlertExtended",
        reset=0b0,
        required=True,
    )
    EXTENDED_STATUS = Field(
        bits=B(13),
        alias="Extended Status",
        identifier="ExtendedStatus",
        reset=0b0,
        required=True,
    )
    RX_BEGINNING_STATUS = Field(
        bits=B(12),
        alias="Beginning SOP* Message Status",
        identifier="RxBeginningStatus",
        reset=0b0,
        required=True,
    )
    VBUS_SINK_DISCONNECT_DETECTED = Field(
        bits=B(11),
        alias="VBus Sink Disconnect Detected",
        identifier="VBusSinkDisconnectDetected",
        reset=0b0,
        required=True,
    )
    RX_BUFFER_OVERFLOW = Field(
        bits=B(10),
        alias="Receive Buffer Overflow",
        identifier="RxBufferOverflow",
        reset=0b0,
        required=True,
    )
    FAULT = Field(
        bits=B(9),
        alias="Fault",
        identifier="Fault",
        reset=0b0,
        required=True,
    )
    VBUS_VOLTAGE_ALARM_LO = Field(
        bits=B(8),
        alias="VBus Voltage Alarm Low",
        identifier="VBusVoltageAlarmLo",
        reset=0b0,
        required=True,
    )
    VBUS_VOLTAGE_ALARM_HI = Field(
        bits=B(7),
        alias="VBus Voltage Alarm High",
        identifier="VBusVoltageAlarmHi",
        reset=0b0,
        required=True,
    )
    TX_MESSAGE_SUCCESSFUL = Field(
        bits=B(6),
        alias="Transmit SOP* Message Successful",
        identifier="TxMessageSuccessful",
        reset=0b0,
        required=True,
    )
    TX_MESSAGE_DISCARDED = Field(
        bits=B(5),
        alias="Transmit SOP* Message Discarded",
        identifier="TxMessageDiscarded",
        reset=0b0,
        required=True,
    )
    TX_MESSAGE_FAILED = Field(
        bits=B(4),
        alias="Transmit SOP* Message Failed",
        identifier="TxMessageFailed",
        reset=0b0,
        required=True,
    )
    HARD_RESET = Field(
        bits=B(3),
        alias="Received Hard Reset",
        identifier="HardReset",
        reset=0b0,
        required=True,
    )
    RX_STATUS = Field(
        bits=B(2),
        alias="Received SOP* Message Status",
        identifier="RxStatus",
        reset=0b0,
        required=True,
    )
    POWER_STATUS = Field(
        bits=B(1),
        alias="Power Status",
        identifier="PowerStatus",
        reset=0b0,
        required=True,
    )
    CC_STATUS = Field(
        bits=B(0),
        alias="CC Status",
        identifier="CCStatus",
        reset=0b0,
        required=True,
    )
