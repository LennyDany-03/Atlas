import subprocess
import platform

def shutdown():
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/s", "/t", "5"])
        return "System will shut down in 5 seconds"
    return "Unsupported OS"


def restart():
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/r", "/t", "5"])
        return "System will restart in 5 seconds"
    return "Unsupported OS"


def sleep():
    if platform.system() == "Windows":
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])
        return "System going to sleep"
    return "Unsupported OS"