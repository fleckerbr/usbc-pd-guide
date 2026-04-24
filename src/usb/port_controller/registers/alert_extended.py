from __future__ import annotations

from usb.port_controller import B, Field, Register


class AlertExtended(Register):
    __address__ = 0x21
    __alias__ = "Alert Extended"
    __identifier__ = "ALERT_EXTENDED"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7, 3),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b00000,
        required=True,
    )
    TIMER_EXPIRED = Field(
        bits=B(2),
        alias="Timer Expired",
        identifier="TimerExpired",
        reset=0b0,
        required=True,
    )
    SOURCE_FR_SWAP = Field(
        bits=B(1),
        alias="Source Fast Role Swap",
        identifier="SourceFRSwap",
        reset=0b0,
        required=True,
    )
    SINK_FR_SWAP = Field(
        bits=B(0),
        alias="Sink Fast Role Swap",
        identifier="SinkFRSwap",
        reset=0b0,
        required=True,
    )
