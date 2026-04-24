from __future__ import annotations

from usb.port_controller import B, Field, Register


class FaultStatusMask(Register):
    __address__ = 0x15
    __alias__ = "Fault Status Mask"
    __identifier__ = "FAULT_STATUS_MASK"
    __readable__ = True
    __writable__ = True

    ALL_REGISTERS_RESET_TO_DEFAULT = Field(
        bits=B(7),
        alias="All Registers Reset To Default",
        identifier="AllRegistersResetToDefault",
        reset=0b1,
        required=True,
    )
    FORCE_OFF_VBUS_MASK = Field(
        bits=B(6),
        alias="Force Off VBus Interrupt Status Mask",
        identifier="ForceOffVBusMask",
        reset=0b1,
        required=True,
    )
    AUTO_DISCHARGE_FAILED_MASK = Field(
        bits=B(5),
        alias="Auto Discharge Failed Mask",
        identifier="AutoDischargeFailedMask",
        reset=0b1,
        required=True,
    )
    FORCE_DISCHARGE_FAILED_MASK = Field(
        bits=B(4),
        alias="Force Discharge Failed Mask",
        identifier="ForceDischargeFailedMask",
        reset=0b1,
        required=True,
    )
    INTERNAL_OR_EXTERNAL_OCP_FAULT_MASK = Field(
        bits=B(3),
        alias="VBus Over Current Protection Fault Interrupt Status Mask",
        identifier="InternalOrExternalOCPFaultMask",
        reset=0b1,
        required=True,
    )
    INTERNAL_OR_EXTERNAL_OCV_FAULT_MASK = Field(
        bits=B(2),
        alias="VBus Over Voltage Protection Fault Interrupt Status Mask",
        identifier="InternalOrExternalOCVFaultMask",
        reset=0b1,
        required=True,
    )
    VCONN_OVER_CURRENT_FAULT_MASK = Field(
        bits=B(1),
        alias="VConn Over Current Fault Interrupt Status Mask",
        identifier="VConnOverCurrentFaultMask",
        reset=0b1,
        required=True,
    )
    I2C_INTERFACE_ERROR_MASK = Field(
        bits=B(0),
        alias="I2C Interface Error Interrupt Status Mask",
        identifier="I2CInterfaceErrorMask",
        reset=0b1,
        required=True,
    )
