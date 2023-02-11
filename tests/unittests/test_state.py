import unittest
from classes.state import State


class TestState(unittest.TestCase):
    """
    The State class isn't overly complicated, but we can still ensure that when being
    initialized, it only does so with integers. In otherwords, type checking.
    """

    def test_init_success_case(self):
        state = State(output=0, zero_input=0, one_input=1)

        self.assertEqual(state.output, 0)
        self.assertEqual(state.zero_input, 0)
        self.assertEqual(state.one_input, 1)

    def test_init_incorrect_type_case(self):
        """
        There COULD be a scenario where we need to make States that utilize floats,
        but for now we don't which is why I'm making them a "bad" input.
        """
        with self.assertRaises(TypeError) as context:
            State(output=0.12, zero_input=0, one_input=1)

            self.assertTrue(
                "Error! Cannot initialize State with non-integer input."
                in context.exception
            )

        with self.assertRaises(TypeError) as context:
            State(output=0, zero_input="Oh no! It's Paul Rudd again!", one_input=1)

            self.assertTrue(
                "Error! Cannot initialize State with non-integer input."
                in context.exception
            )

        with self.assertRaises(TypeError) as context:
            State(
                output=0,
                zero_input=0,
                one_input=State(output=0, zero_input=0, one_input=1),
            )

            self.assertTrue(
                "Error! Cannot initialize State with non-integer input."
                in context.exception
            )
