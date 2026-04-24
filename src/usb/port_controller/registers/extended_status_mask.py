from __future__ import annotations

from usb.port_controller import B, Field, Register


class ExtendedStatusMask(Register):
    __address__ = 0x16
    __alias__ = "Extended Status Mask"
    __identifier__ = "EXTENDED_STATUS_MASK"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7, 1),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b0000000,
        required=True,
    )
    VSAFE0V_STATUS_MASK = Field(
        bits=B(0),
        alias="vSafe0V Status Mask",
        identifier="vSafe0VStatusMask",
        reset=0b1,
        required=True,
    )
