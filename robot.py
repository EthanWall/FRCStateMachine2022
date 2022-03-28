import wpilib

from control_boards import GamepadControlBoard, ControlBoardBase
from fsm import DriveStateMachine
from scheduling import Scheduler
from subsystems import Drivetrain


class Robot(wpilib.TimedRobot):
    # Control Board
    controls: ControlBoardBase

    # Subsystems
    drivetrain: Drivetrain

    # State Machines
    drivetrain_sm: DriveStateMachine

    # Manages the subsystems and state machine main loop
    scheduler: Scheduler

    def robotInit(self) -> None:
        # Control scheme for teleop
        self.controls = GamepadControlBoard()

        # Initialize subsystems
        self.drivetrain = Drivetrain()

        # Initialize state machines
        self.drivetrain_sm = DriveStateMachine(self.controls)

        # Run the subsystem and state machine loops during periodic
        self.scheduler = Scheduler(
            [self.drivetrain],
            [self.drivetrain_sm]
        )

    def autonomousInit(self) -> None:
        pass

    def teleopInit(self) -> None:
        pass

    def testInit(self) -> None:
        pass

    def disabledInit(self) -> None:
        pass

    def autonomousPeriodic(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        pass

    def testPeriodic(self) -> None:
        pass

    def robotPeriodic(self) -> None:
        self.scheduler.update()


if __name__ == "__main__":
    wpilib.run(Robot)
