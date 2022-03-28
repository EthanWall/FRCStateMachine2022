import ctre
import wpilib.simulation
from pyfrc.physics import tankmodel, motor_cfgs
from pyfrc.physics.core import PhysicsInterface
from pyfrc.physics.units import units

from robot import Robot


class PhysicsEngine:

    def __init__(self, physics_controller: PhysicsInterface, robot: Robot):
        self.physics_controller = physics_controller

        # Motors
        self.l_motor = wpilib.simulation.PWMSim(0)
        self.r_motor = wpilib.simulation.PWMSim(2)

        # Encoders
        self.l_encoder = ctre.CANCoderSimCollection(robot.drivetrain.left_encoder)
        self.r_encoder = ctre.CANCoderSimCollection(robot.drivetrain.right_encoder)

        # Drivetrain
        self.drivetrain = tankmodel.TankModel.theory(
            motor_config=motor_cfgs.MOTOR_CFG_CIM,
            robot_mass=110 * units.lbs,
            gearing=10.71,
            nmotors=2,
            x_wheelbase=22 * units.inch,
            wheel_diameter=6 * units.inch
        )

    def update_sim(self, now: float, tm_diff: float):
        l_motor = self.l_motor.getSpeed()
        r_motor = self.r_motor.getSpeed()

        transform = self.drivetrain.calculate(l_motor, r_motor, tm_diff)
        pose = self.physics_controller.move_robot(transform)

        self.l_encoder.setVelocity(int(l_motor))
        self.r_encoder.setVelocity(int(r_motor))
