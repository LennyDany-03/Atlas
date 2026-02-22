class GoalManager:
    def __init__(self):
        self.current_goal = None

    def set_goal(self, intent_data, raw_text):
        if intent_data["intent"] == "exit":
            self.current_goal = "exit_program"
        elif intent_data["intent"] == "open_app":
            self.current_goal = f"Open application ({raw_text})"
        elif intent_data["intent"] == "play_media":
            self.current_goal = f"Play media ({raw_text})"
        else:
            self.current_goal = "clarify_request"

        return self.current_goal