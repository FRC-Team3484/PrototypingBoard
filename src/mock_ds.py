from typing import override
from commands2 import Subsystem
from socket import socket, AF_INET, SOCK_DGRAM

class MockDriverStation(Subsystem):
    """
    Describes a mock driver station to enable the robot without user input
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.active = False
        self.send_count = 0
        self.init_count = 0
        
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.target_addr = ("127.0.0.1", 1110)

    def start(self):
        self.active = True
        self.send_count = 0
        self.init_count = 0

    def stop(self):
        self.active = False

    @override
    def periodic(self):
        if not self.active:
            return

        packet = self._generate_packet()
        
        try:
            self.sock.sendto(packet, self.target_addr)
        except OSError:
            pass

        self.send_count = (self.send_count + 1) & 0xFFFF


    def _generate_packet(self):
        data: bytearray = bytearray()

        # Sequence number
        data.append((self.send_count >> 8) & 0xFF)
        data.append(self.send_count & 0xFF)

        # Data tag
        data.append(0x01)

        # Enabled flag (0x04 = teleop enabled)
        mode = 0x04

        # First ~10 packets need to be disabled or else the robot won't enable
        if self.init_count < 10:
            mode = 0x00
            self.init_count += 1

        data.append(mode)

        # Data request
        data.append(0x10)

        # Red 1 station
        data.append(0x00)

        return bytes(data)
