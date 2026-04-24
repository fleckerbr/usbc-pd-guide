from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class DeviceCapabilities3(Register):
    __address__ = 0x7C
    __alias__ = "Device Capabilities 3"
    __identifier__ = "DEVICE_CAPABILITIES_3"
    __readable__ = True
    __writable__ = False

    RESERVED_15 = Field(
        bits=B(15, 3),
        alias="Reserved",
        identifier="Reserved15",
        reset=0b0000000000000,
        required=True,
    )
    VBUS_VOLTAGE_SUPPORT = Field(
        bits=B(2, 0),
        alias="VBus Voltage Support",
        identifier="VBusVoltageSupport",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
