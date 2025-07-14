import pytest
from fsm_project.fsm.abstract_fsm import AbstractFSM
from fsm_project.fsm.mod_three_fsm import ModThreeFSM
from pydantic import ValidationError


def test_valid_inputs():
    fsm = ModThreeFSM()
    assert fsm.getRemainder("0") == "0"  # s0 -> s0
    assert fsm.getRemainder("1") == "1"  # s0 -> s1
    assert fsm.getRemainder("11") == "0"  # s0->s1->s0
    assert fsm.getRemainder("101") == "2"  # s0->s1->s0->s2


def test_input_with_spaces():
    fsm = ModThreeFSM()
    assert fsm.getRemainder(" 101 ") == "2"  # leading/trailing spaces stripped


def test_empty_input():
    fsm = ModThreeFSM()
    # Empty input means no transitions; stays in initialState "s0"
    assert fsm.getRemainder("") == "0"


def test_invalid_character_in_input():
    fsm = ModThreeFSM()
    with pytest.raises(ValueError, match="Invalid input character 'a'"):
        fsm.getRemainder("10a1")


def test_missing_transition():
    fsm = ModThreeFSM()
    # Remove one transition to simulate missing transition
    fsm.transitions.pop(("s1", "1"))
    with pytest.raises(ValueError, match="No transition from state 's1' on input '1'"):
        fsm.getRemainder("11")


def test_process_input_strips_and_validates():
    fsm = ModThreeFSM()
    assert fsm.processInput(" 101 ") == fsm.processInput("101")
    with pytest.raises(ValueError, match="Invalid input character 'x'"):
        fsm.processInput("10x1")


def test_invalid_nonstring_input():
    fsm = ModThreeFSM()
    with pytest.raises(
        ValidationError,
        match="Input should be a valid string",
    ):
        fsm.processInput(123)
    with pytest.raises(
        ValidationError,
        match="Input should be a valid string",
    ):
        fsm.getRemainder(123)


def test_invalid_final_input():
    class BrokenFSM(AbstractFSM):
        """
        FSM that ends in a state not declared as final.
        Used only for testing invalid final state logic.
        """

        def __init__(self):
            super().__init__(
                states={"start", "mid", "end"},
                alphabet={"a", "b"},
                initialState="start",
                transitions={
                    ("start", "a"): "mid",
                    ("mid", "b"): "end",
                },
                finalStates={"start", "mid"},  # 'end' is intentionally not listed
            )

    fsm = BrokenFSM()
    # input 'ab' leads to state 'end', which is not in finalStates
    with pytest.raises(
        ValueError,
        match="The final state: \\$end is not in the list of acceptable final states",
    ):
        fsm.processInput("ab")
