import wpilib

from control_boards import ControlBoardBase


class GamepadControlBoard(ControlBoardBase):

    def __init__(self):
        self.drive_stick = wpilib.XboxController(0)
        self.arm_stick = wpilib.XboxController(1)

    def get_forward(self) -> float:
        x = self.drive_stick.getLeftY()
        return -x * abs(x)

    def get_turn(self) -> float:
        x = self.drive_stick.getRightX()
        return x * abs(x)

    def get_arm(self) -> float:
        x = self.arm_stick.getLeftY()
        return x
