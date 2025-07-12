# FSM Project

This project implements a Finite State Machine (FSM) framework in Python. It includes an abstract FSM base class and a concrete example, `ModThreeFSM`, which computes the remainder of a binary string modulo 3.

## Project Structure

```md
fsm_project/
├── fsm/
│ ├── abstract_fsm.py # AbstractFSM base class
│ └── mod_three_fsm.py # ModThreeFSM concrete implementation
└── tests/
└── test_fsm.py # Unit tests for FSM classes
```

## Features

- Abstract FSM base class with strict type validation using Pydantic.
- `ModThreeFSM` example that models modulo 3 remainder calculation using FSM logic.
- Input validation and error handling in FSM processing methods.
- Fully tested with `pytest` and coverage reporting.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/antonbarua/fsm_project.git
   cd fsm_project
   ```

2. Create and activate a conda environment with Python 3.13.2:

   ```bash
   conda create --name fsm_env python=3.13.2
   conda activate fsm_env
   ```

3. Install dependencies:
   ```bash
   conda install pip
   pip install -r ./requirements.txt
   ```

## Usage

You can use the FSM classes by importing them and calling their methods:

```python
from fsm.mod_three_fsm import ModThreeFSM

fsm = ModThreeFSM()
result = fsm.getRemainder("10101")
print(f"Remainder modulo 3: {result}")
```

## Unit tests

You can run the unit tests by running the following commands:

```bash
pytest
pytest --cov=fsm_project
```
