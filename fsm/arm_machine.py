from enum import Enum

import wpilib

from control_boards import ControlBoardBase
from fsm import StateMachineBase
from subsystems.arm_subsystem import Arm


class ArmState(Enum):
    RUNNING = 0,
    FALLING = 1


class ArmStateMachine(StateMachineBase):
    state = ArmState.RUNNING

    def __init__(self, controls: ControlBoardBase):
        self.controls = controls

        self.arm = Arm()

    def update(self):
        match self.state:
            case ArmState.RUNNING:

                if self.controls.get_arm() == 0:
                    self.state = ArmState.FALLING
