# Alert Handling

Whenever the TCPC issues pulls the [Alert#] output pin low (asserts [Alert#]), it simply indicates that a status change has occurred.
While the status change may be caused by errors, alerts are also responsible for reporting events such as the discovery of a possible USB connection.

This topic was written based on Revision 2.0, Version 1.3 of the [USB TCPCI] Specification and aims to cover all the alerts listed in the specification
and provide recommendations on how they might be handled effectively.

## Alerts and Nested Alerts

!!! note inline end
    An alert refers to any status change that the TCPC can communicate back to the TCPM without the TCPM initiating I2C communcations.

Whenever the TCPC pulls the [Alert#] pin low, this indicates that one or more of the [ALERT] register's unmasked flags have been set.
This does *not* necessarially mean that an error has occured although alerts can be used to comunicate fault conditions.

In addition to the [ALERT] register, the TCPCI Specification lists at least four[^1] other alert registers that it classified as nested alerts:

-   [ALERT_EXTENDED]
-   [EXTENDED_STATUS]
-   [FAULT_STATUS]
-   [POWER_STATUS]

The distinguishing factor between alert registers and other registers is that alert registers can be masked to prevent asserting the [Alert#] pin.

!!! warning "Masking Alerts vs Nested Alerts"
    Although masking an alert or nested alert flag that is unset will prevent the [Alert#] pin from being asserted,
    the behavior when masking a flag that is already set differs between alert and nested alert registers.

    Masking an alert flag will [silence](#silencing-an-alert) the alert if no other unmasked alert flags are set; however,
    the same is not true when masking a nested alert since since nested alerts set two alert flags.
    For instance, if [POWER_STATUS.SourcingVBus] is set [ALERT.PowerStatus] will also be set.

## Silencing an Alert

When the TCPC asserts [Alert#], there are two ways of de-asserting the alert.

The first option is to simply clear the the alert source by writing a `1b` to all unmasked alert flags that are asserted.
However there may be cases where an alert has not yet been fully handled but you still want to receive an interrupt if another alert is raised
(e.g. detection of [ALERT_EXTENDED.TimerExpired] while [ALERT.CCStatus] is still asserted during the port initialization and connection sequence).

Therefore, the second option is to simply mask the alerts in the [ALERT_MASK] register that have already been seen as this should de-assert the [Alert#] pin of the TCPC.

[^1]: In addition to the four required nested alerts, TCPC vendors can define additional nested alerts in the [VENDOR_DEFINED] registers.
    If the vendor does include additional alerts, they should be handled whenever the [ALERT.VendorDefinedAlert] flag is set.
