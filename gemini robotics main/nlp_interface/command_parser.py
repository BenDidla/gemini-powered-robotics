
# nlp_interface/command_parser.py

class CommandParser:
    """
    Parses Gemini output into structured robot commands.
    """

    def parse(self, text: str) -> dict:
        """
        Parse a natural language text into structured command.

        Example:
            Input: "Move forward 2 meters"
            Output: {"action": "move_forward", "distance": 2}
        """
        text = text.lower()

        if "forward" in text:
            return {"action": "move_forward", "distance": self._extract_number(text)}
        elif "backward" in text:
            return {"action": "move_backward", "distance": self._extract_number(text)}
        elif "left" in text:
            return {"action": "turn_left", "angle": self._extract_number(text)}
        elif "right" in text:
            return {"action": "turn_right", "angle": self._extract_number(text)}
        elif "stop" in text:
            return {"action": "stop"}
        else:
            return {"action": "unknown"}

    def _extract_number(self, text: str) -> float:
        """
        Extract the first number found in the text.
        """
        import re
        matches = re.findall(r'\d+', text)
        if matches:
            return float(matches[0])
        return 0.0
