from classes.statemanager import StateManager

# Set sail for adventure!

# TODO:
# - Add Readme on how to run this thing.
# - UNIT TESTS (and End-to-End!)
# - Incorporate EMAIL NOTES:
#   - Accept Binary, Decimal, Hexadecimal, and numbers with decimal values
#   - Should deal with Negative Values
#   - Plus stupid strings.
# BE SURE TO ADD ALL OF MY THOUGHTS


def modulo_three(string: str, state_manager: StateManager) -> int:
    """
    Takes a binary input string, and performs the modulo three operation on
    it and returns the answer, as a number.
    """
    if not isinstance(state_manager, StateManager):
        raise TypeError(
            "Error! Invalid StateManager! Cannot run modulo_three with {}".format(
                type(state_manager)
            )
        )

    state_manager.process_input(string)
    output = state_manager.current_state_output

    # Reset our state incase we go another round.
    state_manager.reset_current_state()

    return output


def execute():
    # Strings that will terminate the while loop.
    TERMINATE = ["stop", "s", "exit", "terminate", "t", "quit", "q"]
    # We only want to initialize the state_manager once.
    state_manager = StateManager()

    user_input = input(
        "Input a binary string, and I will perform the modulo 3 operator on it. Type 'q' to quit - "
    )
    while user_input.lower() not in TERMINATE:
        print(modulo_three(user_input, state_manager))
        # Empty print statement to make this more readable in the console
        print()
        user_input = input(
            "Input a binary string, and I will perform the modulo 3 operator on it. Type 'q' to quit - "
        )

    print("Done!")


"""
So turns out that this execute command at the bottom of the script really, really hampers with the ability to write unit tests.
I discovered that when you import a script/module, it runs all of the code, so any executables will be executed. At least,
that's what I think what happened. If that is what actually happened, I didn't discover this for so long because that's just
not how I've ever written code at work.

This stumped me for much, much longer than I'm comfortable admitting, but on the bright side I really did learn something new
about unit testing and imports because of this.
"""
# execute()
