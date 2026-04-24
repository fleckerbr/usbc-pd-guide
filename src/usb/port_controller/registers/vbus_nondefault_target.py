from __future__ import annotations

from usb.port_controller import B, Field, Register


class VBusNondefaultTarget(Register):
    __address__ = 0x7A
    __alias__ = "VBus Nondefault Target"
    __identifier__ = "VBUS_NONDEFAULT_TARGET"
    __readable__ = True
    __writable__ = True

    VBUS_NONDEFAULT_VOLTAGE_TARGET = Field(
        bits=B(15, 0),
        alias="VBus Nondefault Voltage Target",
        identifier="VBusNondefaultVoltageTarget",
        reset=0b0000000000000000,
        required=True,
    )
