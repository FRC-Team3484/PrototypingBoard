from typing import Literal

REQUEST_RESTART_CODE = 0x04
REQUEST_REBOOT = 0x08
REQUEST_NORMAL = 0x00

TAG_COMM_VERSION = 0x01
FMS_COMM_VERSION = 0x00

TELEOPERATED = 0x00
TEST = 0x01
AUTONOMOUS = 0x02
ENABLED = 0x04
EMERGENCY_STOP = 0x80

FMS_CONNECTED = 0x08
FMS_RADIO_PING = 0x10
FMS_ROBOT_PING = 0x08
FMS_ROBOT_COMMS = 0x20

RTAG_CAN_INFO = 0x0E
RTAG_CPU_INFO = 0x05
RTAG_RAM_INFO = 0x06
RTAG_DISK_INFO = 0x04

REQUEST_TIME = 0x01
ROBOT_HAS_CODE = 0x20

TAG_DATE = 0x0F
TAG_JOYSTICK = 0x0C
TAG_TIMEZONE = 0x10

RED1 = 0x00
RED2 = 0x01
RED3 = 0x02
BLUE1 = 0x03
BLUE2 = 0x04
BLUE3 = 0x05

def generate_packet( \
        send_count: int, \
        mode:Literal["Enabled", "Disabled", "E-Stop"] = "Disabled", \
        type:Literal["Teleoperated", "Autonomous", "Test"] = "Teleoperated", \
        alliance:Literal["Red1", "Red2", "Red3", "Blue1", "Blue2", "Blue3"] = "Red1" \
        ) -> bytes:
    
    count_bytes_upper: int = (send_count >> 8) & 0xFF
    count_bytes_lower: int = send_count & 0xFF

    data_tag: int = 0x01

    mode_byte: int = 0x00
    if mode == "Enabled":
        mode_byte |= ENABLED
    elif mode == "E-Stop":
        mode_byte |= EMERGENCY_STOP
    if type == "Teleoperated":
        mode_byte |= TELEOPERATED
    elif type == "Autonomous":
        mode_byte |= AUTONOMOUS
    elif type == "Test":
        mode_byte |= TEST

    request_type: int = 0x10

    alliance_byte: int = {"Red1": RED1, "Red2": RED2, "Red3": RED3, "Blue1": BLUE1, "Blue2": BLUE2, "Blue3": BLUE3}[alliance]

    return bytes([
        count_bytes_upper,
        count_bytes_lower,
        data_tag,
        mode_byte,
        request_type,
        alliance_byte
    ])