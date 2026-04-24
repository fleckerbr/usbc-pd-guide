<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# DEVICE_ID

| Address               | Register Name         | IO Access         | Reset Value           |
| :-------------------: | :-------------------: | :---------------: | :-------------------: |
| `0x04`..`0x05`        | [DEVICE_ID]           | `Read`            | `Vendor Defined`      |

## Description

The Device ID, [bcdDevice](/usbc-pd-buide/port-controller/registers/device-id/#bcd-device), is used to identify the release version of the product.
The [bcdDevice](/usbc-pd-buide/port-controller/registers/device-id/#bcd-device) field should reflect a version number relevant to the release version of the product.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15..0`      | bcd Device                                | [DEVICE_ID.bcdDevice]                     |

### `B15..0` bcd Device { #bcd-device data-toc-label="bcd Device" }

!!! success "DEVICE_ID.bcdDevice (Required)"
    A unique 16-bit unsigned integer assigned by the Vendor to identify the version of the TCPC.
