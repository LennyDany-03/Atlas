def create_plan(goal: str):
    if goal == "exit_program":
        return ["terminate"]

    if goal.startswith("Open application"):
        return ["identify_app", "launch_app"]

    if goal.startswith("Play media"):
        return ["identify_media", "launch_player", "play"]

    return ["ask_user_for_clarification"]