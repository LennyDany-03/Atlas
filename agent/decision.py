def decide_next_action(plan: list):
    if not plan:
        return {"action": "idle"}

    next_step = plan[0]

    return {
        "action": next_step,
        "status": "pending"
    }