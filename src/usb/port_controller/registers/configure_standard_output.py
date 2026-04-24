from __future__ import annotations

from usb.port_controller import B, Field, Register


class ConfigureStandardOutput(Register):
    __address__ = 0x18
    __alias__ = "Configure Standard Output"
    __identifier__ = "CONFIGURE_STANDARD_OUTPUT"
    __readable__ = True
    __writable__ = True

    HIGH_IMPEDANCE_OUTPUTS = Field(
        bits=B(7),
        alias="High Impedance Outputs",
        identifier="HighImpedanceOutputs",
        reset=0b0,
        required=False,
    )
    DEBUG_ACCESSORY_CONNECTED_N = Field(
        bits=B(6),
        alias="Debug Accessory Connected#",
        identifier="DebugAccessoryConnected#",
        reset=0b1,
        required=False,
    )
    AUDIO_ACCESSORY_CONNECTED_N = Field(
        bits=B(5),
        alias="Audio Accessory Connected#",
        identifier="AudioAccessoryConnected#",
        reset=0b1,
        required=False,
    )
    ACTIVE_CABLE_CONNECTED = Field(
        bits=B(4),
        alias="Active Cable Connected",
        identifier="ActiveCableConnected",
        reset=0b0,
        required=False,
    )
    MUX_CONTROL = Field(
        bits=B(3, 2),
        alias="MUX Control",
        identifier="MUXControl",
        reset=0b00,
        required=False,
    )
    CONNECTION_PRESENT = Field(
        bits=B(1),
        alias="Connection Present",
        identifier="ConnectionPresent",
        reset=0b0,
        required=False,
    )
    CONNECTOR_ORIENTATION = Field(
        bits=B(0),
        alias="Connector Orientation",
        identifier="ConnectorOrientation",
        reset=0b0,
        required=False,
    )
