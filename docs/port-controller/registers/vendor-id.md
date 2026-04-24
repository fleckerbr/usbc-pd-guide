<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# VENDOR_ID

| Address               | Register Name         | IO Access         | Reset Value           |
| :-------------------: | :-------------------: | :---------------: | :-------------------: |
| `0x00`..`0x01`        | [VENDOR_ID]           | `Read`            | `Vendor Defined`      |

## Description

A Vendor ID, or [VID](/usbc-pd-buide/port-controller/registers/vendor-id/#vendor-id-vid), is used to identify the TCPC vendor.
The [VID](/usbc-pd-buide/port-controller/registers/vendor-id/#vendor-id-vid) is a unique 16-bit unsigned integer assigned by USB-IF.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15..0`      | Vendor ID (VID)                           | [VENDOR_ID.VID]                           |

### `B15..0` Vendor ID (VID) { #vendor-id-vid data-toc-label="Vendor ID (VID)" }

!!! success "VENDOR_ID.VID (Required)"
    A unique 16-bit unsigned integer assigned by the USB-IF to the Vendor.
