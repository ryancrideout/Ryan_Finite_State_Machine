# Explanation for the accepted characters - I figure that it's within the realm of possibility
# that someone could enter a Hexadecimal string, so I wanted to make BinaryStringSanitizer be
# able to handle hexadecimal values.
ACCEPTED_CHARACTERS = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
]


class BinaryStringSanitizer:
    """
    Helper class to help sanitize inputs for the StateManager class. However, with how this is built,
    I could see this class having life doing other various tasks, which is why I broke it out into
    a class.

    I debated about just making this a function, but I figured a class with static methods would be
    alright.
    """

    @staticmethod
    def sanitize_input(input) -> str:
        """
        This sanitizes any input (or at least attempts to) and then returns a binary string.
        Order of operations:
        1. Check if we have an integer or float. I know that it's possible to have decimal value
           in binary, so while we could properly handle them I'll just round the values for now
           and call it a day. Rounding also simplifies the code, but "handling decimals" would be
           a feature I'd consider adding later.
        2. General check of the strings. We'll allow for Hexadecimal values, but any other weird
           characters or negative values we flag.
        """

        # This was stolen from StackOverflow:
        # https://stackoverflow.com/questions/699866/python-int-to-binary-string
        if isinstance(input, int) or isinstance(input, float):
            if isinstance(input, float):
                input = int(input)
            return "{0:b}".format(input)

        if not isinstance(input, str):
            raise TypeError("Error! Unrecognized format for input.")

        # So because we have to iterate through each character in the string, I think this makes the
        # whole process more expensive, but maybe by a trivial amount? I'm not sure. I don't know
        # if I'm just being paranoid or if this is actually an optimization concern.
        is_binary = True
        for character in input:
            # NOTE: I think sometimes Hexadecimal strings could take the format of "0xFF", and
            #       if that's the case I don't think this will work.
            if character.upper() not in ACCEPTED_CHARACTERS:
                raise TypeError(
                    "Please enter Non-Negative Binary or Hexadecimal input."
                )
            elif character not in ["0", "1"]:
                # We're working with Hexadecimal values.
                is_binary = False

        if is_binary:
            return input
        else:
            # Convert Hexadecimal value to Binary.
            return "{0:b}".format(int(input, 16))
