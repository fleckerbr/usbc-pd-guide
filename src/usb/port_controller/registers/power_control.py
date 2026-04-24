from __future__ import annotations

from usb.port_controller import B, Field, Register


class PowerControl(Register):
    __address__ = 0x1C
    __alias__ = "Power Control"
    __identifier__ = "POWER_CONTROL"
    __readable__ = True
    __writable__ = True

    FAST_ROLE_SWAP_ENABLE = Field(
        bits=B(7),
        alias="Fast Role Swap Enable",
        identifier="FastRoleSwapEnable",
        reset=0b0,
        required=True,
    )
    VBUS_VOLTAGE_MONITOR = Field(
        bits=B(6),
        alias="VBUS_VOLTAGE Monitor",
        identifier="VBusVoltageMonitor",
        reset=0b1,
        required=True,
    )
    DISABLE_VOLTAGE_ALARMS = Field(
        bits=B(5),
        alias="Disable Voltage Alarms",
        identifier="DisableVoltageAlarms",
        reset=0b1,
        required=True,
    )
    AUTO_DISCHARGE_DISCONNECT = Field(
        bits=B(4),
        alias="Auto Discharge Disconnect",
        identifier="AutoDischargeDisconnect",
        reset=0b0,
        required=True,
    )
    ENABLE_BLEED_DISCHARGE = Field(
        bits=B(3),
        alias="Enable Bleed Discharge",
        identifier="EnableBleedDischarge",
        reset=0b0,
        required=True,
    )
    FORCE_DISCHARGE = Field(
        bits=B(2),
        alias="Force Discharge",
        identifier="ForceDischarge",
        reset=0b0,
        required=True,
    )
    VCONN_POWER_SUPPORTED = Field(
        bits=B(1),
        alias="VConn Power Supported",
        identifier="VConnPowerSupported",
        reset=0b0,
        required=True,
    )
    ENABLE_VCONN = Field(
        bits=B(0),
        alias="Enable VConn",
        identifier="EnableVConn",
        reset=0b0,
        required=True,
    )
