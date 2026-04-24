from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class CCStatus(Register):
    __address__ = 0x1D
    __alias__ = "CC Status"
    __identifier__ = "CC_STATUS"
    __readable__ = True
    __writable__ = False

    RESERVED_7 = Field(
        bits=B(7, 6),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b00,
        required=True,
    )
    LOOKING4_CONNECTION = Field(
        bits=B(5),
        alias="Looking4Connection",
        identifier="Looking4Connection",
        reset=Reset.UNDEFINED,
        required=True,
    )
    CONNECT_RESULT = Field(
        bits=B(4),
        alias="Connect Result",
        identifier="ConnectResult",
        reset=Reset.UNDEFINED,
        required=True,
    )
    CC2_STATE = Field(
        bits=B(3, 2),
        alias="CC2 State",
        identifier="CC2State",
        reset=Reset.UNDEFINED,
        required=True,
    )
    CC1_STATE = Field(
        bits=B(1, 0),
        alias="CC1 State",
        identifier="CC1State",
        reset=Reset.UNDEFINED,
        required=True,
    )
