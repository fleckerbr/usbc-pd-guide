from __future__ import annotations

from usb.port_controller import Register

from .alert import Alert
from .alert_extended import AlertExtended
from .alert_extended_mask import AlertExtendedMask
from .alert_mask import AlertMask
from .cc_status import CCStatus
from .command import Command
from .configure_extended_1 import ConfigureExtended1
from .configure_standard_output import ConfigureStandardOutput
from .device_capabilities_1 import DeviceCapabilities1
from .device_capabilities_2 import DeviceCapabilities2
from .device_capabilities_3 import DeviceCapabilities3
from .device_id import DeviceID
from .extended_status import ExtendedStatus
from .extended_status_mask import ExtendedStatusMask
from .fault_control import FaultControl
from .fault_status import FaultStatus
from .fault_status_mask import FaultStatusMask
from .generic_timer import GenericTimer
from .message_header_info import MessageHeaderInfo
from .pd_interface_rev import PDInterfaceRev
from .power_control import PowerControl
from .power_status import PowerStatus
from .power_status_mask import PowerStatusMask
from .product_id import ProductID
from .receive_buffer import ReceiveBuffer
from .receive_detect import ReceiveDetect
from .role_control import RoleControl
from .standard_input_capabilities import StandardInputCapabilities
from .standard_output_capabilities import StandardOutputCapabilities
from .tcpc_control import TcpcControl
from .transmit import Transmit
from .transmit_buffer import TransmitBuffer
from .usbpd_rev_ver import USBPDRevVer
from .usbtypec_rev import USBTypeCRev
from .vbus_nondefault_target import VBusNondefaultTarget
from .vbus_sink_disconnect_threshold import VBusSinkDisconnectThreshold
from .vbus_stop_discharge_threshold import VBusStopDischargeThreshold
from .vbus_voltage import VBusVoltage
from .vbus_voltage_alarm_hi_cfg import VBusVoltageAlarmHiCfg
from .vbus_voltage_alarm_lo_cfg import VBusVoltageAlarmLoCfg
from .vendor_defined import VendorDefined
from .vendor_id import VendorID

__all__ = (
    "Register",
    "Alert",
    "AlertExtended",
    "AlertExtendedMask",
    "AlertMask",
    "CCStatus",
    "Command",
    "ConfigureExtended1",
    "ConfigureStandardOutput",
    "DeviceCapabilities1",
    "DeviceCapabilities2",
    "DeviceCapabilities3",
    "DeviceID",
    "ExtendedStatus",
    "ExtendedStatusMask",
    "FaultControl",
    "FaultStatus",
    "FaultStatusMask",
    "GenericTimer",
    "MessageHeaderInfo",
    "PDInterfaceRev",
    "PowerControl",
    "PowerStatus",
    "PowerStatusMask",
    "ProductID",
    "ReceiveBuffer",
    "ReceiveDetect",
    "RoleControl",
    "StandardInputCapabilities",
    "StandardOutputCapabilities",
    "TcpcControl",
    "Transmit",
    "TransmitBuffer",
    "USBPDRevVer",
    "USBTypeCRev",
    "VBusNondefaultTarget",
    "VBusSinkDisconnectThreshold",
    "VBusStopDischargeThreshold",
    "VBusVoltage",
    "VBusVoltageAlarmHiCfg",
    "VBusVoltageAlarmLoCfg",
    "VendorDefined",
    "VendorID",
)

if __name__ == "__main__":
    for register in Register.subclasses():
        print(register)
        for field in register:
            print(f"  - {field}")
