# robot_controller/task_executor.py

from robot_controller.movement import Movement

class TaskExecutor:
    """
    Executes parsed tasks using the Movement module.
    """

    def __init__(self):
        self.movement = Movement()

    def execute(self, command: dict):
        """
        Execute a given command dictionary.
        
        Example command:
        {
            "action": "move_forward",
            "distance": 2
        }
        """
        action = command.get("action")

        if action == "move_forward":
            distance = command.get("distance", 1)
            self.movement.move_forward(distance)
        elif action == "move_backward":
            distance = command.get("distance", 1)
            self.movement.move_backward(distance)
        elif action == "turn_left":
            angle = command.get("angle", 90)
            self.movement.turn_left(angle)
        elif action == "turn_right":
            angle = command.get("angle", 90)
            self.movement.turn_right(angle)
        elif action == "stop":
            self.movement.stop()
        else:
            print(f"[TaskExecutor] Unknown action: {action}")

