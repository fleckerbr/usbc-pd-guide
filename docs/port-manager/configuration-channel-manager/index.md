# Configuration Channel Manager

The connection state machine is responsible for establishing and managing a Source-to-Sink connection using the CC1 and CC2 pins on the connector.
The functionality of this state machine is described in section `4.5 Configuration Channel (CC)` of the [USB TC] Specification.

``` mermaid
stateDiagram-v2
    Unattached.SRC --> Unattached.SNK: <a href="../../../port-controller/registers/role-control/#drp">DRP</a> and<br>tDRPTransition
    Unattached.SRC --> AttachWait.SRC: Connection<br>Detected

    Unattached.SNK --> Unattached.SRC: <a href="../../../port-controller/registers/role-control/#drp">DRP</a> and<br>tDRPTransition
    Unattached.SNK --> AttachWait.SNK: Connection<br>Detected

    AttachWait.SRC --> Attached.SRC: Source Detected<br>for tCCDebounce<br>and VBus Detected
    AttachWait.SRC --> Unattached.SNK: <a href="../../../port-controller/registers/role-control/#drp">DRP</a> and<br> Connection Removed
    AttachWait.SRC --> Unattached.SRC: Not <a href="../../../port-controller/registers/role-control/#drp">DRP</a> and<br> Connection Removed

    Attached.SRC --> Unattached.SNK: <a href="../../../port-controller/registers/role-control/#drp">DRP</a> and<br>Sink Removed
    Attached.SRC --> Unattached.SRC: Not <a href="../../../port-controller/registers/role-control/#drp">DRP</a> and<br>Sink Removed

    AttachWait.SNK --> Attached.SNK: Source Detected<br>for tCCDebounce<br>and VBus Detected
    AttachWait.SNK --> Unattached.SRC: Connection Removed<br>for tPDDebounce

    Attached.SNK --> Unattached.SNK: VBus<br>Removed
```
