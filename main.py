# Set sail for adventure!

# TODO:
# - Add Readme on how to run this thing.
# - UNIT TESTS (and End-to-End!)
# - Incorporate EMAIL NOTES
# BE SURE TO ADD ALL OF MY THOUGHTS


class State_0:
    output = 0

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    # Naming could have been better, but I stuck to consice names.
    zero_input = 0
    one_input = 1


class State_1:
    output = 1

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    # Naming could have been better, but I stuck to consice names.
    zero_input = 1
    one_input = -1


class State_2:
    output = 2

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    # Naming could have been better, but I stuck to consice names.
    zero_input = -1
    one_input = 0


class StateManager:
    """
    Should processing the input happen in this class, or somewhere else?

    Hmm... I think for now I'll put it here? There could be an argument to break
    it out though.
    """

    state_index = 0
    state_list = []

    def __init__(self):
        # Need to initialize states, and then put them into the state list.
        self.initialize_states()
        print("Shoryuken!")

    def initialize_states(self):
        state_0 = State_0()
        state_1 = State_1()
        state_2 = State_2()

        self.state_list = [state_0, state_1, state_2]

    def process_input(string: str):
        print("Shoryuken!")


def modulo_three(string: str) -> float:
    """
    NOTE: Returns float for anticpation of decimal values.

    Takes a binary input string, and performs the modulo three operation on
    it and returns the answer, as a number.
    """
    state_manager = StateManager()
    print("Shoryuken!")


def execute():
    modulo_three()
    print("Shroyuken!")


execute()
