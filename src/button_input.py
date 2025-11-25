from wpilib import DigitalInput

class ButtonInput:
    """
    Creates a base digital input

    Parameters:
        channel (int): The channel for the digital input
    """
    def __init__(self, channel: int) -> None:
        self._channel: int = channel

        self._digital_input: DigitalInput = DigitalInput(channel)

    def get(self) -> bool:
        """
        Returns the value of the digital input

        Returns:
            bool: The value of the digital input
        """
        return self._digital_input.get()
