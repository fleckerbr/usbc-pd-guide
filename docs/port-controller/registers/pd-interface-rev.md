<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# PD_INTERFACE_REV

| Address               | Register Name         | IO Access         | Reset Value           |
| :-------------------: | :-------------------: | :---------------: | :-------------------: |
| `0x0A`..`0x0B`        | [PD_INTERFACE_REV]    | `Read`            | `Vendor Defined`      |

## Description

The USB-Port Controller Specification Revision register refers to this Specification Revision and Version represented by a unique 16-bit unsigned integer.
The format is packed binary coded decimal.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                        |
| ------------- | ----------------------------------------- | ------------------------------------------------- |
| `B15..8`      | bcd USB PD Interface Revision             | [PD_INTERFACE_REV.bcdUSBPDInterfaceRevision]      |
| `B7..0`       | bcd USB PD Interface Version              | [PD_INTERFACE_REV.bcdUSBPDInterfaceVersion]       |

### `B15..8` bcd USB PD Interface Revision { #bcd-usb-pd-interface-revision data-toc-label="bcd USB PD Interface Revision" }

!!! success "PD_INTERFACE_REV.bcdUSBPDInterfaceRevision (Required)"
    Example: `0010 0000` - Revision 2.0

### `B7..0` bcd USB PD Interface Version { #bcd-usb-pd-interface-version data-toc-label="bcd USB PD Interface Version" }

!!! success "PD_INTERFACE_REV.bcdUSBPDInterfaceVersion (Required)"
    Example: `0001 0011` - Version 1.3
