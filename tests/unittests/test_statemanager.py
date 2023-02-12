import unittest
from classes.state import State
from classes.statemanager import StateManager


class TestStatemanager(unittest.TestCase):
    """
    I realize after writing a bunch of these tests that I could have had a setUp method
    or something where I initialize a StateManager once instead of initializing one for
    each of the tests.

    I'm going to leave it alone for now as the tests still take like no time to run, but
    that's an optimization that could happen if we need it to.
    """

    # HELPER FUNCTION
    def examine_state_manager_attributes(self, state_manager):
        self.assertEqual(state_manager.current_state, state_manager.state_list[0])
        self.assertEqual(state_manager.state_index, 0)
        self.assertEqual(len(state_manager.state_list), 3)
        for state in state_manager.state_list:
            self.assertEqual(type(state), State)

        # Also do some checks that our states have the correct parameters.
        state_0 = state_manager.state_list[0]
        state_1 = state_manager.state_list[1]
        state_2 = state_manager.state_list[2]

        self.assertEqual(state_0.output, 0)
        self.assertEqual(state_0.zero_input, 0)
        self.assertEqual(state_0.one_input, 1)

        self.assertEqual(state_1.output, 1)
        self.assertEqual(state_1.zero_input, 1)
        self.assertEqual(state_1.one_input, -1)

        self.assertEqual(state_2.output, 2)
        self.assertEqual(state_2.zero_input, -1)
        self.assertEqual(state_2.one_input, 0)

    # Test __init__
    def test_init_success_case(self):
        """
        Whenever we initialize a StateManager, we should have three states in our
        state list, the state index should be 0, and our current state should be
        state 0.
        """
        state_manager = StateManager()
        self.examine_state_manager_attributes(state_manager)

    # Test initialize_states
    def test_initialize_states_success_case(self):
        """
        I will say, I am pretty conflicted on whether or not to include this as a unit
        test. The Technical Exercise Rubric states that I should strive to not have
        redundant code, which I agree with. And given how the init is literally just
        the initialize_states method, I think as of right now, this IS a redundant test.

        However -

        I also believe that there's no such thing as a "bad" test, in the sense that a
        test will never take away value. At worst it just may not add anything.

        Moreover, I would also say a test like this would have value in the event that
        either the init or this method gets changed in the future. Because if this doesn't
        get written now, then, it could be forgotten about later. Like someone could be in
        a hurry and make changes to the initialize_states method and forget to write/look
        at unit tests.

        If these redundant tests already exist, then at the very least it acts as a safety
        check.

        My two cents.
        """
        state_manager = StateManager()
        state_manager.current_state = "One very confused dog."
        state_manager.state_index = 99
        state_manager.state_list = [1, "a", "Pillows"]

        # Even with changing up the variables, initialize_states should
        # give us a clean slate.
        state_manager.initialize_states()
        self.examine_state_manager_attributes(state_manager)

    # Test process_input
    def test_process_input_basic_case(self):
        """
        Testing the process input with a basic test case, such as 41 in binary.
        101001 Modulo 3 will give us two.
        """
        state_manager = StateManager()
        state_manager.process_input("101001")

        self.assertEqual(state_manager.current_state, state_manager.state_list[2])

    def test_process_input_integer_case(self):
        """
        Testing the case where we feed process_input an integer. This wasn't in the
        original scope, but I figure it'd be nice if the Finite State Machine could
        work with binary strings and integer inputs.

        After all, most people would call modulo on an integer input.
        """
        state_manager = StateManager()
        state_manager.process_input(41)

        self.assertEqual(state_manager.current_state, state_manager.state_list[2])

    def test_process_input_float_case(self):
        """
        Handle an input that is a float - I.E., has a decimal value. For now we'll
        just round the values but I acknowledge that we could make changes to the
        logic so we return a decimal value.
        """
        state_manager = StateManager()
        state_manager.process_input(1.2)

        self.assertEqual(state_manager.current_state, state_manager.state_list[1])

    def test_process_input_negative_value_case(self):
        """
        Case where we feed the process_input method a negative value. In the future,
        it'd be possible to make something that accepts negative values, but for now
        we just throw an error.
        """
        state_manager = StateManager()
        with self.assertRaises(TypeError) as context:
            state_manager.process_input(-666)

            self.assertTrue("Please enter Non-Negative Number." in context.exception)

    def test_process_input_negative_binary_value_case(self):
        """
        Attempt to feed process_input a negative binary string. This should still
        fail on account of this being negative.
        """
        state_manager = StateManager()
        with self.assertRaises(TypeError) as context:
            state_manager.process_input("-1101")

            self.assertTrue(
                "Please enter Non-Negative Binary or Hexadecimal input."
                in context.exception
            )

    # Test set_current_state
    def test_set_current_state_success_case(self):
        """
        Standard success case for setting the current state.
        """
        state_manager = StateManager()
        self.assertEqual(state_manager.current_state, state_manager.state_list[0])

        state_manager.set_current_state(state_manager.state_list[1])
        self.assertEqual(state_manager.current_state, state_manager.state_list[1])

    def test_set_current_state_non_state_list_case(self):
        """
        Try to set the current state for a StateManager with a state that is NOT
        in the state_list of the StateManager. This will throw an error.
        """
        state_manager = StateManager()
        evil_state = State(output=64, zero_input=-1, one_input=1)

        with self.assertRaises(ValueError) as context:
            state_manager.set_current_state(evil_state)

            self.assertTrue(
                "Error! Unrecognized State does not exist in state_list"
                in context.exception
            )

    def test_set_current_state_non_state_case(self):
        """
        Try to set the state for a StateManager with something that simply
        isn't a state.

        This includes the meaning of life, unfortunately.
        """
        state_manager = StateManager()
        meaning_of_life = 42

        with self.assertRaises(TypeError) as context:
            state_manager.set_current_state(meaning_of_life)

            self.assertTrue(
                "Error! Cannot set State to be a non-state." in context.exception
            )

    # Test current_state_output
    def test_current_state_output_success_case(self):
        """
        Simple test case where we successfully get the output of our
        current state.
        """
        state_manager = StateManager()
        self.assertEqual(state_manager.current_state_output, 0)

        state_manager.set_current_state(state_manager.state_list[2])
        self.assertEqual(state_manager.current_state_output, 2)

    # Test reset_current_state
    def test_reset_current_state_success_case(self):
        """
        This method call should only ever produce one outcome, so I
        think we can get away with one test.
        """
        state_manager = StateManager()
        state_manager.current_state = "I love Machine Gun Kiss"
        state_manager.state_index = 4

        state_manager.reset_current_state()
        self.assertEqual(state_manager.state_index, 0)
        self.assertEqual(state_manager.current_state, state_manager.state_list[0])
