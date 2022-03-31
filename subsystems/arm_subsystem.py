import ctre
import wpilib
import wpilib.drive

from subsystems import SubsystemBase
from util import SingletonMeta


class Arm(SubsystemBase, metaclass=SingletonMeta):
    """
    The robot's drivetrain
    """

    class DSKeys:
        """
        Value names for the Smart Dashboard
        """

        ARM_POWER = "Arm Power"

    class _PeriodicIO:
        # Outputs
        demand: float = 0

        # Inputs
        pass

    def __init__(self):
        # Periodic Input/Output
        self._io = self._PeriodicIO()

        # Motors
        self._motors = wpilib.MotorControllerGroup(wpilib.Spark(4), wpilib.Spark(5))

    def read_periodic_inputs(self):
        pass

    def write_periodic_outputs(self):
        # Move the arm
        demand = self._io.demand

        self._motors.set(demand)

    def update_on_dashboard(self):
        demand = self._io.demand

        wpilib.SmartDashboard.putNumber(self.DSKeys.ARM_POWER, demand)

    # Getters

    pass

    # Setters

    def drive(self, power: float):
        """
        Move the arm.
        :param power: Power to feed to the arm
        """

        # Set the arm power
        self._io.demand = power

    def drive_volts(self, volts: float):
        """
        Move the arm with voltage compensation.
        :param volts: The power to feed to the arm in volts
        """

        # Compensate for voltage drops
        power = volts / wpilib.RobotController.getBatteryVoltage()

        # Set the arm power
        self._io.demand = power

    def stop(self):
        self._io.demand = 0
