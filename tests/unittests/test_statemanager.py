import unittest
from classes.state import State
from classes.statemanager import StateManager


class TestStatemanager(unittest.TestCase):

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
    # TODO: This will be the meat and potatoes, I think.

    # Test sanitize_input
    # TODO: This will come in the future.

    # Test set_current_state
    def test_set_current_state_success_case(self):
        """
        Standard success case for setting the current state.
        """
        state_manager = StateManager()
        self.assertEqual(state_manager.current_state, state_manager.state_list[0])

        state_manager.set_current_state(state_manager.state_list[1])
        self.assertEqual(state_manager.current_state, state_manager.state_list[1])
