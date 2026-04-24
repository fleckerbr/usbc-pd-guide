from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class MessageHeaderInfo(Register):
    __address__ = 0x2E
    __alias__ = "Message Header Info"
    __identifier__ = "MESSAGE_HEADER_INFO"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7, 5),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b000,
        required=True,
    )
    CABLE_PLUG = Field(
        bits=B(4),
        alias="Cable Plug",
        identifier="CablePlug",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
    DATA_ROLE = Field(
        bits=B(3),
        alias="Data Role",
        identifier="DataRole",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
    USBPD_SPECIFICATION_REVISION = Field(
        bits=B(2, 1),
        alias="USB PD Specification Revision",
        identifier="USBPDSpecificationRevision",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
    POWER_ROLE = Field(
        bits=B(0),
        alias="Power Role",
        identifier="PowerRole",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
