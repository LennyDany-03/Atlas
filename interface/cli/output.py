def render_output(response: dict):
    print(f"\n🤖 {response.get('message', '')}\n")