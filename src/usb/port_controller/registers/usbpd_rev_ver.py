from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class USBPDRevVer(Register):
    __address__ = 0x08
    __alias__ = "USB PD Revision Version"
    __identifier__ = "USBPD_REV_VER"
    __readable__ = True
    __writable__ = False

    BCD_USB_PD_REVISION = Field(
        bits=B(15, 8),
        alias="bcd USB PD Revision",
        identifier="bcdUSBPDRevision",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    BCD_USB_PD_VERSION = Field(
        bits=B(7, 0),
        alias="bcd USB PD Version",
        identifier="bcdUSBPDVersion",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
