<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# PRODUCT_ID

| Address               | Register Name         | IO Access         | Reset Value           |
| :-------------------: | :-------------------: | :---------------: | :-------------------: |
| `0x02`..`0x03`        | [PRODUCT_ID]          | `Read`            | `Vendor Defined`      |

## Description

The Product ID, or [PID](/usbc-pd-buide/port-controller/registers/product-id/#product-id-pid), is used to identify the TCPC product.
Manufacturers should set the USB Product ID field to a unique value across all USB products from the vendor.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B15..0`      | Product ID (PID)                          | [PRODUCT_ID.PID]                          |

### `B15..0` Product ID (PID) { #product-id-pid data-toc-label="Product ID (PID)" }

!!! success "PRODUCT_ID.PID (Required)"
    A unique 16-bit unsigned integer assigned uniquely by the Vendor to identify the TCPC.
