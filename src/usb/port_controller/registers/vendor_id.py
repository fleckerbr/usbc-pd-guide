from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class VendorID(Register):
    __address__ = 0x00
    __alias__ = "Vendor ID"
    __identifier__ = "VENDOR_ID"
    __readable__ = True
    __writable__ = False

    VID = Field(
        bits=B(15, 0),
        alias="Vendor ID",
        identifier="VID",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
