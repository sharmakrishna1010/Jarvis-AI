import subprocess
from audio_engine import say


def create_react_app(project_name):
    print(f"Bootstrapping React Vite project: {project_name}")

    try:
        subprocess.Popen(
            f"npx create-vite {project_name} --template react",
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        return True, "React setup initiated."
    except Exception as e:
        return False, f"React setup failed: {e}"


def create_nextjs_app(project_name):
    print(f"Bootstrapping Next.js project: {project_name}")

    try:
        subprocess.Popen(
            f"npx create-next-app {project_name}",
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        return True, "Next.js setup initiated."
    except Exception as e:
        return False, f"Next.js setup failed: {e}"


def create_react_native_app(project_name):
    print(f"Bootstrapping React Native project: {project_name}")

    try:
        subprocess.Popen(
            f"npx expo init {project_name}",
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        return True, "React Native setup initiated."
    except Exception as e:
        return False, f"React Native setup failed: {e}"
    
    
def create_flutter_app(project_name):
    print(f"Bootstrapping Flutter project: {project_name}")

    try:
        subprocess.Popen(
            f"flutter create {project_name}",
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        return True, "Flutter setup initiated."
    except Exception as e:
        return False, f"Flutter setup failed: {e}"


def create_django_app(project_name):
    print(f"Bootstrapping Django project: {project_name}")

    try:
        subprocess.Popen(
            f"django-admin startproject {project_name}",
            shell=True,
            creationflags=subprocess.CREATE_NEW_CONSOLE,
        )
        return True, "Django setup initiated."
    except Exception as e:
        return False, f"Django setup failed: {e}"

