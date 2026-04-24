from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class ProductID(Register):
    __address__ = 0x02
    __alias__ = "Product ID"
    __identifier__ = "PRODUCT_ID"
    __readable__ = True
    __writable__ = False

    PID = Field(
        bits=B(15, 0),
        alias="Product ID",
        identifier="PID",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
