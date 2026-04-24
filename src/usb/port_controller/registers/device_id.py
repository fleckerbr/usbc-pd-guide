from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class DeviceID(Register):
    __address__ = 0x04
    __alias__ = "Device ID"
    __identifier__ = "DEVICE_ID"
    __readable__ = True
    __writable__ = False

    BCD_DEVICE = Field(
        bits=B(15, 0),
        alias="bcd Device",
        identifier="bcdDevice",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
