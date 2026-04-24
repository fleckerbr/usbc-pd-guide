from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class USBTypeCRev(Register):
    __address__ = 0x06
    __alias__ = "USB Type-C Revision"
    __identifier__ = "USBTYPEC_REV"
    __readable__ = True
    __writable__ = False

    RESERVED_15 = Field(
        bits=B(15, 8),
        alias="Reserved",
        identifier="Reserved15",
        reset=0b00000000,
        required=True,
    )
    BCD_USB_TYPEC_RELEASE = Field(
        bits=B(7, 0),
        alias="bcd USB Type-C Release",
        identifier="bcdUSBTypeCRelease",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
