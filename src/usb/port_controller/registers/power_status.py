from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class PowerStatus(Register):
    __address__ = 0x1E
    __alias__ = "Power Status"
    __identifier__ = "POWER_STATUS"
    __readable__ = True
    __writable__ = False

    DEBUG_ACCESSORY_CONNECTED = Field(
        bits=B(7),
        alias="Debug Accessory Connected",
        identifier="DebugAccessoryConnected",
        reset=Reset.UNDEFINED,
        required=False,
    )
    TCPC_INITIALIZATION_STATUS = Field(
        bits=B(6),
        alias="TCPC Initialization Status",
        identifier="TCPCInitializationStatus",
        reset=Reset.UNDEFINED,
        required=True,
    )
    SOURCING_NONDEFAULT_VOLTAGE = Field(
        bits=B(5),
        alias="Sourcing Nondefault Voltage",
        identifier="SourcingNondefaultVoltage",
        reset=Reset.UNDEFINED,
        required=False,
    )
    SOURCING_VBUS = Field(
        bits=B(4),
        alias="Sourcing VBus",
        identifier="SourcingVBus",
        reset=Reset.UNDEFINED,
        required=True,
    )
    VBUS_DETECTION_ENABLED = Field(
        bits=B(3),
        alias="VBus Detection Enabled",
        identifier="VBusDetectionEnabled",
        reset=Reset.UNDEFINED,
        required=True,
    )
    VBUS_PRESENT = Field(
        bits=B(2),
        alias="VBus Present",
        identifier="VBusPresent",
        reset=Reset.UNDEFINED,
        required=True,
    )
    VCONN_PRESENT = Field(
        bits=B(1),
        alias="VConn Present",
        identifier="VConnPresent",
        reset=Reset.UNDEFINED,
        required=True,
    )
    SINKING_VBUS = Field(
        bits=B(0),
        alias="Sinking VBus",
        identifier="SinkingVBus",
        reset=Reset.UNDEFINED,
        required=True,
    )
