from typing import override
from wpilib import TimedRobot

from src.button_input import ButtonInput
from src.motor import Motor
from src.pwm_input import PWMInput
from src.mock_ds import MockDS

class MyRobot(TimedRobot):
    def __init__(self) -> None:
        super().__init__()

        self._mock_ds: MockDS = MockDS()
        self._motor_1: Motor = Motor(1)
        self._motor_2: Motor = Motor(2)
        self._motor_3: Motor = Motor(3)
        self._motor_4: Motor = Motor(4)

        self._pwm_1: PWMInput = PWMInput(1)
        self._pwm_2: PWMInput = PWMInput(2)
        self._pwm_3: PWMInput = PWMInput(3)
        self._pwm_4: PWMInput = PWMInput(4)

        self._button_motor_1_up: ButtonInput = ButtonInput(1)
        self._button_motor_1_down: ButtonInput = ButtonInput(2)
        self._button_motor_2_up: ButtonInput = ButtonInput(3)
        self._button_motor_2_down: ButtonInput = ButtonInput(4)
        self._button_motor_3_up: ButtonInput = ButtonInput(5)
        self._button_motor_3_down: ButtonInput = ButtonInput(6)
        self._button_motor_4_up: ButtonInput = ButtonInput(7)
        self._button_motor_4_down: ButtonInput = ButtonInput(8)

        self._button_all_on: ButtonInput = ButtonInput(9)
        self._button_all_off: ButtonInput = ButtonInput(10)

    @override
    def robotInit(self) -> None:
        self._mock_ds.start()

    @override
    def teleopPeriodic(self) -> None:
        self._motor_1.set_power(self._pwm_1.get())
        self._motor_2.set_power(self._pwm_2.get())
        self._motor_3.set_power(self._pwm_3.get())
        self._motor_4.set_power(self._pwm_4.get())

        if self._button_all_on.get():
            self._motor_1.set_power(0.5)
            self._motor_2.set_power(0.5)
            self._motor_3.set_power(0.5)
            self._motor_4.set_power(0.5)

        if self._button_all_off.get():
            self._motor_1.set_power(0)
            self._motor_2.set_power(0)
            self._motor_3.set_power(0)
            self._motor_4.set_power(0)

        if self._button_motor_1_up.get():
            self._motor_1.set_power(0.5)

        if self._button_motor_1_down.get():
            self._motor_1.set_power(-0.5)

        if self._button_motor_2_up.get():
            self._motor_2.set_power(0.5)

        if self._button_motor_2_down.get():
            self._motor_2.set_power(-0.5)

        if self._button_motor_3_up.get():
            self._motor_3.set_power(0.5)

        if self._button_motor_3_down.get():
            self._motor_3.set_power(-0.5)

        if self._button_motor_4_up.get():
            self._motor_4.set_power(0.5)

        if self._button_motor_4_down.get():
            self._motor_4.set_power(-0.5)