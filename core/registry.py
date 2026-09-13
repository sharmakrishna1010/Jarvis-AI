from tools.file_ops import *
from tools.dev_ops import *
from tools.system_ops import *
from tools.web_ops import *
from tools.preference import *
from tools.media_control import *

# import tools as you build them...

# The magic dictionary
TOOL_REGISTRY = {
    # System tools
    "CMD": run_cmd,
    "SYSTEM_STATUS": report_system_status,
    
    # File tools
    "WRITE_FILE": write_file,
    
    # Dev tools
    "REACT_APP": create_react_app,
    "NEXT_APP": create_nextjs_app,
    "FLUTTER_APP": create_flutter_app,
    "REACT_NATIVE_APP": create_react_native_app,
    "DJANGO_APP": create_django_app,
    
    # Web tools
    "GET_WEATHER": fetch_live_weather,

    # Preference tools
    "SAVE_PREFERENCE": save_preference,
    "DELETE_PREFERENCE": delete_preference,

    # Media control tools
    "PAUSE_RESUME": pause_resume,
    "VOLUME_DOWN": volume_down,
    "VOLUME_UP": volume_up,
    "PLAY_NEXT": play_next,
    "PLAY_PREVIOUS": play_previous
}
