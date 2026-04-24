from __future__ import annotations

from usb.port_controller import B, Field, Register, Reset


class DeviceCapabilities2(Register):
    __address__ = 0x26
    __alias__ = "Device Capabilities 2"
    __identifier__ = "DEVICE_CAPABILITIES_2"
    __readable__ = True
    __writable__ = False

    DEVICE_CAPABILITIES_3_SUPPORT = Field(
        bits=B(15),
        alias="DEVICE_CAPABILITIES_3 Support",
        identifier="DeviceCapabilities3Support",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    MESSAGE_DISABLE_DISCONNECT = Field(
        bits=B(14),
        alias="Message Disable Disconnect",
        identifier="MessageDisableDisconnect",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    GENERIC_TIMER = Field(
        bits=B(13),
        alias="Generic Timer",
        identifier="GenericTimer",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    LONG_MESSAGE = Field(
        bits=B(12),
        alias="Long Message",
        identifier="LongMessage",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SM_BUS_PEC = Field(
        bits=B(11),
        alias="SMBus PEC",
        identifier="SMBusPEC",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SOURCE_FR_SWAP = Field(
        bits=B(10),
        alias="Source FR Swap",
        identifier="SourceFRSwap",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SINK_FR_SWAP = Field(
        bits=B(9),
        alias="Sink FR Swap",
        identifier="SinkFRSwap",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    WATCHDOG_TIMER = Field(
        bits=B(8),
        alias="Watchdog Timer",
        identifier="WatchdogTimer",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    SINK_DISCONNECT_DETECTION = Field(
        bits=B(7),
        alias="Sink Disconnect Detection",
        identifier="SinkDisconnectDetection",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    STOP_DISCHARGE_THRESHOLD = Field(
        bits=B(6),
        alias="Stop Discharge Threshold",
        identifier="StopDischargeThreshold",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VBUS_VOLTAGE_ALARM_LSB = Field(
        bits=B(5, 4),
        alias="VBus Voltage Alarm LSB",
        identifier="VBusVoltageAlarmLSB",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VCONN_POWER_SUPPORTED = Field(
        bits=B(3, 1),
        alias="VConn Power Supported",
        identifier="VConnPowerSupported",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
    VCONN_OVERCURRENT_FAULT_CAPABLE = Field(
        bits=B(0),
        alias="VConn Overcurrent Fault Capable",
        identifier="VConnOvercurrentFaultCapable",
        reset=Reset.VENDOR_DEFINED,
        required=True,
    )
