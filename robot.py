from typing import override
import wpilib
from commands2 import TimedCommandRobot
from wpilib import SmartDashboard, DriverStation

from src.io.button_input import ButtonInput
from src.io.motor import Motor
from src.io.pwm_input import PWMInput
from src.mock_driverstation import SocketSubsystem, EnableRobotCommand, DisableRobotCommand

from src.constants import PrototyingBoardConstants as PBC
import src.config

class MyRobot(TimedCommandRobot):
    def __init__(self) -> None:
        super().__init__()

        self._socket            : SocketSubsystem = SocketSubsystem()
        self._motors            : list[Motor] = []
        self._motors_enabled    : list[bool] = []
        self._motors_last_power : list[float] = []

        for i in range(0, PBC.Motors.NUM_MOTORS):
            self._motors.append(Motor(PBC.Motors.MOTOR_CAN_IDS[i]))
            self._motors_last_power.append(0.0)
            self._motors_enabled.append(False)
        # End for

        # self._print_timer: wpilib.Timer = wpilib.Timer()
    # End def

    @override
    def robotPeriodic(self):
        SmartDashboard.putNumber("Battery Voltage", DriverStation.getBatteryVoltage())

    @override
    def disabledInit(self) -> None:
        # self._print_timer.restart()
        # if src.config.MOCK_DS_ENABLED:
        #     print("Running command")
        #     EnableRobotCommand(self._socket, self.isEnabled, disable_packets=50).schedule()

        for i in range(0, PBC.Motors.NUM_MOTORS):
            self._motors_enabled[i] = False
            SmartDashboard.putNumber(f"motor_{i+1}_power", 0.0)
            SmartDashboard.putBoolean(f"motor_{i+1}_en", False)
            SmartDashboard.putNumber(f"motor_{i+1}_gearto", 0)
            SmartDashboard.putBoolean(f"motor_{i+1}_invert", False)
            self._motors_last_power[i] = 0.0
        # End for

    @override
    def disabledPeriodic(self) -> None:
        # if self._print_timer.advanceIfElapsed(0.5):
        #     print("Disabled")
        pass
        
    @override
    def teleopInit(self) -> None:
        # self._print_timer.restart()
        
        for i in range(0, PBC.Motors.NUM_MOTORS):
            self._motors_enabled[i] = False
            SmartDashboard.putNumber(f"motor_{i+1}_power", 0.0)
            SmartDashboard.putBoolean(f"motor_{i+1}_en", False)
            SmartDashboard.putNumber(f"motor_{i+1}_gearto", 0)
            SmartDashboard.putBoolean(f"motor_{i+1}_invert", False)
            self._motors_last_power[i] = 0.0
            self._motors[i].set_power(0.0)
        # End for
    # End def

    @override
    def teleopExit(self) -> None:
        for i in range(0, PBC.Motors.NUM_MOTORS):
            self._motors_enabled[i] = False
            SmartDashboard.putBoolean(f"motor_{i+1}_en", False)
            SmartDashboard.putNumber(f"motor_{i+1}_power", 0.0)
            SmartDashboard.putNumber(f"motor_{i+1}_gearto", 0)
            SmartDashboard.putBoolean(f"motor_{i+1}_invert", False)
            self._motors_last_power[i] = 0.0
            self._motors[i].set_power(0.0)
        # End for
    # End def

    @override
    def teleopPeriodic(self) -> None:
        # if self._print_timer.hasElapsed(10.0):
        #     self._print_timer.stop()
        #     self._print_timer.reset()
        #     print("Enabled for 10 seconds")
        #     print("Disabling robot...")
        #     DisableRobotCommand(self._socket, self.isDisabled).schedule()


        if src.config.MOTORS_ENABLED:
            for i in range(0, PBC.Motors.NUM_MOTORS):
                _pwrEntry = SmartDashboard.getEntry(f"motor_{i+1}_power")
                _enEntry = SmartDashboard.getEntry(f"motor_{i+1}_en")
                _followEntry = SmartDashboard.getEntry(f"motor_{i+1}_gearto")
                _invertEntry = SmartDashboard.getEntry(f"motor_{i+1}_invert")
                
                _power = _pwrEntry.getDouble(0.0)
                _follow : int = _followEntry.getInteger(0)
                _invert : bool = _invertEntry.getBoolean(False)
                self._motors_enabled[i] = _enEntry.getBoolean(False)

                if (_follow > 0):
                    if (_follow == i):
                        _followEntry.setInteger(0)
                    else:
                        self._motors[i].follow(self._motors[_follow])
                    # End if
                # End if

                self._motors[i].invert(_invert)

                if (not self._motors_enabled[i]):
                    _power = 0.0
                    # _pwrEntry.setDouble(_power) # Disabled so we can set motor speed before enabling the motor
                elif (abs(_power) <= PBC.Motors.MOTOR_STOP_THRESHOLD):
                    _power = 0.0
                # End if

                if (not self._motors[i].isFollowing()):
                    self._motors[i].set_power(float(_power))
                # End if

                if (_follow > 0):
                    if (_follow == i):
                        _followEntry.setInteger(0)
                    else:
                        self._motors[_follow].set_power(float(_power))
                        SmartDashboard.putNumber(f"motor_{_follow}_power", _power)
                    # End if
                # End if

            # End for
        # End if
    # End def
# End class