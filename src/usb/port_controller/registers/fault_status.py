from __future__ import annotations

from usb.port_controller import B, Field, Register


class FaultStatus(Register):
    __address__ = 0x1F
    __alias__ = "Fault Status"
    __identifier__ = "FAULT_STATUS"
    __readable__ = True
    __writable__ = True

    ALL_REGISTERS_RESET_TO_DEFAULT = Field(
        bits=B(7),
        alias="All Registers Reset To Default",
        identifier="AllRegistersResetToDefault",
        reset=0b1,
        required=True,
    )
    FORCE_OFF_VBUS = Field(
        bits=B(6),
        alias="Force Off VBus",
        identifier="ForceOffVBus",
        reset=0b0,
        required=True,
    )
    AUTO_DISCHARGE_FAILED = Field(
        bits=B(5),
        alias="Auto Discharge Failed",
        identifier="AutoDischargeFailed",
        reset=0b0,
        required=True,
    )
    FORCE_DISCHARGE_FAILED = Field(
        bits=B(4),
        alias="Force Discharge Failed",
        identifier="ForceDischargeFailed",
        reset=0b0,
        required=True,
    )
    INTERNAL_OR_EXTERNAL_OCP = Field(
        bits=B(3),
        alias="VBus Over Current Protection Fault",
        identifier="InternalOrExternalOCP",
        reset=0b0,
        required=True,
    )
    INTERNAL_OR_EXTERNAL_OVP = Field(
        bits=B(2),
        alias="VBus Over Voltage Protection Fault",
        identifier="InternalOrExternalOVP",
        reset=0b0,
        required=True,
    )
    VCONN_OVER_CURRENT_FAULT = Field(
        bits=B(1),
        alias="VConn Over Current Fault",
        identifier="VConnOverCurrentFault",
        reset=0b0,
        required=True,
    )
    I2C_INTERFACE_ERROR = Field(
        bits=B(0),
        alias="I2C Interface Error",
        identifier="I2CInterfaceError",
        reset=0b0,
        required=True,
    )
