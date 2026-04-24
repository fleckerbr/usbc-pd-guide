from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class PDInterfaceRev(Register):
    __address__ = 0x0A
    __alias__ = "PD Interface Revision"
    __identifier__ = "PD_INTERFACE_REV"
    __readable__ = True
    __writable__ = False

    BCD_USB_PD_INTERFACE_REVISION = Field(
        bits=B(15, 8),
        alias="bcd USB PD Inter-Block Specification Revision",
        identifier="bcdUSBPDRevision",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    BCD_USB_PD_INTERFACE_VERSION = Field(
        bits=B(7, 0),
        alias="bcd USB PD Inter-Block Specification Version",
        identifier="bcdUSBPDVersion",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
