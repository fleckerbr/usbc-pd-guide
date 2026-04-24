from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class RoleControl(Register):
    __address__ = 0x1A
    __alias__ = "Role Control"
    __identifier__ = "ROLE_CONTROL"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b0,
        required=True,
    )
    DRP = Field(
        bits=B(6),
        alias="DRP",
        identifier="DRP",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
    RP_VALUE = Field(
        bits=B(5, 4),
        alias="Rp Value",
        identifier="RpValue",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
    CC2 = Field(
        bits=B(3, 2),
        alias="CC2",
        identifier="CC2",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
    CC1 = Field(
        bits=B(1, 0),
        alias="CC1",
        identifier="CC1",
        reset=Reset.CAPABILITY_DEFINED,
        required=True,
    )
