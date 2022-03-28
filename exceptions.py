class InvalidStateError(Exception):
    def __init__(self, state: str):
        """
        Exception raised when a State Machine attempts to transition into a State that does not exist.

        :param state: The non-existent state
        """
        super().__init__(f"The state \"{state}\" does not exist!")
