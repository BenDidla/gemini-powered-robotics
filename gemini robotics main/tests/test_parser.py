
# tests/test_parser.py

import unittest
from nlp_interface.command_parser import CommandParser

class TestCommandParser(unittest.TestCase):

    def setUp(self):
        self.parser = CommandParser()

    def test_parse_move_forward(self):
        command = self.parser.parse("Move forward 5 meters")
        self.assertEqual(command['action'], "move_forward")
        self.assertEqual(command['distance'], 5)

    def test_parse_turn_left(self):
        command = self.parser.parse("Turn left 90 degrees")
        self.assertEqual(command['action'], "turn_left")
        self.assertEqual(command['angle'], 90)

    def test_parse_unknown(self):
        command = self.parser.parse("Dance around")
        self.assertEqual(command['action'], "unknown")

if __name__ == '__main__':
    unittest.main()
