from __future__ import annotations

from usb.port_controller import B, Field, Register


class VBusVoltageAlarmLoCfg(Register):
    __address__ = 0x78
    __alias__ = "VBus Voltage Alarm Low Config"
    __identifier__ = "VBUS_VOLTAGE_ALARM_LO_CFG"
    __readable__ = True
    __writable__ = True

    RESERVED_15 = Field(
        bits=B(15, 12),
        alias="Reserved",
        identifier="Reserved15",
        reset=0b0000,
        required=True,
    )
    VOLTAGE_TRIP_POINT = Field(
        bits=B(11, 0),
        alias="Voltage Trip Point",
        identifier="VoltageTripPoint",
        reset=0b000000000000,
        required=True,
    )
