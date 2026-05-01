import subprocess
import psutil

def is_safe_command(command):
    dangerous_keywords = {
        "del",
        "erase",
        "rmdir",
        "rm",
        "format",
        "diskpart",
        "reg",
        "shutdown",
        "restart",
        "remove-item",
        "clear-content",
        "drop",
        "truncate",
        "attrib",
        "icacls",
        "takeown",
    }
    words = command.lower().split()
    for word in words:
        if word in dangerous_keywords:
            return False
    return True

def run_cmd(command_string):
    command_to_run = command_string.replace("'", "")

    if not is_safe_command(command_to_run):
        return False, f"SECURITY ALERT: Blocked dangerous command -> {command_to_run}"

    interactive_keywords = ["npx", "npm", "pip", "flutter", "django-admin", "python"]
    needs_new_window = any(
        keyword in command_to_run.lower() for keyword in interactive_keywords
    )

    try:
        if needs_new_window:
            print("Interactive dev command detected in CMD tool. Forcing into a new console...")
            safe_command = f'start "" cmd /k "{command_to_run}"'
            subprocess.Popen(safe_command, shell=True)
        else:
            subprocess.Popen(command_to_run, shell=True)

        return True, f"Executing System Command: {command_to_run}"
    except Exception as e:
        return False, f"Failed to run command: {e}"

def report_system_status():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        
        memory = psutil.virtual_memory()
        ram_usage = memory.percent
        ram_free_gb = round(memory.available / (1024 ** 3), 1)

        report = f"CPU utilization is at {cpu_usage} percent. Memory is at {ram_usage} percent capacity, with {ram_free_gb} gigabytes available."
        
        return True, report
        
    except Exception as e:
        return False, f"Failed to retrieve system status: {e}"