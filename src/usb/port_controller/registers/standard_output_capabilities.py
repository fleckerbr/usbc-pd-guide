from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class StandardOutputCapabilities(Register):
    __address__ = 0x29
    __alias__ = "Standard Output Capabilities"
    __identifier__ = "STANDARD_OUTPUT_CAPABILITIES"
    __readable__ = True
    __writable__ = False

    VBUS_SINK_DISCONNECT_DETECT_INDICATOR = Field(
        bits=B(7),
        alias="VBus Sink Disconnect Detect Indicator",
        identifier="VBusSinkDisconnectDetectIndicator",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    DEBUG_ACCESSORY_INDICATOR = Field(
        bits=B(6),
        alias="Debug Accessory Indicator",
        identifier="DebugAccessoryIndicator",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_PRESENT_MONITOR = Field(
        bits=B(5),
        alias="VBus Present Monitor",
        identifier="VBusPresentMonitor",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    AUDIO_ADAPTER_ACCESSORY_INDICATOR = Field(
        bits=B(4),
        alias="Audio Adapter Accessory Indicator",
        identifier="AudioAdapterAccessoryIndicator",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    ACTIVE_CABLE_INDICATOR = Field(
        bits=B(3),
        alias="Active Cable Indicator",
        identifier="ActiveCableIndicator",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    MUX_CONFIGURATION_CONTROL = Field(
        bits=B(2),
        alias="MUX Configuration Control",
        identifier="MUXConfigurationControl",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    CONNECTION_PRESENT = Field(
        bits=B(1),
        alias="Connection Present",
        identifier="ConnectionPresent",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    CONNECTOR_ORIENTATION = Field(
        bits=B(0),
        alias="Connector Orientation",
        identifier="ConnectorOrientation",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
