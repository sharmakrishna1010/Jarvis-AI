from audio_engine import say

def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        say(f"Wrote data to {filename}")
        return True, f"Success: Wrote data to {filename}"
    except Exception as e:
        say(f"File creation failed: {e}")
        return False, f"File creation failed: {e}"