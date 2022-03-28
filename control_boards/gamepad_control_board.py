import wpilib

from control_boards import ControlBoardBase


class GamepadControlBoard(ControlBoardBase):

    def __init__(self):
        self.drive_stick = wpilib.XboxController(0)

    def get_forward(self) -> float:
        x = self.drive_stick.getLeftY()
        return -x * abs(x)

    def get_turn(self) -> float:
        x = self.drive_stick.getRightX()
        return x * abs(x)
