class ControlBoardBase:
    """
    Defines the necessary controls for the robot. Should be implemented by a child class.
    """

    def get_forward(self) -> float:
        raise NotImplemented

    def get_turn(self) -> float:
        raise NotImplemented
