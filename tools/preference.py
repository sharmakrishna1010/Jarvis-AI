import datetime
from memory.memory_chroma import save_preference as sp
from memory.memory_chroma import delete_preference as dp

def save_preference(key, value, updated_at=None):
    try:
        sp(key, value, updated_at)
        return True, f"Preference for '{key}' has been updated to '{value}'."
    except Exception as e:
        return False, f"Failed to save preference: {e}"

def delete_preference(key):
    try:
        deleted = dp(key)
        if deleted:
            return True, f"Preference for '{key}' has been removed."
        return True, f"No existing preference found for '{key}'."
    except Exception as e:
        return False, f"Failed to delete preference: {e}"
