from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class StandardInputCapabilities(Register):
    __address__ = 0x28
    __alias__ = "Standard Input Capabilities"
    __identifier__ = "STANDARD_INPUT_CAPABILITIES"
    __readable__ = True
    __writable__ = False

    RESERVED_15 = Field(
        bits=B(15, 5),
        alias="Reserved",
        identifier="Reserved15",
        reset=0b00000000000,
        required=True,
    )
    SOURCE_FAST_ROLE_SWAP = Field(
        bits=B(4, 3),
        alias="Source Fast Role Swap",
        identifier="SourceFastRoleSwap",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_EXTERNAL_OVER_VOLTAGE_FAULT = Field(
        bits=B(2),
        alias="VBus External Over Voltage Fault",
        identifier="VBusExternalOverVoltageFault",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_EXTERNAL_OVER_CURRENT_FAULT = Field(
        bits=B(1),
        alias="VBus External Over Current Fault",
        identifier="VBusExternalOverCurrentFault",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    FORCE_OFF_VBUS = Field(
        bits=B(0),
        alias="Force Off VBus",
        identifier="ForceOffVBus",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
