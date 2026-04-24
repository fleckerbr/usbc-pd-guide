from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class ExtendedStatus(Register):
    __address__ = 0x20
    __alias__ = "Extended Status"
    __identifier__ = "EXTENDED_STATUS"
    __readable__ = True
    __writable__ = False

    RESERVED_7 = Field(
        bits=B(7, 1),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b0000000,
        required=True,
    )
    VSAFE0V = Field(
        bits=B(0),
        alias="vSafe0V",
        identifier="vSafe0V",
        reset=Reset.UNDEFINED,
        required=True,
    )
