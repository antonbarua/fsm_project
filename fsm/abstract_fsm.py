from abc import ABC
from pydantic import BaseModel, validate_call


class AbstractFSM(BaseModel, ABC):
    """
    Abstract base class for a Finite State Machine (FSM).

    This class defines the core structure of an FSM with the following components:

    Attributes:
        states (set[str]): A finite set of states in the FSM.
        alphabet (set[str]): A finite set of input symbols the FSM recognizes.
        initialState (str): The starting state of the FSM.
        transitions (dict[tuple[str, str], str]): Mapping from (state, input_symbol) tuples
            to the next state, representing all valid state transitions.
        finalStates (set[str]): A finite set of states in the FSM that includes all the valid final states of the FSM.

    Subclasses must implement the methods to map the finalState to the requisite output.
    """

    states: set[str]
    alphabet: set[str]
    initialState: str
    transitions: dict[tuple[str, str], str]
    finalStates: set[str]

    @validate_call
    def processInput(self, input: str) -> str:
        """
        Processes the input string through the FSM, transitioning between states
        according to the FSM's transition rules.

        Args:
            input (str): The input string composed of characters from the FSM's alphabet.


        Returns:
            str: The final state of the FSM after processing the input string.

        Raises:
            ValueError: If the input contains characters not in the alphabet,
                        or if a transition for a given input from the current state does not exist.
        """
        input = input.strip()
        currentState = self.initialState

        for char in input:
            if char not in self.alphabet:
                raise ValueError(f"Invalid input character '{char}'")
            nextState = self.transitions.get((currentState, char))
            if nextState is None:
                raise ValueError(
                    f"No transition from state '{currentState}' on input '{char}'"
                )
            currentState = nextState

        if currentState not in self.finalStates:
            raise ValueError(
                f"The final state: ${currentState} is not in the list of acceptable final states"
            )

        return currentState
