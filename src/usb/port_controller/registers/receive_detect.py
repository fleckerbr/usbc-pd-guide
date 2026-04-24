from __future__ import annotations

from usb.port_controller import B, Field, Register


class ReceiveDetect(Register):
    __address__ = 0x2F
    __alias__ = "Receive Detect"
    __identifier__ = "RECEIVE_DETECT"
    __readable__ = True
    __writable__ = True

    MESSAGE_DISABLE_DISCONNECT = Field(
        bits=B(7),
        alias="Message Disable Disconnect",
        identifier="MessageDisableDisconnect",
        reset=0b0,
        required=True,
    )
    ENABLE_CABLE_RESET = Field(
        bits=B(6),
        alias="Enable Cable Reset",
        identifier="EnableCableReset",
        reset=0b0,
        required=True,
    )
    ENABLE_HARD_RESET = Field(
        bits=B(5),
        alias="Enable Hard Reset",
        identifier="EnableHardReset",
        reset=0b0,
        required=True,
    )
    ENABLE_SOPDBG11_MESSAGE = Field(
        bits=B(4),
        alias="Enable SOP_DBG'' message",
        identifier="EnableSOPDBG''message",
        reset=0b0,
        required=True,
    )
    ENABLE_SOPDBG1_MESSAGE = Field(
        bits=B(3),
        alias="Enable SOP_DBG' message",
        identifier="EnableSOPDBG'message",
        reset=0b0,
        required=True,
    )
    ENABLE_SOP11_MESSAGE = Field(
        bits=B(2),
        alias="Enable SOP'' message",
        identifier="EnableSOP''message",
        reset=0b0,
        required=True,
    )
    ENABLE_SOP1_MESSAGE = Field(
        bits=B(1),
        alias="Enable SOP' message",
        identifier="EnableSOP'message",
        reset=0b0,
        required=True,
    )
    ENABLE_SO_PMESSAGE = Field(
        bits=B(0),
        alias="Enable SOP message",
        identifier="EnableSOPmessage",
        reset=0b0,
        required=True,
    )
