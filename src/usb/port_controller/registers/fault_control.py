from __future__ import annotations

from usb.port_controller import B, Field, Register


class FaultControl(Register):
    __address__ = 0x1B
    __alias__ = "Fault Control"
    __identifier__ = "FAULT_CONTROL"
    __readable__ = True
    __writable__ = True

    RESERVED_7 = Field(
        bits=B(7, 5),
        alias="Reserved",
        identifier="Reserved7",
        reset=0b000,
        required=True,
    )
    FORCE_OFF_VBUS = Field(
        bits=B(4),
        alias="Force Off VBus",
        identifier="ForceOffVBus",
        reset=0b0,
        required=False,
    )
    VBUS_DISCHARGE_FAULT_DETECTION_TIMER = Field(
        bits=B(3),
        alias="VBus Discharge Fault Detection Timer",
        identifier="VBusDischargeFaultDetectionTimer",
        reset=0b0,
        required=True,
    )
    INTERNAL_OR_EXTERNAL_OCP_FAULT = Field(
        bits=B(2),
        alias="VBus Over Current Protection Fault",
        identifier="InternalOrExternalOCPFault",
        reset=0b0,
        required=False,
    )
    INTERNAL_OR_EXTERNAL_OVP_FAULT = Field(
        bits=B(1),
        alias="VBus Over Voltage Protection Fault",
        identifier="InternalOrExternalOVPFault",
        reset=0b0,
        required=False,
    )
    VCONN_OVER_CURRENT_FAULT = Field(
        bits=B(0),
        alias="VConn Over Current Fault",
        identifier="VConnOverCurrentFault",
        reset=0b0,
        required=False,
    )
