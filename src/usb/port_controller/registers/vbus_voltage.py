from __future__ import annotations

from usb.port_controller import B, Field, Register


class VBusVoltage(Register):
    __address__ = 0x70
    __alias__ = "VBus Voltage"
    __identifier__ = "VBUS_VOLTAGE"
    __readable__ = True
    __writable__ = False

    RESERVED_15 = Field(
        bits=B(15, 12),
        alias="Reserved",
        identifier="Reserved15",
        reset=0b0000,
        required=True,
    )
    SCALE_FACTOR = Field(
        bits=B(11, 10),
        alias="Scale Factor",
        identifier="ScaleFactor",
        reset=0b00,
        required=True,
    )
    VBUS_VOLTAGE_MEASUREMENT = Field(
        bits=B(9, 0),
        alias="VBus Voltage Measurement",
        identifier="VBusVoltageMeasurement",
        reset=0b0000000000,
        required=True,
    )
