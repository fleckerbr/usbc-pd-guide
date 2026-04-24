from __future__ import annotations

from usb.port_controller import B, Field, Register


class GenericTimer(Register):
    __address__ = 0x2C
    __alias__ = "Generic Timer"
    __identifier__ = "GENERIC_TIMER"
    __readable__ = False
    __writable__ = True

    GENERIC_TIMER = Field(
        bits=B(15, 0),
        alias="Generic Timer",
        identifier="GenericTimer",
        reset=0b0000000000000000,
        required=True,
    )
