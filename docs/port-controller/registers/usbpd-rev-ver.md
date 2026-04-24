<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# USBPD_REV_VER

| Address               | Register Name         | IO Access         | Reset Value           |
| :-------------------: | :-------------------: | :---------------: | :-------------------: |
| `0x08`..`0x09`        | [USBPD_REV_VER]       | `Read`            | `Vendor Defined`      |

## Description

This register refers to USB PD Specification Revision and Version, USB PD represented by a unique 16-bit unsigned integer.
The format is packed binary coded decimal.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15..8`      | bcd USB PD Revision                       | [USBPD_REV_VER.bcdUSBPDRevision]          |
| `B7..0`       | bcd USB PD Version                        | [USBPD_REV_VER.bcdUSBPDVersion]           |

### `B15..8` bcd USB PD Revision { #bcd-usb-pd-revision data-toc-label="bcd USB PD Revision" }

!!! success "USBPD_REV_VER.bcdUSBPDRevision (Required)"
    Example: `0011 0001` - Revision 3.1

### `B7..0` bcd USB PD Version { #bcd-usb-pd-version data-toc-label="bcd USB PD Version" }

!!! success "USBPD_REV_VER.bcdUSBPDVersion (Required)"
    Example: `0001 0000` - Version 1.0
