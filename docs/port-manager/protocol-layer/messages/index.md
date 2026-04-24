# Protocol Layer Messages

## Message Discarding

| Message Pending<br>Transmission   | Message Received  | Discard Pending<br>Transmission   |
| :-------------------------------: | :---------------: | :-------------------------------: |
| SOP                               | SOP               | Yes                               |
| SOP                               | SOP'/SOP''        | No                                |
| SOP'/SOP''                        | SOP               | Yes                               |
| SOP'/SOP''                        | SOP'/SOP''        | No                                |

## Ordered Sets

| Ordered Set   | K-code 1      | K-code 2      | K-code 3      | K-code 4      |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| SOP           | Sync-1        | Sync-1        | Sync-1        | Sync-2        |
| SOP'          | Sync-1        | Sync-1        | Sync-3        | Sync-3        |
| SOP''         | Sync-1        | Sync-3        | Sync-1        | Sync-3        |
| SOP' Debug    | Sync-1        | RST-2         | RST-2         | Sync-3        |
| SOP'' Debug   | Sync-1        | RST-2         | Sync-3        | Sync-2        |
| Hard Reset    | RST-1         | RST-1         | RST-1         | RST-2         |
| Cable Reset   | RST-1         | Sync-1        | RST-1         | Sync-3        |
