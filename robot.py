from typing import override
from wpilib import TimedRobot

from src.io.button_input import ButtonInput
from src.io.motor import Motor
from src.io.pwm_input import PWMInput
from src.mock_ds import MockDS

from src.constants import PrototyingBoardConstants
import src.config

class MyRobot(TimedRobot):
    def __init__(self) -> None:
        super().__init__()

        self._mock_ds: MockDS = MockDS()
        self._motor_1: Motor = Motor(PrototyingBoardConstants.Motors.MOTOR_1_CAN_ID)
        self._motor_2: Motor = Motor(PrototyingBoardConstants.Motors.MOTOR_2_CAN_ID)
        self._motor_3: Motor = Motor(PrototyingBoardConstants.Motors.MOTOR_2_CAN_ID)
        self._motor_4: Motor = Motor(PrototyingBoardConstants.Motors.MOTOR_2_CAN_ID)

        self._pwm_1: PWMInput = PWMInput(PrototyingBoardConstants.PWMInputs.PWM_1_CHANNEL)
        self._pwm_2: PWMInput = PWMInput(PrototyingBoardConstants.PWMInputs.PWM_2_CHANNEL)
        self._pwm_3: PWMInput = PWMInput(PrototyingBoardConstants.PWMInputs.PWM_3_CHANNEL)
        self._pwm_4: PWMInput = PWMInput(PrototyingBoardConstants.PWMInputs.PWM_4_CHANNEL)

        self._button_motor_1_up: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_1_UP_CHANNEL)
        self._button_motor_1_down: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_1_DOWN_CHANNEL)
        self._button_motor_2_up: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_2_UP_CHANNEL)
        self._button_motor_2_down: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_2_DOWN_CHANNEL)
        self._button_motor_3_up: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_3_UP_CHANNEL)
        self._button_motor_3_down: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_3_DOWN_CHANNEL)
        self._button_motor_4_up: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_4_UP_CHANNEL)
        self._button_motor_4_down: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_MOTOR_4_DOWN_CHANNEL)

        self._button_all_on: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_ALL_ON_CHANNEL)
        self._button_all_off: ButtonInput = ButtonInput(PrototyingBoardConstants.DigitalInputs.BUTTON_ALL_OFF_CHANNEL)

    @override
    def robotInit(self) -> None:
        if src.config.MOCK_DS_ENABLED:
            self._mock_ds.start()

    @override
    def teleopPeriodic(self) -> None:
        if src.config.MOTORS_ENABLED:
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