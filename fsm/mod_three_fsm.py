from fsm_project.fsm.abstract_fsm import AbstractFSM
from pydantic import validate_call, PrivateAttr


class ModThreeFSM(AbstractFSM):
    """
    A concrete Finite State Machine that computes the remainder of a binary string modulo 3.

    This FSM has three states ('s0', 's1', 's2') representing remainders 0, 1, and 2 respectively.
    The alphabet consists of the binary characters '0' and '1'.
    The transition function updates the state based on input bits, simulating mod 3 arithmetic.

    Attributes:
        _finalStateToRemainder (dict[str, str]): A private mapping from each final state
            to its corresponding remainder value as a string.

    Methods:
        processInput(input: str) -> str:
            Processes an input string of binary digits through the FSM,
            returning the final state after processing.

        getRemainder(input: str) -> str:
            Returns the remainder (as a string) of the input binary number modulo 3,
            by running the FSM and mapping the final state to its remainder.
    """

    _finalStateToRemainder: dict[str, str] = PrivateAttr()

    def __init__(self):
        """
        Initializes the ModThreeFSM with predefined states, alphabet, initial state,
        transitions, and the final state to remainder mapping.
        """
        super().__init__(
            states={"s0", "s1", "s2"},
            alphabet={"0", "1"},
            initialState="s0",
            transitions={
                ("s0", "0"): "s0",
                ("s0", "1"): "s1",
                ("s1", "0"): "s2",
                ("s1", "1"): "s0",
                ("s2", "0"): "s1",
                ("s2", "1"): "s2",
            },
            finalStates={"s0", "s1", "s2"},
        )
        self._finalStateToRemainder = {"s0": "0", "s1": "1", "s2": "2"}

    @validate_call
    def getRemainder(self, input: str) -> str:
        """
        Computes the remainder of the binary input string modulo 3 by processing it
        through the FSM and mapping the resulting state to its remainder value.

        Args:
            input (str): A binary string composed of characters '0' and '1'.

        Returns:
            str: The remainder (as a string) of the input binary number modulo 3.

        Raises:
            ValueError: If the input is invalid or transitions are missing during processing or the final state is not in the set of acceptable final states.
            KeyError: If the final state is not found in the remainder mapping.
        """

        remainderState = self.processInput(input)
        return self._finalStateToRemainder[remainderState]
