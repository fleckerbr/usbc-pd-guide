from __future__ import annotations

from usb.port_controller import B, Field, Register


class PowerStatusMask(Register):
    __address__ = 0x14
    __alias__ = "Power Status Mask"
    __identifier__ = "POWER_STATUS_MASK"
    __readable__ = True
    __writable__ = True

    DEBUG_ACCESSORY_CONNECTED_MASK = Field(
        bits=B(7),
        alias="Debug Accessory Connected Status Mask",
        identifier="DebugAccessoryConnectedMask",
        reset=0b1,
        required=True,
    )
    TCPC_INITIALIZATION_MASK = Field(
        bits=B(6),
        alias="TCPC Initialization Status Mask",
        identifier="TCPCInitializationMask",
        reset=0b1,
        required=True,
    )
    SOURCING_NONDEFAULT_VOLTAGE_MASK = Field(
        bits=B(5),
        alias="Sourcing Nondefault Voltage Status Interrupt Mask",
        identifier="SourcingNondefaultVoltageMask",
        reset=0b1,
        required=True,
    )
    SOURCING_VBUS_MASK = Field(
        bits=B(4),
        alias="Sourcing VBus Status Interrupt Mask",
        identifier="SourcingVBusMask",
        reset=0b1,
        required=True,
    )
    VBUS_DETECTION_MASK = Field(
        bits=B(3),
        alias="VBus Detection Status Interrupt Mask",
        identifier="VBusDetectionMask",
        reset=0b1,
        required=True,
    )
    VBUS_PRESENT_MASK = Field(
        bits=B(2),
        alias="VBus Present Status Interrupt Mask",
        identifier="VBusPresentMask",
        reset=0b1,
        required=True,
    )
    VCONN_PRESENT_MASK = Field(
        bits=B(1),
        alias="VConn Present Status Interrupt Mask",
        identifier="VConnPresentMask",
        reset=0b1,
        required=True,
    )
    SINKING_VBUS_MASK = Field(
        bits=B(0),
        alias="Sinking VBus Status Interrupt Mask",
        identifier="SinkingVBusMask",
        reset=0b1,
        required=True,
    )
