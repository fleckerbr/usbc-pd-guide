<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# RECEIVE_BUFFER

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x30`                | [RECEIVE_BUFFER]      | -                 |                   |

## Description

The [RECEIVE_BUFFER] comprises of three sets of registers: [READABLE_BYTE_COUNT], [RX_BUF_FRAME_TYPE] and [RX_BUF_BYTE_x].
These registers can only be accessed by reading at a common register address `0x30`.

These registers indicate the status of the received SOP\* message buffer and shall be read by the TCPM when the TCPC
sets [ALERT.RxStatus] to indicate that a SOP\* message was received.

The TCPC shall set the [READABLE_BYTE_COUNT] to `0x00` after the interrupt has been cleared.
See Sections 4.7.5, 4.7.6, 4.7.7, 4.7.8, and 4.7.9 for information on receiving SOP\* messages, Hard Reset, and Cable Reset messages respectively.

The TCPC shall disable PD message delivery and set the [READABLE_BYTE_COUNT] to zero upon detection of a disconnect
(Sink TCPC shall use the disconnect condition as defined in [RECEIVE_DETECT.MessageDisableDisconnect]).
The TCPM power down PD message delivery per Section 4.8.2.

If [DEVICE_CAPABILITIES_2.LongMessage] is set to `0b`, the [RECEIVE_BUFFER] is sized to hold two 30 bytes SOP\* messages.

If [DEVICE_CAPABILITIES_2.LongMessage] is set to `1b`, the [RECEIVE_BUFFER] is sized to hold a 264 bytes SOP\* message plus a 30 bytes SOP\* message.

Regardless of the [DEVICE_CAPABILITIES_2.LongMessage] setting, TCPC shall automatically increment the pointer of [RX_BUF_BYTE_x] as TCPM reads [RX_BUF_BYTE_x].
TCPM can re-read [RX_BUF_BYTE_x] at a zero offset by writing to [COMMAND.ResetReceiveBuffer] (0xEE).
However, the pointer of [RX_BUF_BYTE_x] would not increment if TCPM reads [READABLE_BYTE_COUNT] or [RX_BUF_FRAME_TYPE].

***

## READABLE_BYTE_COUNT

| Address               | Register Name             | IO Access         | Reset Value       |
| :-------------------: | :-----------------------: | :---------------: | :---------------: |
| `0x30`                | [READABLE_BYTE_COUNT]     | `Read`            | `0x00`            |

### Description

The TCPM reads the [READABLE_BYTE_COUNT] to determine the number of bytes in the [RX_BUF_BYTE_x]

If [DEVICE_CAPABILITIES_2.LongMessage]=`0b`, the value in this register shall be less than or equal to 31.

If [DEVICE_CAPABILITIES_2.LongMessage]=`1b`, the value supported in this register shall be up to 133.

### Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..0`       | Readable Byte Count                       | [READABLE_BYTE_COUNT.ReadableByteCount]   |

#### `B7..0` Readable Byte Count { #readable-byte-count data-toc-label="Readable Byte Count" }

!!! success "READABLE_BYTE_COUNT.ReadableByteCount (Required)"
    Indicates the number of bytes in the [RX_BUF_BYTE_x] registers plus one (for the [RX_BUF_FRAME_TYPE]).
    The content of this register is undefined when the [RECEIVE_BUFFER] is cleared.

***

## RX_BUF_FRAME_TYPE

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x30`                | [RX_BUF_FRAME_TYPE]   | `Read`            | `0x00`            |

### Description

The TCPM reads the [RX_BUF_FRAME_TYPE] to determine the type of message.

This register is "hidden" and can only be accessed by reading at address `0x30`.

### Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..3`       | Reserved                                  |                                           |
| `B2..0`       | Received SOP* Message                     | [RX_BUF_FRAME_TYPE.RxMessage]             |

#### `B2..0` Received SOP\* Message { #received-sop-message data-toc-label="Received SOP* Message" }

!!! success "RX_BUF_FRAME_TYPE.RxMessage (Required)"
    `000b` :material-arrow-right-thin: Received SOP

    `001b` :material-arrow-right-thin: Received SOP'

    `010b` :material-arrow-right-thin: Received SOP''

    `011b` :material-arrow-right-thin: Received SOP_DBG'

    `100b` :material-arrow-right-thin: Received SOP_DBG''

    `110b` :material-arrow-right-thin: Received Cable Reset

    All others are reserved.

***

## RX_BUF_BYTE_x

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x30`                | [RX_BUF_BYTE_x]       | `Read`            | `0x00`            |

### Description

The TCPM reads the content of the USB PD message at index `x` of the receive buffer.

These registers are "hidden" and can only be accessed by reading at address `0x30`.

### Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..0`       | Value                                     | [RX_BUF_BYTE_x.Value]                     |

#### `B7..0` Value { #value data-toc-label="Value" }

!!! success "RX_BUF_BYTE_x.Value (Required)"
    The value received at index `x` of the receive buffer.

***
