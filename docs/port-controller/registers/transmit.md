<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# TRANSMIT

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x50`                | [TRANSMIT]            | `Read`/`Write`    | `0x00`            |

## Description

Transmit aggregate of data written to [TRANSMIT_BUFFER] since the pointer was last reset.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..6`       | Reserved                                  |                                           |
| `B5..4`       | Retry Counter                             | [TRANSMIT.RetryCounter]                   |
| `B3`          | Reserved                                  |                                           |
| `B2..0`       | Transmit SOP* Message                     | [TRANSMIT.TransmitSOP*Message]            |

### `B5..4` Retry Counter { #retry-counter data-toc-label="Retry Counter" }

!!! success "TRANSMIT.RetryCounter (Required)"
    <<PLACEHOLDER>>

### `B2..0` Transmit SOP\* Message { #transmit-sop-message data-toc-label="Transmit SOP* Message" }

!!! success "TRANSMIT.TransmitSOP*Message (Required)"
    <<PLACEHOLDER>>
