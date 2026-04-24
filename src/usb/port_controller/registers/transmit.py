from __future__ import annotations

from usb.port_controller import B, Field, Register


class Transmit(Register):
    __address__ = 0x50
    __alias__ = "Transmit"
    __identifier__ = "TRANSMIT"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7, 6),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b00,
        required=True,
    )
    RETRY_COUNTER = Field(
        bits=B(5, 4),
        alias="Retry Counter",
        identifier="RetryCounter",
        reset=0b00,
        required=True,
    )
    RESERVED_3 = Field(
        bits=B(3),
        alias="Reserved",
        identifier="Reserved3",
        reset=0b0,
        required=True,
    )
    TRANSMIT_SOP_MESSAGE = Field(
        bits=B(2, 0),
        alias="Transmit SOP* Message",
        identifier="TransmitSOP*Message",
        reset=0b000,
        required=True,
    )
