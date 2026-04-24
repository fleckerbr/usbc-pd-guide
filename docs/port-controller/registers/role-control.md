<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# ROLE_CONTROL

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x1A`                | [ROLE_CONTROL]        | `Read`/`Write`    | `...`             |

## Description

After the TCPC has set the power on reset default values, this register is set and cleared only by the TCPM.
The TCPM writes to this register to configure the CC pull up (Rp) or pull down (Rd) resistors.

The TCPM shall write B6 (DRP) = `0b` and B3..0 (CC1/CC2) if it wishes to control the Rp/Rd directly
instead of having the TCPC perform DRP toggling autonomously.
When controlling Rp/Rd directly, the TCPM writes to B3..0 (CC1/CC2) each time it wishes to change the CC1/CC2 values.
This control is used for TCPM-TCPC implementing Source or Sink only as well as when a connection has been detected via
DRP toggling but the TCPM wishes to attempt Try.SRC or Try.SNK (as defined in [USB TC]).

The TCPM may configure the TCPC to autonomously toggle the Rp/Rd when the TCPM-TCPC is implementing a DRP.
When initiating autonomous DRP toggling, the TCPM shall write B6 (DRP) = `1b` and write the starting value of
Rp/Rd to B3..0 (CC1/CC2) to indicate DRP autonomous toggling mode to the TCPC.
The TCPC shall not start the DRP toggling until subsequently the TCPM writes to the [COMMAND] register to start
the DRP toggling while [POWER_CONTROL.AutoDischargeDisconnect]=`0b`, as in Figure 4-19.

It is recommended the TCPM write [ROLE_CONTROL.DRP]=`0b` before writing to [POWER_CONTROL.AutoDischargeDisconnect] and
starting the DRP toggling using [COMMAND.Look4Connection] as shown in Figure 4-24, Figure 4-25 and Figure 4-26.
If [ROLE_CONTROL.DRP]=`1b`, the only allowed values for CC1/CC2 are Rp/Rp or Rd/Rd.
[COMMAND.Look4Connection] shall do nothing if CC1/CC2 are not Rp/Rp or Rd/Rd.
When CC1 and CC2 are set to Open and DRP = `0b`, the TCPC may power down the PHY and CC Status comparators.

When the TCPM has set [ROLE_CONTROL.CC1] = [ROLE_CONTROL.CC2]=`11b` (Open), the Sink TCPC is recommended
to remove terminations from the CC pins as long as the VBUS is present (i.e. above vSafe5V).
This allows a bus-powered Sink TCPC to remove terminations from CC pins in USB Type-C ErrorRecovery state when the VBUS is present.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7`          | Reserved                                  |                                           |
| `B6`          | DRP                                       | [ROLE_CONTROL.DRP]                        |
| `B5..4`       | Rp Value                                  | [ROLE_CONTROL.RpValue]                    |
| `B3..2`       | CC2                                       | [ROLE_CONTROL.CC2]                        |
| `B1..0`       | CC1                                       | [ROLE_CONTROL.CC1]                        |

### `B6` DRP { #drp data-toc-label="DRP" }

!!! success "ROLE_CONTROL.DRP (Required)"
    `0b` :material-arrow-right-thin: Source-only or Sink-only power mode is selected.

    `1b` :material-arrow-right-thin: Dual-Role-Power mode is selected.

    :   The TCPC shall use the Rp value defined in [`B5..4`](#rp-value) when a connection is resolved.
        The TCPC toggles CC1 & CC2 after receiving [COMMAND.Look4Connection] and until a connection is detected.
        Upon connection, the TCPC shall resolve to either an Rp or Rd and report the CC1/CC2 State in the [CC_STATUS] register.

### `B5..4` Rp Value { #rp-value data-toc-label="Rp Value" }

!!! success "ROLE_CONTROL.RpValue (Required)"
    `00b` :material-arrow-right-thin: Rp default

    `01b` :material-arrow-right-thin: Rp 1.5A

    `10b` :material-arrow-right-thin: Rp 3.0A

    `11b` :material-arrow-right-thin: Reserved

### `B3..2` CC2 { #cc2 data-toc-label="CC2" }

!!! success "ROLE_CONTROL.CC2 (Required)"
    `00b` :material-arrow-right-thin: Ra

    `01b` :material-arrow-right-thin: Rp (Use Rp definition in [`B5..4`](#rp-value))

    `10b` :material-arrow-right-thin: Rd

    `11b` :material-arrow-right-thin: Open (Disconnect or don't care)

### `B1..0` CC1 { #cc1 data-toc-label="CC1" }

!!! success "ROLE_CONTROL.CC1 (Required)"
    `00b` :material-arrow-right-thin: Ra

    `01b` :material-arrow-right-thin: Rp (Use Rp definition in [`B5..4`](#rp-value))

    `10b` :material-arrow-right-thin: Rd

    `11b` :material-arrow-right-thin: Open (Disconnect or don't care)
