# PrototyingBoard
A codebase for using our prototyping board, written in Python.

- 1x RoboRIO 1.0
- 4x Talon SRX Motor Controllers
- 4x PWM inputs
- 10 digital inputs

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


