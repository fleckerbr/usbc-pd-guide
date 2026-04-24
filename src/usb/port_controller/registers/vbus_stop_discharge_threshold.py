from __future__ import annotations

from usb.port_controller import B, Field, Register


class VBusStopDischargeThreshold(Register):
    __address__ = 0x74
    __alias__ = "VBus Stop Discharge Threshold"
    __identifier__ = "VBUS_STOP_DISCHARGE_THRESHOLD"
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
        reset=0b000000100000,
        required=True,
    )
