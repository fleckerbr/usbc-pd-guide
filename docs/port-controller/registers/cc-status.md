<!-- WARNING -- This file is auto-generated and changes will not be saved -->

# CC_STATUS

| Address               | Register Name         | IO Access         | Reset Value       |
| :-------------------: | :-------------------: | :---------------: | :---------------: |
| `0x1D`                | [CC_STATUS]           | `Read`            |                   |

## Description

The TCPM starts the DRP toggling by issuing [COMMAND.Look4Connection].

The TCPM reads this register upon detecting an [Alert#] and seeing the [ALERT.CCStatus]=`1b`.
The TCPC indicates the Connection status, the Connection result, and the current CC state in this register.

The TCPC shall set [CC_STATUS.Looking4Connection]=`0b` when it has detected a potential connection.
The Autonomous DRP toggling details are defined in Figure 4-24 and Section 4.4.8.

The TCPM reads the [Looking4Connection](/usbc-pd-buide/port-controller/registers/cc-status/#looking4connection) to determine if the TCPC is toggling Rp/Rd when operating as a DRP.
The TCPM reads the [CC_STATUS.ConnectResult] to determine if a DRP TCPC is presenting an Rp or Rd.
The TCPM shall read the [CC_STATUS.CC1State] and [CC_STATUS.CC2State] to determine the CC1 and CC2 states.

When reporting the state of the CC lines, the TCPC shall debounce for tTCPCfilter.
The TCPC shall perform a minimal debounce and the TCPM must complete the debounce as defined in [USB TC].

The TCPM as a Source detects a Sink attachment and detachment by reading [CC_STATUS.CC1State] and [CC_STATUS.CC2State] bits.
The CC Status monitoring may be disabled per Section 4.8.3.

A TCPM which is using polling rather than Alerts should assume the data in the [CC_STATUS] register is not valid until at least
tCCStatusDelay + tTCPCFilter + tCcTCPCSampleRate (max) after the [ROLE_CONTROL] has been updated.
The tCcTCPCSampleRate is the CC sample rate used by the TCPC.
The CC sampling method and rate is performed in a vendor specific manner and therefore outside the scope of this specification.

## Register Fields

| Bit(s)        | Name                                      | Identifier                                |
| ------------- | ----------------------------------------- | ----------------------------------------- |
| `B7..6`       | Reserved                                  |                                           |
| `B5`          | Looking4Connection                        | [CC_STATUS.Looking4Connection]            |
| `B4`          | Connect Result                            | [CC_STATUS.ConnectResult]                 |
| `B3..2`       | CC2 State                                 | [CC_STATUS.CC2State]                      |
| `B1..0`       | CC1 State                                 | [CC_STATUS.CC1State]                      |

### `B5` Looking4Connection { #looking4connection data-toc-label="Looking4Connection" }

!!! success "CC_STATUS.Looking4Connection (Required)"
    `0b` :material-arrow-right-thin: TCPC is not actively looking for a connection.

    :   A transition from `1b` to `0b` indicates a potential connection has been found.

    `1b` :material-arrow-right-thin: TCPC is looking for a connection.

    :   Toggling as a DRP or looking for a connection as Sink/Source only condition.

### `B4` Connect Result { #connect-result data-toc-label="Connect Result" }

!!! success "CC_STATUS.ConnectResult (Required)"
    `0b` :material-arrow-right-thin: Alert cleared.

    `1b` :material-arrow-right-thin: [RECEIVE_BUFFER] register changed.

    :   [READABLE_BYTE_COUNT] being set to `0` does not set this bit.

### `B3..2` CC2 State { #cc2-state data-toc-label="CC2 State" }

!!! success "CC_STATUS.CC2State (Required)"
    If ([ROLE_CONTROL.CC2]=`Rp`) or ([CC_STATUS.ConnectResult]=`0b`)

    `00b` :material-arrow-right-thin: SRC.Open (Open, Rp)

    `01b` :material-arrow-right-thin: SRC.Ra (below maximum vRa)

    `10b` :material-arrow-right-thin: SRC.Rd (within the vRd range)

    `11b` :material-arrow-right-thin: Reserved

    ***

    If ([ROLE_CONTROL.CC2]=`Rd`) or ([CC_STATUS.ConnectResult]=`1b`)

    `00b` :material-arrow-right-thin: SNK.Open (below maximum vRa)

    `01b` :material-arrow-right-thin: SNK.Default (above minimum vRd-Connect)

    `10b` :material-arrow-right-thin: SNK.Power1.5 (above minimum vRd-Connect), detects Rp 1.5A

    `11b` :material-arrow-right-thin: SNK.Power3.0 (above minimum vRd-Connect), detects Rp 3.0A

    ***

    If [ROLE_CONTROL.CC2]=`Ra`, this field is set to `00b`

    If [ROLE_CONTROL.CC2]=`Open`, this field is set to `00b`

    This field always returns `00b` if ([CC_STATUS.Looking4Connection]=`1b`) or
    ([POWER_CONTROL.EnableVconn]=`1b` and [TCPC_CONTROL.PlugOrientation]=`1b`).
    Otherwise, the returned value depends upon [ROLE_CONTROL.CC2].

### `B1..0` CC1 State { #cc1-state data-toc-label="CC1 State" }

!!! success "CC_STATUS.CC1State (Required)"
    If ([ROLE_CONTROL.CC1]=`Rp`) or ([CC_STATUS.ConnectResult]=`0b`)

    `00b` :material-arrow-right-thin: SRC.Open (Open, Rp)

    `01b` :material-arrow-right-thin: SRC.Ra (below maximum vRa)

    `10b` :material-arrow-right-thin: SRC.Rd (within the vRd range)

    `11b` :material-arrow-right-thin: Reserved

    ***

    If ([ROLE_CONTROL.CC1]=`Rd`) or ([CC_STATUS.ConnectResult]=`1b`)

    `00b` :material-arrow-right-thin: SNK.Open (below maximum vRa)

    `01b` :material-arrow-right-thin: SNK.Default (above minimum vRd-Connect)

    `10b` :material-arrow-right-thin: SNK.Power1.5 (above minimum vRd-Connect), detects Rp 1.5A

    `11b` :material-arrow-right-thin: SNK.Power3.0 (above minimum vRd-Connect), detects Rp 3.0A

    ***

    If [ROLE_CONTROL.CC1]=`Ra`, this field is set to `00b`

    If [ROLE_CONTROL.CC1]=`Open`, this field is set to `00b`

    This field always returns `00b` if ([CC_STATUS.Looking4Connection]=`1b`) or
    ([POWER_CONTROL.EnableVconn]=`1b` and [TCPC_CONTROL.PlugOrientation]=`1b`).
    Otherwise, the returned value depends upon [ROLE_CONTROL.CC1].
