from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class VendorDefined(Register):
    __address__ = 0x80
    __alias__ = "Vendor Defined"
    __identifier__ = "VENDOR_DEFINED"
    __readable__ = True
    __writable__ = True

    RESERVED_15 = Field(
        bits=B(15, 0),
        alias="Reserved",
        identifier="Reserved15",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
