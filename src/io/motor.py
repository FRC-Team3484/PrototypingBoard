from phoenix5 import TalonSRX, TalonSRXConfiguration, TalonSRXControlMode

class Motor:
    """
    Defines a base motor controlled by a TalonSRX

    Parameters:
        can_id (int): The CAN ID of the TalonSRX
        can_bus (str): The CAN bus to use
    """
    def __init__(self, can_id: int, can_bus: str = "rio") -> None:
        self._can_id: int = can_id

        self._motor: TalonSRX = TalonSRX(can_id, can_bus)
        self._motor_config: TalonSRXConfiguration = TalonSRXConfiguration()

    def set_power(self, power: float) -> None:
        """
        Sets the power of the motor

        Parameters:
            power (float): The power to set
        """
        self._motor.set(TalonSRXControlMode.Current, power)