import unittest
from unittest.mock import patch

from main import execute, modulo_three
from classes.statemanager import StateManager

"""
Tests that are meant to represent "end-to-end" tests.
"""


class TestModuloThree(unittest.TestCase):
    def test_modulo_three_success_case(self):
        """
        Test case where we give the modulo three function the input string of "11011" (which is 27),
        and an initialized State Manager. We should get an output of zer0.
        """
        test_input = "11011"
        state_manager = StateManager()

        self.assertEqual(modulo_three(test_input, state_manager), 0)

    def test_modulo_three_40000_case(self):
        """
        40000 in binary is "1001110001000000". According to Google, 40000 Mod 3 is one.

        But now I know you guys are going to question me because I said I'm good at Math but
        I looked this up on Google.
        13333 * 3 = 39999.
        40000 - 39999 = 1.

        Hopefully that clears my name?
        """
        test_input = "1001110001000000"
        state_manager = StateManager()

        self.assertEqual(modulo_three(test_input, state_manager), 1)

    def test_modulo_three_integer_40000_case(self):
        """
        Test case where we feed the modulo three function the int 40000.

        Luckily I didn't need Google to tell me that 40000, so I should be safe from your
        scrutiny for now.
        """
        test_input = 40000
        state_manager = StateManager()

        self.assertEqual(modulo_three(test_input, state_manager), 1)

    def test_modulo_three_bad_state_manager_case(self):
        """
        Test case where we have an "invalid" StateManager.

        Paul Rudd is a constant source of amusement to me, but he ain't no StateManager.
        """
        test_input = "11011"
        state_manager = "Paul Rudd is an incredibly sexy beast. An absolute unit."

        with self.assertRaises(TypeError) as context:
            modulo_three(test_input, state_manager)

            # Paul Rudd is a string?
            self.assertTrue(
                "Error! Invalid StateManager! Cannot run modulo_three with str"
                in context.exception
            )

    def test_modulo_three_bad_string_input_case(self):
        """
        Test case where we feed the modulo three method a nonsensical string.
        This shouldn't work for obvious reasons.
        """
        schmuck_bait = "https://www.youtube.com/watch?v=VD6__C2Ht6M"
        state_manager = StateManager()

        with self.assertRaises(TypeError) as context:
            modulo_three(schmuck_bait, state_manager)

            self.assertTrue(
                "Please enter Non-Negative Binary or Hexadecimal input."
                in context.exception
            )

    def test_modulo_three_hexidecimal_case(self):
        """
        Call the modulo three method with a hexadecimal value. In this case we'll use "FE", which
        is 254. 254 Modulo 3 will be 2.
        """
        test_input = "FE"
        state_manager = StateManager()

        self.assertEqual(modulo_three(test_input, state_manager), 2)


class TestExecute(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input", create=True)
    def test_execute_success_case(self, mocked_input, mock_print):
        """
        I had a hard time making this test comprehensive - while this works, it doesn't really strike
        me as an impressive test. Sure it tells us that it runs and completes just fine, but not much
        else beyond that.

        I already wrote it though so I'll leave it in.

        I think the test functions as it does because the mocks aren't covering the input/print statements
        that are nested in the while loop of the execute command, but I'm not going to go down that rabbit
        hole as I don't think that's the primary goal of this exercise.
        """

        # Values for our mocked user inputs - this is meant to simulate someone typing on a keyboard.
        binary_string = "11011"
        exit_command = "TeRmInAte"

        # Commands are executed in order.
        mocked_input.side_effect = [binary_string, exit_command]

        execute()

        # Also assert that our terminate command works correctly.
        mock_print.assert_called_with("Done!")
