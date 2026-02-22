from tools.permissions import check_permission

# system tools
from tools.system_tools.apps import open_app, close_app
from tools.system_tools.browser import open_url
from tools.system_tools.files import read_file, write_file, delete_file
from tools.system_tools.shell import run_command
from tools.system_tools.input import press_key, type_text, mouse_click
from tools.system_tools.power import shutdown, restart, sleep

TOOL_MAP = {
    # apps
    "open_app": open_app,
    "close_app": close_app,

    # browser
    "open_url": open_url,

    # files
    "read_file": read_file,
    "write_file": write_file,
    "delete_file": delete_file,

    # shell
    "run_command": run_command,

    # input
    "press_key": press_key,
    "type_text": type_text,
    "mouse_click": mouse_click,

    # power
    "shutdown": shutdown,
    "restart": restart,
    "sleep": sleep,
}

def execute_tool(tool_call: dict):
    """
    tool_call format:
    {
      "name": "open_app",
      "args": { "name": "spotify" }
    }
    """
    if not tool_call:
        return "No tool requested"

    tool_name = tool_call.get("name")
    args = tool_call.get("args", {})

    if tool_name not in TOOL_MAP:
        return f"Unknown tool: {tool_name}"

    if not check_permission(tool_name):
        return "❌ Permission denied"

    try:
        return TOOL_MAP[tool_name](**args)
    except Exception as e:
        return f"⚠️ Tool execution failed: {e}"