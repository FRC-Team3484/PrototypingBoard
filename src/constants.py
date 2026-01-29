class PrototyingBoardConstants:

    class Motors:
        MOTOR_STOP_THRESHOLD: float = 0.02
        NUM_MOTORS : int = 4

        MOTOR_CAN_IDS : list[int] = [ i+1 for i in range (0, NUM_MOTORS, 1) ]
        # MOTOR_CAN_IDS: int = 2
        # MOTOR_CAN_IDS: int = 3
        # MOTOR_CAN_IDS: int = 4

    class PWMInputs:
        PWM_RESET_THRESHOLD: float = 0.05
        NUM_PWM_CHANNELS : int = 4
        
        PWM_CHANNEL_ID : list[int] = [ i+1 for i in range (1, NUM_PWM_CHANNELS, 1) ]
        # PWM_2_CHANNEL: int = 2
        # PWM_3_CHANNEL: int = 3
        # PWM_4_CHANNEL: int = 4

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
