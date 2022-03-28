import typing

import wpilib

from fsm import StateMachineBase
from subsystems import SubsystemBase


class Scheduler:
    _all_subsystems: typing.Tuple[SubsystemBase]
    _all_state_machines: typing.Tuple[StateMachineBase]

    def __init__(self, subsystems_: typing.Iterable[SubsystemBase], state_machines: typing.Iterable[StateMachineBase]):
        self._all_subsystems = tuple(subsystems_)
        self._all_state_machines = tuple(state_machines)

    def update(self):
        if not wpilib.RobotState.isEnabled():
            return

        [x.read_periodic_inputs() for x in self._all_subsystems]
        [x.update() for x in self._all_state_machines]
        [x.write_periodic_outputs() for x in self._all_subsystems]
        [x.update_on_dashboard() for x in self._all_subsystems]
