<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# GENERIC_TIMER

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x2C`..`0x2D`        | [GENERIC_TIMER]       | `Write`           | `0x0000`          |

## Description

The TCPM writes a non-zero value to this register to start the general purpose timer.
If the TCPM writes a non-zero value to this register before the timer has expired, the timer is restarted with the last written non-zero value.
After the timer has expired, the timer does not restart until TCPM writes a non-zero value to this register.
The timer shall stop when a zero value is written to this register.

[ALERT_EXTENDED.TimerExpired] is asserted when the last written non-zero timer value has expired.
Clearing the [ALERT_EXTENDED.TimerExpired] has no effect to this register.
To avoid a race condition, the TCPM may write a zero value to this register before writing a non-zero value to start the timer.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15..0`      | Generic Timer                             | [GENERIC_TIMER.GenericTimer]              |

### `B15..0` Generic Timer { #generic-timer data-toc-label="Generic Timer" }

!!! success "GENERIC_TIMER.GenericTimer (Required)"
    16-bit timer value with 0.1ms LSB.

    A non-zero value starts the timer. A value of zero stops the timer. 
    The timer does not restart after it has expired.

    Required if [DEVICE_CAPABILITIES_2.GenericTimer]=`1b`.
