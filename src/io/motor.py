from __future__ import annotations
from phoenix5 import TalonSRX, TalonSRXConfiguration, TalonSRXControlMode, FollowerType


class Motor:
    """
    Defines a base motor controlled by a TalonSRX

    Parameters:
        can_id (int): The CAN ID of the TalonSRX
        can_bus (str): The CAN bus to use
    """
    def __init__(self, can_id: int) -> None:
        self._can_id: int = can_id

        self._motor: TalonSRX = TalonSRX(can_id)
        self._motor_config: TalonSRXConfiguration = TalonSRXConfiguration()
        self._following = 0
    # End def

    def set_power(self, power: float) -> None:
        """
        Sets the power of the motor

        Parameters:
            power (float): The power to set
        """
        self._motor.set(TalonSRXControlMode.PercentOutput, power)
    # End def

    def follow(self, master : int) -> None:
        self._following = master
    # End def

    def isFollowing(self) -> bool:
        return (self._following > 0)
    # End def

    def invert(self, invert : bool) -> None:
        self._motor.setInverted(invert)
    # End def

    def GetIMotorController(self) -> TalonSRX:
        return self._motor
    # End def
# End class