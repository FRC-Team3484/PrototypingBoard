import socket
from typing import Tuple, Callable

from commands2 import Subsystem, Command

from src.request_generator import generate_packet


class SocketSubsystem(Subsystem):
    ADDRESS: Tuple[str, int] = ("127.0.0.1", 1110)

    def __init__(self) -> None:
        super().__init__()
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_data(self, data: bytes) -> None:
        try:
            self._sock.sendto(data, self.ADDRESS)
        except OSError:
            pass

class EnableRobotCommand(Command):
    def __init__(self, socket: SocketSubsystem, is_robot_enabled:Callable[[], bool], max_tries: int = 500, diable_packets: int = 10) -> None:
        super().__init__()
        self.addRequirements(socket)
        self._socket: SocketSubsystem = socket
        self._check_enabled: Callable = is_robot_enabled
        self._max_tries: int = max_tries
        self._disable_packets = diable_packets
        self._n_tries: int = 0
    
    def runsWhenDisabled(self) -> bool:
        return True

    def initialize(self) -> None:
        self._n_tries = 0

    def execute(self) -> None:
        if self._n_tries >= self._max_tries:
            return

        mode = "Disabled"
        if self._n_tries >= self._disable_packets:
            mode = "Enabled"

        packet = generate_packet(
            send_count=self._n_tries,
            mode=mode,
            type="Teleoperated",
            alliance="Red1"
        )
        self._socket.send_data(packet)
        self._n_tries += 1

    def isFinished(self) -> bool:
        return self._check_enabled() or self._n_tries >= self._max_tries
    
    def end(self, interrupted: bool) -> None:
        if interrupted:
            print(f"EnableRobotCommand was interrupted after {self._n_tries} tries.")
        elif self._check_enabled():
            print(f"Robot enabled after {self._n_tries} tries.")
        else:
            print(f"Failed to enable robot after {self._n_tries} tries.")

class DisableRobotCommand(Command):
    def __init__(self, socket: SocketSubsystem, is_robot_disabled:Callable[[], bool], max_tries: int = 500) -> None:
        super().__init__()
        self.addRequirements(socket)
        self._socket: SocketSubsystem = socket
        self._check_disabled: Callable = is_robot_disabled
        self._max_tries: int = max_tries
        self._n_tries: int = 0

    def initialize(self) -> None:
        self._n_tries = 0

    def execute(self) -> None:
        if self._n_tries >= self._max_tries:
            return

        packet = generate_packet(
            send_count=self._n_tries,
            mode="Disabled",
            type="Teleoperated",
            alliance="Red1"
        )
        self._socket.send_data(packet)
        self._n_tries += 1

    def isFinished(self) -> bool:
        return self._check_disabled() or self._n_tries >= self._max_tries
    
    def end(self, interrupted: bool) -> None:
        if interrupted:
            print(f"DisableRobotCommand was interrupted after {self._n_tries} tries.")
        elif self._check_disabled():
            print(f"Robot disabled after {self._n_tries} tries.")
        else:
            print(f"Failed to disable robot after {self._n_tries} tries.")