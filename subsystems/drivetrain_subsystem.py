import ctre
import wpilib
import wpilib.drive

from subsystems import SubsystemBase
from util import SingletonMeta


class Drivetrain(SubsystemBase, metaclass=SingletonMeta):
    """
    The robot's drivetrain
    """

    class DSKeys:
        """
        Value names for the Smart Dashboard
        """

        AVERAGE_DISTANCE = "Drivetrain Distance"

    class _PeriodicIO:
        # Outputs
        left_demand: float = 0
        right_demand: float = 0

        # Inputs
        left_position: float = 0
        right_position: float = 0

    def __init__(self):
        # Periodic Input/Output
        self._io = self._PeriodicIO()

        # Motors
        left_motors = wpilib.MotorControllerGroup(wpilib.Spark(0), wpilib.Spark(1))
        left_motors.setInverted(False)

        right_motors = wpilib.MotorControllerGroup(wpilib.Spark(2), wpilib.Spark(3))
        right_motors.setInverted(True)

        # Drivetrain
        self._drive = wpilib.drive.DifferentialDrive(left_motors, right_motors)

        # Encoders
        self.left_encoder = ctre.CANCoder(1)
        self.right_encoder = ctre.CANCoder(2)

    def read_periodic_inputs(self):
        self._io.left_position = self.left_encoder.getPosition()
        self._io.right_position = self.right_encoder.getPosition()

    def write_periodic_outputs(self):
        # Drive the robot
        left_demand = self._io.left_demand
        right_demand = self._io.right_demand

        self._drive.tankDrive(left_demand, right_demand, False)

    def update_on_dashboard(self):
        wpilib.SmartDashboard.putNumber(self.DSKeys.AVERAGE_DISTANCE, self.average_distance)

    # Getters

    @property
    def left_distance(self) -> float:
        return self._io.left_position

    @property
    def right_distance(self) -> float:
        return self._io.right_position

    @property
    def average_distance(self) -> float:
        return (self.left_distance + self.right_distance) / 2

    # Setters

    def arcade_drive(self, forward: float, rotation: float):
        """
        Drive the robot with forward and rotation controls
        :param forward: Movement in the heading direction
        :param rotation: Movement around the robot's center
        """

        # Calculate the wheel speeds for arcade drive
        speeds = self._drive.arcadeDriveIK(forward, rotation, False)

        # Set the left and right motor powers
        self._io.left_demand = speeds.left
        self._io.right_demand = speeds.right

    def stop(self):
        self._io.left_demand = 0
        self._io.right_demand = 0

    def reset_encoders(self):
        self.left_encoder.setPosition(0)
        self.right_encoder.setPosition(0)

        # Reset the Periodic I/O. It now contains invalid values
        self._io = self._PeriodicIO()
