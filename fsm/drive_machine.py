from enum import Enum

import wpilib

from control_boards import ControlBoardBase
from exceptions import InvalidStateError
from fsm import StateMachineBase
from subsystems import Drivetrain


class DriveState(Enum):
    IDLE = 0,
    OPEN_LOOP = 1  # Voltage control


class DriveStateMachine(StateMachineBase):
    state = DriveState.IDLE

    def __init__(self, controls: ControlBoardBase):
        self.controls = controls

        # Subsystems are singletons. In this instance, constructing a Drivetrain
        # gets the one instance of Drivetrain, it does NOT make a new one.
        self.drivetrain = Drivetrain()

    def update(self):
        match self.state:
            case DriveState.IDLE:

                if wpilib.RobotState.isTeleop():
                    self.state = DriveState.OPEN_LOOP

            case DriveState.OPEN_LOOP:

                if not wpilib.RobotState.isTeleop():
                    self.state = DriveState.IDLE
                    self.drivetrain.stop()
                    return

                forward = self.controls.get_forward()
                rotation = self.controls.get_turn()

                self.drivetrain.arcade_drive(forward, rotation)

            case _:

                raise InvalidStateError(self.state.name)
