from socket import socket, AF_INET, SOCK_DGRAM
import threading
import time

class MockDS:
    """
    Describes a mock driver station to enable the robot without user input
    """
    def __init__(self) -> None:
        self._active: bool = False
        self._thread: threading.Thread | None = None

    def _generate_packet(self, send_count: int, enabled: bool) -> bytes:
        data: bytearray = bytearray()
        data.append((send_count >> 8) & 0xFF)
        data.append(send_count & 0xFF)
        data.append(0x01)           # general data tag
        data.append(0x04 if enabled else 0x00)
        data.append(0x10)           # normal data request
        data.append(0x00)           # red 1 station
        return bytes(data)

    def start(self) -> None:
        """
        Starts the mock driver station, and tries to enable the robot
        """
        if self._active:
            return
        self._active = True

        def run() -> None:
            sock: socket = socket(AF_INET, SOCK_DGRAM)
            send_count = 0
            next_time: float = time.perf_counter()

            packet: bytes
            send_count: int

            for _ in range(10):
                if not self._active:
                    break

                packet = self._generate_packet(send_count, enabled=False)
                send_count = (send_count + 1) & 0xFFFF

                _ = sock.sendto(packet, ("127.0.0.1", 1110))

                next_time += 0.020
                time.sleep(max(0, next_time - time.perf_counter()))

            while self._active:
                packet = self._generate_packet(send_count, enabled=True)
                send_count = (send_count + 1) & 0xFFFF
                _ = sock.sendto(packet, ("127.0.0.1", 1110))

                next_time += 0.020
                time.sleep(max(0, next_time - time.perf_counter()))

            sock.close()

        self._thread = threading.Thread(target=run, daemon=True)
        self._thread.start()

    def stop(self):
        """
        Shuts down the mock driver station
        """
        self._active = False
        if self._thread and self._thread.is_alive():
            self._thread.join()
