from __future__ import annotations

from usb.port_controller import B, Field, Register


class Command(Register):
    __address__ = 0x23
    __alias__ = "Command"
    __identifier__ = "COMMAND"
    __readable__ = False
    __writable__ = True

    WAKE_I2C = Field(
        bits=B(7, 0),
        alias="Wake I2C",
        identifier="WakeI2C",
        reset=0b00000000,
        required=True,
    )
    DISABLE_VBUS_DETECT = Field(
        bits=B(7, 0),
        alias="Disable VBus Detect",
        identifier="DisableVBusDetect",
        reset=0b00000000,
        required=True,
    )
    ENABLE_VBUS_DETECT = Field(
        bits=B(7, 0),
        alias="Enable VBus Detect",
        identifier="EnableVBusDetect",
        reset=0b00000000,
        required=True,
    )
    DISABLE_SINK_VBUS = Field(
        bits=B(7, 0),
        alias="Disable Sink VBus",
        identifier="DisableSinkVBus",
        reset=0b00000000,
        required=True,
    )
    SINK_VBUS = Field(
        bits=B(7, 0),
        alias="Sink VBus",
        identifier="SinkVBus",
        reset=0b00000000,
        required=True,
    )
    DISABLE_SOURCE_VBUS = Field(
        bits=B(7, 0),
        alias="Disable Source VBus",
        identifier="DisableSourceVBus",
        reset=0b00000000,
        required=True,
    )
    SOURCE_VBUS_DEFAULT_VOLTAGE = Field(
        bits=B(7, 0),
        alias="Source VBus Default Voltage",
        identifier="SourceVBusDefaultVoltage",
        reset=0b00000000,
        required=True,
    )
    SOURCE_VBUS_NONDEFAULT_VOLTAGE = Field(
        bits=B(7, 0),
        alias="Source VBus Nondefault Voltage",
        identifier="SourceVBusNondefaultVoltage",
        reset=0b00000000,
        required=True,
    )
    LOOK4_CONNECTION = Field(
        bits=B(7, 0),
        alias="Look4Connection",
        identifier="Look4Connection",
        reset=0b00000000,
        required=True,
    )
    RX_ONE_MORE = Field(
        bits=B(7, 0),
        alias="Receive One More",
        identifier="RxOneMore",
        reset=0b00000000,
        required=True,
    )
    SEND_FR_SWAP_SIGNAL = Field(
        bits=B(7, 0),
        alias="Send FR Swap Signal",
        identifier="SendFRSwapSignal",
        reset=0b00000000,
        required=True,
    )
    RESET_TRANSMIT_BUFFER = Field(
        bits=B(7, 0),
        alias="Reset Transmit Buffer",
        identifier="ResetTransmitBuffer",
        reset=0b00000000,
        required=True,
    )
    RESET_RECEIVE_BUFFER = Field(
        bits=B(7, 0),
        alias="Reset Receive Buffer",
        identifier="ResetReceiveBuffer",
        reset=0b00000000,
        required=True,
    )
    I2C_IDLE = Field(
        bits=B(7, 0),
        alias="I2C Idle",
        identifier="I2CIdle",
        reset=0b00000000,
        required=True,
    )
