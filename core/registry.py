from tools.file_ops import *
from tools.dev_ops import *
from tools.system_ops import *

# import tools as you build them...

# The magic dictionary
TOOL_REGISTRY = {
    # System tools
    "CMD": run_cmd,
    
    # File tools
    "WRITE_FILE": write_file,
    
    # Dev tools
    "REACT_APP": create_react_app,
    "NEXT_APP": create_nextjs_app,
    "FLUTTER_APP": create_flutter_app,
    "REACT_NATIVE_APP": create_react_native_app,
    "DJANGO_APP": create_django_app,
}
