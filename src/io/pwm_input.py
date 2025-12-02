from wpilib import PWM

class PWMInput:
    """
    Creates a base PWM input

    Parameters:
        channel (int): The channel for the PWM input
    """
    def __init__(self, channel: int) -> None:
        self._channel: int = channel

        self._pwm_input: PWM = PWM(channel)

    def get(self) -> float:
        """
        Returns the value of the PWM input

        Returns:
            float: The value of the PWM input
        """
        return self._pwm_input.getSpeed()