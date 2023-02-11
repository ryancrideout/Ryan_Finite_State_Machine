class State:
    """
    This is the State Class. While what I have works for Modulo 3 states, I'm suspicious that this class
    WOULDN'T work for all Modulo X states. I think to get around this one could use inherentance (parent/child)
    classes, but admittedly I didn't think about it that hard as I'm just attempting to solve the Modulo 3
    exercise.

    Like maybe for Modulo X States we could do some stuff with "setattr" to get all of the input values we
    want. Like I feel like there has to be a mathematical formula for setting states depending on what Modulo
    you're working with, but again I haven't looked it up. Maybe I shouldn't be thinking about it so much,
    but I just can't help myself because this is such an interesting problem.

    It might have been appropriate to make "State" a Python Data Class (@dataclass), given that
    it's just three attributes (for now). I'm comfortable with just leaving this as a class though,
    as Data Classes I addmitedly don't have THAT much experience with.

    Side note: "Modulo X" sounds awesome.
    """

    output = 0

    # These are the attributes that determine which state we should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes are meant to modify the state_index to help
    # the StateManager find the right state. That said, I feel like there are better names out there because without context
    # I'm not sure these make sense.
    zero_input = 0
    one_input = 0

    def __init__(self, output: int, zero_input: int, one_input: int) -> None:
        # Ensure that we're making our States with ints here.
        for parameter in [output, zero_input, one_input]:
            if not isinstance(parameter, int):
                raise TypeError(
                    "Error! Cannot initialize State with non-integer input."
                )

        self.output = output
        self.zero_input = zero_input
        self.one_input = one_input
