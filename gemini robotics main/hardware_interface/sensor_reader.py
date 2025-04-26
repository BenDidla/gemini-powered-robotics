# hardware_interface/sensor_reader.py

import random

class SensorReader:
    """
    Simulates reading sensors.
    Replace these with actual sensor readings from ultrasonic or IMU.
    """

    def __init__(self):
        print("[SensorReader] Sensors initialized.")

    def read_distance(self) -> float:
        """
        Simulate reading distance from an ultrasonic sensor.
        """
        distance = random.uniform(10.0, 100.0)  # returns distance between 10cm and 100cm
        print(f"[SensorReader] Distance measured: {distance:.2f} cm")
        return distance

    def read_orientation(self) -> dict:
        """
        Simulate reading orientation from an IMU sensor.
        """
        orientation = {
            "pitch": random.uniform(-90.0, 90.0),
            "roll": random.uniform(-90.0, 90.0),
            "yaw": random.uniform(0.0, 360.0)
        }
        print(f"[SensorReader] Orientation: {orientation}")
        return orientation
