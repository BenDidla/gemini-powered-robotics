
# tests/test_movement.py

import unittest
from robot_controller.movement import Movement

class TestMovement(unittest.TestCase):

    def setUp(self):
        self.movement = Movement()

    def test_move_forward(self):
        self.movement.move_forward(2)
        # Here we'd mock MotorDriver in real hardware tests

    def test_turn_left(self):
        self.movement.turn_left(90)

    def test_stop(self):
        self.movement.stop()

if __name__ == '__main__':
    unittest.main()
