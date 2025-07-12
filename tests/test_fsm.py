import pytest
from fsm_project.fsm.mod_three_fsm import ModThreeFSM


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
