# PrototyingBoard
A codebase for using our prototyping board, written in Python

- 1x RoboRIO 1.0
- 4x Talon SRX Motor Controllers
- 4x PWM inputs
  - For each, positive powers the motor up, negative powers the motor down
- 10 digital inputs
  - 2 for each motor, one steps up 5%, the other steps down 5%
  - The other two buttons sets all to 50%, and the other sets all to 0%

## Installing
Clone this repository:
```bash
git clone https://github.com/FRC-Team3484/PrototypingBoard
```

Create a virtual environment:
```bash
python -m venv .venv
```

Activate it:
```bash
source ./.venv/bin/activate # Linux
```

Install the dependencies:
```bash
pip install -r requirements.py
```

And download the RoboRIO libraries:
```bash
robotpy sync
```

## Usage
Test your code using:
```bash
robotpy test
```

And deploy it to a RoboRIO using:
```bash
robotpy deploy
```

## To-Do
- [ ] Create base motor class
- [ ] Create base digital input class
- [ ] Create base PWM input class
- [ ] Connect together in `robot.py`
- [ ] Use `PowerMotor` from `FRC3484_Lib` instead