from __future__ import annotations

from usb.port_controller import B, Field, Register


class ReceiveBuffer(Register):
    __address__ = 0x30
    __alias__ = "Receive Buffer"
    __identifier__ = "RECEIVE_BUFFER"
    __readable__ = True
    __writable__ = True

    BYTE = Field(
        bits=B(7, 0),
        alias="Byte",
        identifier="Byte",
        reset=0b00000000,
        required=True,
    )
