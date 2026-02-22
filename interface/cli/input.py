def get_cli_input():
    try:
        user_input = input("🧠 > ")
        return user_input.strip()
    except KeyboardInterrupt:
        return "exit"