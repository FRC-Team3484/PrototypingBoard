class PrototyingBoardConstants:

    class Motors:
        MOTOR_1_CAN_ID: int = 1
        MOTOR_2_CAN_ID: int = 2
        MOTOR_3_CAN_ID: int = 3
        MOTOR_4_CAN_ID: int = 4

    class PWMInputs:
        PWM_RESET_THRESHOLD: float = 0.05
        
        PWM_1_CHANNEL: int = 1
        PWM_2_CHANNEL: int = 2
        PWM_3_CHANNEL: int = 3
        PWM_4_CHANNEL: int = 4

    class DigitalInputs:
        BUTTON_MOTOR_1_UP_CHANNEL: int = 1
        BUTTON_MOTOR_1_DOWN_CHANNEL: int = 2
        BUTTON_MOTOR_2_UP_CHANNEL: int = 3
        BUTTON_MOTOR_2_DOWN_CHANNEL: int = 4
        BUTTON_MOTOR_3_UP_CHANNEL: int = 5
        BUTTON_MOTOR_3_DOWN_CHANNEL: int = 6
        BUTTON_MOTOR_4_UP_CHANNEL: int = 7
        BUTTON_MOTOR_4_DOWN_CHANNEL: int = 8

        BUTTON_ALL_ON_CHANNEL: int = 9
        BUTTON_ALL_OFF_CHANNEL: int = 10
