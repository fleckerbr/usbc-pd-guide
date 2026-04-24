from __future__ import annotations

from usb.port_controller import B, Field, Register


class ConfigureExtended1(Register):
    __address__ = 0x2A
    __alias__ = "Configure Extended 1"
    __identifier__ = "CONFIGURE_EXTENDED_1"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7, 2),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b000000,
        required=True,
    )
    FR_SWAP_BIDIRECTIONAL_PIN = Field(
        bits=B(1),
        alias="FR Swap Bidirectional Pin",
        identifier="FRSwapBidirectionalPin",
        reset=0b0,
        required=True,
    )
    STANDARD_INPUT_SOURCE_FR_SWAP = Field(
        bits=B(0),
        alias="Standard Input Source FR Swap",
        identifier="StandardInputSourceFRSwap",
        reset=0b0,
        required=True,
    )
