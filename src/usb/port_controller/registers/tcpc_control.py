from __future__ import annotations

from usb.port_controller import B, Field, Register


class TcpcControl(Register):
    __address__ = 0x19
    __alias__ = "Tcpc Control"
    __identifier__ = "TCPC_CONTROL"
    __readable__ = True
    __writable__ = True

    ENABLE_SM_BUS_PEC = Field(
        bits=B(7),
        alias="Enable SMBus PEC",
        identifier="EnableSMBusPEC",
        reset=0b0,
        required=True,
    )
    ENABLE_LOOKING4_CONNECTION_ALERT = Field(
        bits=B(6),
        alias="Enable Looking4Connection Alert",
        identifier="EnableLooking4ConnectionAlert",
        reset=0b0,
        required=True,
    )
    ENABLE_WATCHDOG_TIMER = Field(
        bits=B(5),
        alias="Enable Watchdog Timer",
        identifier="EnableWatchdogTimer",
        reset=0b0,
        required=True,
    )
    DEBUG_ACCESSORY_CONTROL = Field(
        bits=B(5),
        alias="Debug Accessory Control",
        identifier="DebugAccessoryControl",
        reset=0b0,
        required=True,
    )
    I2C_CLOCK_STRETCHING_CONTROL = Field(
        bits=B(3, 2),
        alias="I2C Clock Stretching Control",
        identifier="I2CClockStretchingControl",
        reset=0b00,
        required=True,
    )
    BIST_TEST_MODE = Field(
        bits=B(1),
        alias="BIST Test Mode",
        identifier="BISTTestMode",
        reset=0b0,
        required=True,
    )
    PLUG_ORIENTATION = Field(
        bits=B(0),
        alias="Plug Orientation",
        identifier="PlugOrientation",
        reset=0b0,
        required=True,
    )
