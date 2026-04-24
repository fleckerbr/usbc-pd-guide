# USB-C Architecture

Unlike the USB Power Delivery Specification, this architecture described in this guide is not going to focus on an abstract logical system architecture.
Instead, the focus will be on one specific implementation of the USB stack with the following objectives:

!!! abstract "Architectural Design Objectives"
    1. The design shall adhere to the requirements from Revision 2.3 of the USB-C Cable and Connector Specification
        - USB4 support not included
        - USB-C cable alternate modes not included
    2. All Host-to-Device configurations from Section 2.3.3 of the USB-C Cable and Connector Specification shall be supported
        - Source-only, Sink-only, and Dual-Role-Power (DRP) ports are supported
        - DFP-only, UFP-only, and Dual-Role-Data (DRD) ports are supported
    3. The Type-C Port Manager (TCPM) shall support USB Power Delivery Revision 3.2
        - 240W power range support
    4. The design shall implement Revision 2.0 of the USB Type-C Port Controller Interface Specification
        - Dedicated Type-C Port Controller (TCPC) hardware will be used in the design
    5. The USB Type-C Connector System Software Interface (UCSI) Revision 3.0 shall be considered
        - Full support for UCSI may not be included, but the design shall allow it to be added at a later time
    6. The architecture shall be primarially designed for power providers and consumers
        - USB Power Delivery Hubs and other peripherals need not be considered

To accomplish these objectives, the system architecture depicted in the following figure was conceived.
The remaining sections will provide a summary of each of the components named in this architectural overview and describe how they relate to other systems defined in official USB specifications.

![USB-C High Level Architecture View](assets/usbc-architecture-dark.png#only-dark)
![USB-C High Level Architecture View](assets/usbc-architecture-light.png#only-light)

## Type-C Port Controller

The USB Power Delivery (PD) architectural overview describes a communications stack that consists of the following layers:[^1]

- A Device Policy Manager
- A Policy Engine
- A Protocol Layer
- A Physical Layer

A Type-C Port Controller (TCPC) exists to encapsulate the Physical (PHY) layer and part of the Protocol (PRL) layer in addition to VBus and VConn power controls,
USB-C Configuration Channel (CC) logic, and USB PD Biphase Mark Coding (BMC).[^2]

Although there is a standardized interface for communication between a TCPC and TCPM, the Type-C Port Controller Interface (TCPCI) allows for a variety of vendor defined features
which will generally require custom handling. Handling for these vendor defined featues will be discussed in the following [Type-C Port Controller Interface](#type-c-port-controller-interface)
and [Configuration Channel Manager](#configuration-channel-manager) sections.

!!! note "Power Path Controller"
    In theory the TCPC should control power routing from a device's power system to the physical port connector and therefore if [COMMAND.SourceVBusDefaultVoltage] or [COMMAND.SinkVBus] is sent,
    no further action should be necessary at the firmware level to begin sourcing or sinking power.

    However, since power routing is hardware dependent, the TCPC may not always have the ability to direct power as necessary.
    In this scenario, power routing shall be handled by the Device Policy Manager as the USB-C port should not be tied to the Power System directly.

## Type-C Port Controller Interface

The TCPCI Specification defines the port controller interface as the I2C interface between the TCPC and TCPM.[^2]
In the architecture used by this guide, the scope of this interface has been expanded to include the TCPM-side logic for handling and dispaching messages to and from the port controller.

From a firmware developer's perspective, the TCPCI should largely function as an API where various calls can be made to read the various registers defined in the TCPCI Specification.
However, the TCPCI is also responsible for monitoring the TCPC's [Alert#] pin and automatically collecting the relevant data based on the type of alert in the [ALERT] and nested alert registers as needed.

As the TCPCI is responsible for alert detection in this architecture, it is also solely responsible for managing alert masks and as such, mask registers should not need to be exposed in the TCPCI's API.
However, they may be still be exposed for debugging purposes.

## Configuration Channel Manager

The Configuration Channel (CC) Manager is the foundational manager for a USB-C Port.[^3] It is responsible for managing the initial connection between a USB-C port and its port partner.

!!! warning "USB-C Cable and Connnector Connection State Diagrams"
    Although the USB-C Cable and Connector Specification has state diagrams and state summaries documenting the implementation of a CC state machine,
    these diagrams are not accurate in a system that incorporated a dedicated TCPC.[^4]

    Despite this, the Cable and Connector specification is the only place that defines which CC states are optional, mandatory, and allow USB PD communication for each port type.
    This guide will provide an alternate CC state machine designed for use with a TCPC in the detailed section covering the CC Manager.

After the CC Manager confirms that the TCPC is attached in a state that allows for USB PD communication, it shall then enable the PD Policy Engine and Protocol Layer

## Protocol Layer

The purpose of the Protocol (PRL) Layer is to process both incoming and outgoing PD messages for the Policy Engine (PE) and functions exactly as defined by the USB PD Specification.
In some cases it may be necessary to break up messages into chunks and for this reason the Protocol Layer defines an inner Layer known as the Chunking Layer which is composed of the three following state machines:[^5]

- Chunked RX
- Chunked Tx
- Chunked Message Router

As a result of this design the Policy Engine only needs to handle un-chunked messages and will not receive a message until all related chunks have been collated.

## Policy Engine

Each USB-C port has a dedicated Policy Engine that interacts with the Device Policy Manager to implement the port's Local Policy.[^6]

## Device Policy Manager

The Device Policy Manager (DPM) is responsible for managing the behavior of all local USB-C ports.
It shall have knowledge about the capabilities of the device's power system and the individual ports as well as live information about changes in its capabilities and shall be able to request power supply changes.

[^1]: `Section 2.6` `Architectural Overview` - [USB PD R3.2 V1.0]
[^2]: `Section 2.2` `USB Type-C Port Controller (TCPC) Interface` - [USB TCPCI R2.0 V1.3]
[^3]: `Section 4.5` `Configuration Channel (CC)` - [USB TC R2.3]
[^4]: `Section 4.5.2.1` `Connection State Diagrams` - [USB TC R2.3]
[^5]: `Section 6.12.2.1.1` `Architecture of Device Including Chunking Layer` - [USB PD R3.2 V1.0]
[^6]: `Section 8.3` `Policy Engine` - [USB PD R3.2 V1.0]
