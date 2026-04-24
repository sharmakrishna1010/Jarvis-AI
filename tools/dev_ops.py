import subprocess
import os

def resolve_path(path_str):
    if not path_str or path_str.strip() in ["", "."]:
        return os.getcwd()
    
    clean_path = path_str.strip('\'" ').lower()
    
    # Catch the keyword no matter what fake path the AI invented
    if "downloads" in clean_path:
        actual_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    elif "desktop" in clean_path:
        actual_dir = os.path.join(os.path.expanduser("~"), "Desktop")
    elif "documents" in clean_path:
        actual_dir = os.path.join(os.path.expanduser("~"), "Documents")
    else:
        # If it's something else, try to resolve it normally
        actual_dir = os.path.expanduser(path_str)

    # If the folder still doesn't exist, fall back to the Jarvis root folder to prevent any errors
    if not os.path.exists(actual_dir):
        print(f"Warning: Directory '{actual_dir}' not found. Defaulting to current folder.")
        return os.getcwd()

    return actual_dir

def create_react_app(project_name, target_dir="."):
    actual_dir = resolve_path(target_dir)
    print(f"Bootstrapping React project '{project_name}' in new console...")

    try:
        command = f'start cmd /k "npx create-vite {project_name} --template react"'
        subprocess.Popen(command, shell=True, cwd=actual_dir)
        return True, f"React setup initiated in {actual_dir}."
    except Exception as e:
        return False, f"React setup failed: {e}"


def create_nextjs_app(project_name, target_dir="."):
    actual_dir = resolve_path(target_dir)
    print(f"Bootstrapping Next.js project '{project_name}' in new console...")

    try:
        command = f'start cmd /k "npx create-next-app {project_name}"'
        subprocess.Popen(command, shell=True, cwd=actual_dir)
        return True, "Next.js setup initiated."
    except Exception as e:
        return False, f"Next.js setup failed: {e}"


def create_django_app(project_name, target_dir="."):
    actual_dir = resolve_path(target_dir)
    print(f"Bootstrapping Django project '{project_name}' in new console...")

    try:
        command = f'start cmd /k "django-admin startproject {project_name}"'
        subprocess.Popen(command, shell=True, cwd=actual_dir)
        return True, "Django setup initiated."
    except Exception as e:
        return False, f"Django setup failed: {e}"


def create_react_native_app(project_name, target_dir="."):
    actual_dir = resolve_path(target_dir)
    print(f"Bootstrapping React Native project '{project_name}' in new console...")

    try:
        command = f'start cmd /k "npx react-native init {project_name}"'
        subprocess.Popen(command, shell=True, cwd=actual_dir)
        return True, "React Native setup initiated."
    except Exception as e:
        return False, f"React Native setup failed: {e}"


def create_flutter_app(project_name, target_dir="."):
    actual_dir = resolve_path(target_dir)
    print(f"Bootstrapping Flutter project '{project_name}' in new console...")

    try:
        command = f'start cmd /k "flutter create {project_name}"'
        subprocess.Popen(command, shell=True, cwd=actual_dir)
        return True, "Flutter setup initiated."
    except Exception as e:
        return False, f"Flutter setup failed: {e}"
