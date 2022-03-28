class StateMachineBase:
    """
    All state machines should inherit from this class.
    A state machine is responsible for making calls to subsystems and ensuring that a subsystem
    is controlled in an understandable and predictable way.
    """

    def update(self):
        """
        Make calls to subsystems, process logic and user input, and switch between states
        """
        raise NotImplemented
