import subprocess

def is_safe_command(command):
    dangerous_keywords = {"del", "erase", "rmdir", "rm", "format", "diskpart", "reg", "shutdown", "restart", "remove-item", "clear-content", "drop", "truncate", "attrib", "icacls", "takeown"}
    words = command.lower().split()
    for word in words:
        if word in dangerous_keywords:
            return False
    return True

def run_cmd(command_string):
    command_to_run = command_string.replace("'", "")
    
    if not is_safe_command(command_to_run):
        return False, f"SECURITY ALERT: Blocked dangerous command -> {command_to_run}"
    
    try:
        subprocess.Popen(command_to_run, shell=True)
        return True, f"Executing System Command: {command_to_run}"
    except Exception as e:
        return False, f"Failed to run command: {e}"