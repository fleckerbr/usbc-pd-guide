from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class DeviceCapabilities1(Register):
    __address__ = 0x24
    __alias__ = "Device Capabilities 1"
    __identifier__ = "DEVICE_CAPABILITIES_1"
    __readable__ = True
    __writable__ = False

    VBUS_NONDEFAULT_TARGET = Field(
        bits=B(15),
        alias="VBus Nondefault Target",
        identifier="VBusNondefaultTarget",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_OCP_REPORTING = Field(
        bits=B(14),
        alias="VBus OCP Reporting",
        identifier="VBusOCPReporting",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_OVP_REPORTING = Field(
        bits=B(13),
        alias="VBus OVP Reporting",
        identifier="VBusOVPReporting",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    BLEED_DISCHARGE = Field(
        bits=B(12),
        alias="Bleed Discharge",
        identifier="BleedDischarge",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    FORCE_DISCHARGE = Field(
        bits=B(11),
        alias="Force Discharge",
        identifier="ForceDischarge",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_MEASUREMENT_AND_ALARM_CAPABLE = Field(
        bits=B(10),
        alias="VBus Measurement and Alarm Capable",
        identifier="VBusMeasurementAndAlarmCapable",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SOURCE_RESISTOR_SUPPORTED = Field(
        bits=B(9, 8),
        alias="Source Resistor Supported",
        identifier="SourceResistorSupported",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    POWER_ROLES_SUPPORTED = Field(
        bits=B(7, 5),
        alias="Power Roles Supported",
        identifier="PowerRolesSupported",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SOPDBG1_SOPDBG11_SUPPORT = Field(
        bits=B(4),
        alias="SOP_DBG'/SOP_DBG'' Support",
        identifier="SOPDBG'/SOPDBG''Support",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SOURCE_VCONN = Field(
        bits=B(3),
        alias="Source VConn",
        identifier="SourceVConn",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SINK_VBUS = Field(
        bits=B(2),
        alias="Sink VBus",
        identifier="SinkVBus",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SOURCE_NONDEFAULT_VBUS = Field(
        bits=B(1),
        alias="Source Nondefault VBus",
        identifier="SourceNondefaultVBus",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SOURCE_VBUS = Field(
        bits=B(0),
        alias="Source VBus",
        identifier="SourceVBus",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
