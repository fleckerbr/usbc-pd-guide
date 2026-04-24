from __future__ import annotations

from usb.port_controller import B, Field, Register


class AlertExtendedMask(Register):
    __address__ = 0x17
    __alias__ = "Alert Extended Mask"
    __identifier__ = "ALERT_EXTENDED_MASK"
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
        reset=0b1,
        required=True,
    )
    SOURCE_FAST_ROLE_SWAP_MASK = Field(
        bits=B(1),
        alias="Source Fast Role Swap Mask",
        identifier="SourceFastRoleSwapMask",
        reset=0b1,
        required=True,
    )
    SINK_FAST_ROLE_SWAP_MASK = Field(
        bits=B(0),
        alias="Sink Fast Role Swap Mask",
        identifier="SinkFastRoleSwapMask",
        reset=0b1,
        required=True,
    )
