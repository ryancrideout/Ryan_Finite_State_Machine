from classes.state import State


class StateManager:
    """
    The StateManager class - this is in charge of initializing states and then processing
    input to get our desired state.

    This is specifically engineered to work with Modulo 3, but I don't know if it'd work with
    any other Modulos. If we wanted to scale this up to work with other Modulos, probably what
    I'd do is make StateManager an abstract class, and then make different child classes for
    different Modulos - like maybe have a StateManagerThree, StateManagerFour, etc. class.

    But then again, I don't know if that solves the problem of scalablity. (We couldn't just make
    infinite classes... like what if someone wanted a Finite State Machine for Modulo 24?)
    Maybe there exists an elegant solution for each of the methods that'd work for all states of
    all Modulos. Like maybe there's a "process_input" method out there that would just work for
    all Modulo states.

    I'm not sure, as I haven't researched it, but I am curious.
    """

    state_index = 0
    state_list = []
    current_state = None

    def __init__(self):
        """
        I think there's an argument to take the logic from "initialize_states" and just put
        it into the __init__ method. I really like keeping logic out of the __init__ method,
        but I would like to know if you guys would have had the "initialize_states" method or
        have just put that logic into __init__.
        """
        self.initialize_states()

    def initialize_states(self):
        """
        Okay so what I have for initializing the initial states for modulo 3, while it works, I
        don't think it's scalable at all. In the context of the advanced exercise, the Mathematician
        inside of me feels like there HAS to be a mathematical formula for correctly initializing states.

        Like, in my mind, what someone could do is when they initialize the StateManager, is they just
        specify what Modulo they're working with and then one block of code would be able to initialize
        any number of states based on the Modulo value.

        I think it could look like something I have commented below. That works specifically for Modulo 3,
        but it doesn't work for Modulo 4 or Modulo 10 (I tried just those two), so the logic would have to
        be adjusted.
        """
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
        """

        """
        This is the implementation I was talking about that isn't scalable. If someone wanted to make this
        work with Modulo 5, for example, then they have to manually go in here and add two more States.
        I don't like that, as I'm pretty sure it violates one of the S.O.L.I.D principles.

        TODO: Actually investigate if it violates S.O.L.I.D. principles haha.
        """
        self.state_list = [
            # State 0
            State(output=0, zero_input=0, one_input=1),
            # State 1
            State(output=1, zero_input=1, one_input=-1),
            # State 2
            State(output=2, zero_input=-1, one_input=0),
        ]

        # Our initial state will always be state 0. State index will also be 0.
        self.current_state = self.state_list[0]
        self.state_index = 0

    def process_input(self, binary_string: str):
        """
        Take the binary string and process it. This will also give us our current state.

        This implementation works for Modulo 3, but I think we'd have to tweak it to work
        with different modulos.
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

    def set_current_state(self, state: State):
        """
        Method to assign the state. While we could have just assigned current_state
        directly in the "process_input" method, I like having this as a separate
        method as it allows for more freedom, and is useful for debugging.
        """
        if not isinstance(state, State):
            raise TypeError("Error! Cannot set State to be a non-state.")
        if state not in self.state_list:
            raise ValueError("Error! Unrecognized State does not exist in state_list")

        self.current_state = state

    @property
    def current_state_output(self) -> int:
        return self.current_state.output

    def reset_current_state(self):
        """
        Reset the current state to be state 0. While this technically could be achieved with
        the set_current_state method, we might want to make some of the attributes of this
        class private, and this method would help facilitate that.

        That, and we need to reset the state_index.
        """
        self.state_index = 0
        self.current_state = self.state_list[0]
