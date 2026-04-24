<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# TRANSMIT_BUFFER

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x51`                | [TRANSMIT_BUFFER]     | -                 |                   |

## Description

The [TRANSMIT_BUFFER] holds the [I2C_WRITE_BYTE_COUNT] and the portion of the SOP\* USB PD message payload
(including the header and/or the data bytes) most recently written by the TCPM in [TX_BUF_BYTE_x].

If DEVICE_CAPABILITIES_2.LongMessage is set to zero, the TRANSMIT_BUFFER is capable of holding 30 byte SOP\* message. The TCPM can write up to 30 bytes to the TX_BUF_BYTE_x in one burst.

Regardless of the [DEVICE_CAPABILITIES_2.LongMessage] setting, the TCPC automatically increments the [TX_BUF_BYTE_x] offset as TCPM writes to [TX_BUF_BYTE_x].
The TCPM can re-write to [TX_BUF_BYTE_x] beginning at offset 1 by writing to [COMMAND.ResetTransmitBuffer].
The TCPM shall write as many bytes in the buffer as defined in the [I2C_WRITE_BYTE_COUNT] in one I2C write transaction.
If the [I2C_WRITE_BYTE_COUNT] is different than the number of bytes written in the buffer,
the TCPC shall assert [FAULT_STATUS.I2CInterfaceError] and ignore the write (i.e. no change in the [TX_BUF_BYTE_x] content and the offset).

***

## I2C_WRITE_BYTE_COUNT

| Address               | Register Name             | IO Access         | Reset Value       |
| :-------------------: | :-----------------------: | :---------------: | :---------------: |
| `0x51`                | [I2C_WRITE_BYTE_COUNT]    | `Write`           | `0x00`            |

### Description

The number of bytes the TCPM writes to the [TX_BUF_BYTEx] in the given I2C/SMBus transaction.
The TCPM shall write as many bytes in the buffer as defined in this register in one I2C write transaction.

If [DEVICE_CAPABILITIES_2.LongMessage]=`0b`, the TCPC shall ignore the I2C transaction if [I2C_WRITE_BYTE_COUNT] is more than 30.

If [DEVICE_CAPABILITIES_2.LongMessage]=`1b`, the TCPC shall ignore the I2C transaction if [I2C_WRITE_BYTE_COUNT] is more than 132.

### Register Fields

| Bit(s)        | Name                                      | Identifier                                    |
| ------------- | ----------------------------------------- | --------------------------------------------- |
| `B7..0`       | I2C Write Byte Count                      | [I2C_WRITE_BYTE_COUNT.I2CWriteByteCount]      |

#### `B7..0` I2C Write Byte Count { #i2c-write-byte-count data-toc-label="I2C Write Byte Count" }

!!! success "I2C_WRITE_BYTE_COUNT.I2CWriteByteCount (Required)"
    The number of bytes the TCPM writes to the [TX_BUF_BYTEx] in the given I2C/SMBus transaction.

***

## TX_BUF_BYTE_x

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x51`                | [TX_BUF_BYTE_x]       | `Write`           | `0x00`            |

### Description

The TCPM writes the content of the USB PD message to index `x` of the transmit buffer.

These registers are "hidden" and can only be accessed by reading at address `0x51`.

### Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..0`       | Value                                     | [TX_BUF_BYTE_x.Value]                     |

#### `B7..0` Value { #value data-toc-label="Value" }

!!! success "TX_BUF_BYTE_x.Value (Required)"
    The value received at index `x` of the receive buffer.

***
