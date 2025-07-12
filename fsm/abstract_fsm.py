from abc import ABC, abstractmethod
from pydantic import BaseModel


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

    Subclasses must implement the abstract method `processInput` to define how input strings
    are processed through the FSM.
    """

    states: set[str]
    alphabet: set[str]
    initialState: str
    transitions: dict[tuple[str, str], str]

    @abstractmethod
    def processInput(self, input: str) -> str:
        """
        Processes the given input string through the FSM, transitioning between states.

        Args:
            input (str): The input string composed of characters from the FSM's alphabet.

        Returns:
            str: The final state after processing all input characters.

        Raises:
            ValueError: If an input character is not in the FSM's alphabet or
                        if there is no valid transition from the current state
                        for a given input character.
        """
        pass
