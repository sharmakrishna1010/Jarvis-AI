from core.audio_engine import say

def write_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True, f"Success: Wrote data to {filename}"
    except Exception as e:
        return False, f"File creation failed: {e}"
