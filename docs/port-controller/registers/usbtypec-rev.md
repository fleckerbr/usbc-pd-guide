<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# USBTYPEC_REV

| Address               | Register Name         | IO Access         | Reset Value           |
| :-------------------: | :-------------------: | :---------------: | :-------------------: |
| `0x06`..`0x07`        | [USBTYPEC_REV]        | `Read`            | `Vendor Defined`      |

## Description

This register refers to [USB TC] Cable and Connector Specification Revision, USB Type-C represented by a unique 16-bit unsigned register.
The format is packed binary coded decimal.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15..8`      | Reserved                                  |                                           |
| `B7..0`       | bcd USB Type-C Release                    | [USBTYPEC_REV.bcdUSBTypeCRelease]         |

### `B7..0` bcd USB Type-C Release { #bcd-usb-type-c-release data-toc-label="bcd USB Type-C Release" }

!!! success "USBTYPEC_REV.bcdUSBTypeCRelease (Required)"
    Example: `0010 0001` - Release 2.1
