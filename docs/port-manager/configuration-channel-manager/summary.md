# Configuration Channel State Summary

The following table summarizes the mandatory and optional states for each type of port and the states where PD communication is permitted.

| Connection State                  | SOURCE                        | SINK                          | DRP                           | USB PD Communications     |
| --------------------------------- | :---------------------------: | :---------------------------: | :---------------------------: | :-----------------------: |
| [Disabled]                        | `Optional`                    | `Optional`                    | `Optional`                    | `Not Permitted`           |
| [ErrorRecovery]                   | `Mandatory`, `Optional`[^1]   | `Mandatory`, `Optional`[^1]   | `Mandatory`, `Optional`[^1]   | `Not Permitted`           |
| [Unattached.SNK]                  | `N/A`                         | `Mandatory`                   | `Mandatory`                   | `Not Permitted`           |
| [AttachWait.SNK]                  | `N/A`                         | `Mandatory`, `Optional`[^2]   | `Mandatory`                   | `Not Permitted`           |
| [Attached.SNK]                    | `N/A`                         | `Mandatory`                   | `Mandatory`                   | `Permitted`               |
| [UnattachedWait.SRC]              | `Mandatory`, `N/A`[^3]        | `N/A`                         | `N/A`                         | `Not Permitted`           |
| [Unattached.SRC]                  | `Mandatory`                   | `N/A`                         | `Mandatory`                   | `Not Permitted`           |
| [AttachWait.SRC]                  | `Mandatory`                   | `N/A`                         | `Mandatory`                   | `Not Permitted`           |
| [Attached.SRC]                    | `Mandatory`                   | `N/A`                         | `Mandatory`                   | `Permitted`               |
| [Try.SRC] [^4]                    | `N/A`                         | `N/A`                         | `Optional`                    | `Not Permitted`           |
| [TryWait.SNK] [^5]                | `N/A`                         | `N/A`                         | `Optional`                    | `Not Permitted`           |
| [Try.SNK] [^4] [^10]              | `N/A`                         | `N/A`                         | `Optional`                    | `Not Permitted`           |
| [TryWait.SRC] [^6] [^10]          | `N/A`                         | `N/A`                         | `Optional`                    | `Not Permitted`           |
| [CorrosionMitigation]             | `Optional`                    | `Optional`                    | `Optional`                    | `Not Permitted`           |
| [UnorientedDebugAccessory.SRC]    | `Mandatory`, `Optional`[^7]   | `N/A`                         | `Mandatory`, `Optional`[^7]   | `Not Permitted`           |
| [OrientedDebugAccessory.SRC]      | `Mandatory`, `Optional`[^8]   | `N/A`                         | `Mandatory`, `Optional`[^8]   | `Permitted`               |
| [DebugAccessory.SNK]              | `N/A`                         | `Optional`                    | `Optional`                    | `Permitted`               |
| [Unattached.Accessory]            | `N/A`                         | `Optional`                    | `N/A`                         | `Not Permitted`           |
| [AttachWait.Accessory]            | `N/A`                         | `Optional`                    | `N/A`                         | `Not Permitted`           |
| [PoweredAccessory]                | `N/A`                         | `Optional`                    | `N/A`                         | `Permitted`               |
| [Unsupported.Accessory] [^9]      | `N/A`                         | `Optional`                    | `N/A`                         | `Not Permitted`           |
| [CTUnattached.VPD]                | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [CTAttachWait.VPD] [^10]          | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [CTAttached.VPD] [^10]            | `N/A`                         | `N/A`                         | `Optional`                    | `Not Permitted`           |
| [CTDisabled.VPD] [^10]            | `N/A`                         | `N/A`                         | `Optional`                    | `Not Permitted`           |
| [CTUnattached.SNK]                | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [CTAttached.SNK] [^11]            | `N/A`                         | `N/A`                         | `Optional`                    | `Permitted`               |
| [CTUnattached.Unsupported] [^10]  | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [CTAttachWait.Unsupported] [^10]  | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [CTTry.SNK] [^10]                 | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [CTAttached.Unsupported] [^10]    | `N/A`                         | `N/A`                         | `Optional`                    | `SOP' Permitted`          |
| [PowerDefault.SNK]                | `N/A`                         | `Mandatory`                   | `Mandatory`                   | `Permitted`               |
| [Power1.5.SNK]                    | `N/A`                         | `Optional`                    | `Optional`                    | `Permitted`               |
| [Power3.O.SNK]                    | `N/A`                         | `Optional`                    | `Optional`                    | `Permitted`               |

[^1]: `Optional` for non-USB4 and non-USB PD implementations.
[^2]: `Optional` for UFP applications that are USB 2.0-only, consume USB Default Power and do not support USB PD or accessories.
[^3]: `Mandatory` for a DFP that was providing VConn in the previous [Attached.SRC] state. `N/A` for a DFP that was not providing VConn in the previous [Attached.SRC] state.
[^4]: [Try.SRC] and [Try.SNK] shall not be supported at the same time, although an unattached device may dynamically choose between [Try.SRC] and [Try.SNK] state machines based on external factors.
[^5]: [TryWait.SNK] is `Mandatory` when [Try.SRC] is supported.
[^6]: [TryWait.SRC] is `Mandatory` when [Try.SNK] is supported.
[^7]: [UnorientedDebugAccessory.SRC] is `Mandatory` for any Source or DRP that supports Debug Accessory Mode.
[^8]: [OrientedDebugAccessory.SRC] is only `Mandatory` if orientation detection is needed in Debug Accessory Mode.
[^9]: [Unsupported.Accessory] is `Mandatory` when [PoweredAccessory] is supported.
[^10]: [CTAttachWait.VPD], [CTAttached.VPD], [CTDisabled.VPD], [Try.SNK], [TryWait.SRC], [CTUnattached.Unsupported], [CTAttachWait.Unsupported], [CTAttached.Unsupported], and [CTTry.SNK] are `Mandatory` when [CTUnattached.VPD] is supported.
[^11]: [CTAttached.SNK] is `Mandatory` when [CTUnattached.SNK] is supported.
