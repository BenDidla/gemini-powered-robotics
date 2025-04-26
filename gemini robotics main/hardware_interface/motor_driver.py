# hardware_interface/motor_driver.py

import time

class MotorDriver:
    """
    Simulates motor control. 
    Replace these print statements with real GPIO control if using hardware.
    """

    def __init__(self):
        # Initialize motor control pins here if using real hardware
        print("[MotorDriver] Initialized motor driver.")

    def move_forward(self, speed=50):
        print(f"[MotorDriver] Moving forward at {speed}% speed.")
        # GPIO control logic here

    def move_backward(self, speed=50):
        print(f"[MotorDriver] Moving backward at {speed}% speed.")
        # GPIO control logic here

    def turn_left(self, angle=90):
        print(f"[MotorDriver] Turning left {angle} degrees.")
        time.sleep(angle / 90)  # Rough estimate, adjust with calibration

    def turn_right(self, angle=90):
        print(f"[MotorDriver] Turning right {angle} degrees.")
        time.sleep(angle / 90)  # Rough estimate, adjust with calibration

    def stop(self):
        print("[MotorDriver] Stopping motors.")
        # GPIO stop logic here
