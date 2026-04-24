from __future__ import annotations

from usb.port_controller import B, Field, Register


class TransmitBuffer(Register):
    __address__ = 0x51
    __alias__ = "Transmit Buffer"
    __identifier__ = "TRANSMIT_BUFFER"
    __readable__ = True
    __writable__ = True

    BYTE = Field(
        bits=B(15, 0),
        alias="Byte",
        identifier="Byte",
        reset=0b0000000000000000,
        required=True,
    )
