import unittest
from classes.binarystringsanitizer import BinaryStringSanitizer


class TestBinaryStringSanitizer(unittest.TestCase):
    """
    Tests for the Binary String Sanitizer - I realize that this functionality has already sort of been tested
    in some of the other tests, but I figure it's good to do my due diligence and write tests here as well.
    """

    def test_sanitize_input_success_case(self):
        """
        If we give sanitize_input a clean binary string, it should just spit it right back out.
        """
        self.assertEqual(BinaryStringSanitizer.sanitize_input("1111"), "1111")

    def test_sanitize_input_integer_case(self):
        """
        Integers should be converted to binary.
        """
        self.assertEqual(BinaryStringSanitizer.sanitize_input(2), "10")

    def test_sanitize_input_float_case(self):
        """
        If you think that floats should also be converted to binary, you'd be right.
        """
        self.assertEqual(BinaryStringSanitizer.sanitize_input(3.1415), "11")

    def test_sanitize_input_negative_integer_case(self):
        """
        Negative integers should throw an error.
        """
        with self.assertRaises(TypeError) as context:
            BinaryStringSanitizer.sanitize_input(-14)

            self.assertTrue("Please enter Non-Negative Number." in context.exception)

    def test_sanitize_input_negative_float_case(self):
        """
        Negative floats should also throw an error.
        """
        with self.assertRaises(TypeError) as context:
            BinaryStringSanitizer.sanitize_input(-52.8393)

            self.assertTrue("Please enter Non-Negative Number." in context.exception)

    def test_sanitize_input_unrecognized_input_case(self):
        """
        Admittedly, this test is more or less testing the compiler (which, admittedly, I don't
        think makes for a great test) but I've included it anyways.
        """
        with self.assertRaises(TypeError) as context:
            BinaryStringSanitizer.sanitize_input(BinaryStringSanitizer)

            self.assertTrue(
                "Error! Unrecognized format for input." in context.exception
            )

    def test_sanitize_input_hexadecimal_case(self):
        """
        Sanitize Inputs should be able to take hexadecimal values of any casing and return
        a binary input.
        """
        self.assertEqual(
            BinaryStringSanitizer.sanitize_input("aBcDeF"), "101010111100110111101111"
        )

    def test_sanitize_input_garbage_string_case(self):
        """
        If we have any inputs that don't conform to hexadecimal characters, then we throw
        an error.

        In theory, if you had a nonsensical string consisting of only a's, b's, c's, d's, e's
        and f's, you WOULD get back an output. Not sure if that would be a bug or a feature.
        """
        with self.assertRaises(TypeError) as context:
            BinaryStringSanitizer.sanitize_input(
                "It's not Willem Dafoe, it's Willem Dafriend!"
            )

            self.assertTrue(
                "Please enter Non-Negative Binary or Hexadecimal input."
                in context.exception
            )
