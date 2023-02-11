# Set sail for adventure!

# TODO:
# - Add Readme on how to run this thing.
# - UNIT TESTS (and End-to-End!)
# - Incorporate EMAIL NOTES
# BE SURE TO ADD ALL OF MY THOUGHTS


class State:
    output = 0

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    zero_input = 0
    one_input = 0

    def __init__(self, output: int, zero_input: int, one_input: int) -> None:
        self.output = output
        self.zero_input = zero_input
        self.one_input = one_input


class State_0:
    output = 0

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    # Naming could have been better, but I stuck to concise names.
    zero_input = 0
    one_input = 1


class State_1:
    output = 1

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    # Naming could have been better, but I stuck to concise names.
    zero_input = 1
    one_input = -1


class State_2:
    output = 2

    # These are the attributes that determine which state we
    # should move to based on the binary input ("0" or "1") we receive.
    # This is within the context of the state manager as well - these attributes
    # are meant to modify the state_index to help the StateManager find the
    # right state.
    # Naming could have been better, but I stuck to concise names.
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
    current_state = None

    def __init__(self):
        # Need to initialize states, and then put them into the state list.
        self.initialize_states()

    def initialize_states(self):
        """
        Dear Ryan - please explain the snot out of this. Thanks.
        """
        modulo = 3
        for i in range(modulo):
            # NOTE: Order matters for these checks. If we did, say "if i % 2" before the last
            #       state check, we'd initialize the final state incorrectly.
            if i == 0:
                # Conditions to initialize the first state (which is state 0)
                self.state_list.append(State(output=i, zero_input=0, one_input=1))
            elif i == (modulo - 1):
                # Conditions for initializing the last state for the state list.
                if i % 2 == 0:
                    self.state_list.append(State(output=i, zero_input=-1, one_input=0))
                else:
                    self.state_list.append(State(output=i, zero_input=0, one_input=-1))
            elif i % 2 == 1:
                # Conditions for initializing odd numbered states
                self.state_list.append(State(output=i, zero_input=1, one_input=-1))
            elif i % 2 == 0:
                # Conditions for initializing even numbered states.
                self.state_list.append(State(output=i, zero_input=-1, one_input=1))

        # state_0 = State_0()
        # state_1 = State_1()
        # state_2 = State_2()

        # self.state_list = [state_0, state_1, state_2]

        # Our initial state will always be state 0.
        self.current_state = self.state_list[0]

    def process_input(self, binary_string: str):
        """
        Take the binary string and process it. This will also
        give us our current state.
        """
        for binary_integer in binary_string:
            input = int(binary_integer)
            # Note: 0's are "Falsy" and 1's are Truthy.
            if input:
                # 1 as an input
                self.state_index += self.state_list[self.state_index].one_input
            else:
                # 0 as an input
                self.state_index += self.state_list[self.state_index].zero_input

        self.set_current_state(self.state_list[self.state_index])

    def set_current_state(self, state):
        """
        TODO: Abstract the state further so we can do type checking.

        Method to assign the state. While we could have just assigned current_state
        directly in the "process_input" method, I like having this as a separate
        method as it allows for more freedom, and is useful for debugging.
        """
        self.current_state = state

    @property
    def current_state_output(self):
        return self.current_state.output


# Idea - make modulo_three a method for the state_manager (Hmm...)
# Or make it so we don't have to initialize the classes every time.
# Solution - initialize StateManager on start up, then trap the
# user in a while loop. How devious.
def modulo_three(string: str) -> float:
    """
    NOTE: Returns float for anticpation of decimal values.

    Takes a binary input string, and performs the modulo three operation on
    it and returns the answer, as a number.
    """
    state_manager = StateManager()
    state_manager.process_input(string)
    print(state_manager.current_state_output)


def execute():
    modulo_three("1111")
    print("Done!")


execute()
