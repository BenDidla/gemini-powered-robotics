# robot_controller/movement.py

from hardware_interface.motor_driver import MotorDriver

class Movement:
    """
    High-level movement controller that wraps the MotorDriver.
    """

    def __init__(self):
        self.motor = MotorDriver()

    def move_forward(self, distance: float):
        print(f"[Movement] Moving forward for {distance} units.")
        self.motor.move_forward(speed=50)
        # Time delay proportional to distance could be added here
        self.motor.stop()

    def move_backward(self, distance: float):
        print(f"[Movement] Moving backward for {distance} units.")
        self.motor.move_backward(speed=50)
        # Add sleep based on distance if needed
        self.motor.stop()

    def turn_left(self, angle: float):
        print(f"[Movement] Turning left {angle} degrees.")
        self.motor.turn_left(angle)

    def turn_right(self, angle: float):
        print(f"[Movement] Turning right {angle} degrees.")
        self.motor.turn_right(angle)

    def stop(self):
        print("[Movement] Stopping robot.")
        self.motor.stop()

