import os
from audio_engine import listen, say
from action import performAction, greetings

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 40)
    print(" JARVIS INITIALIZED")
    print("=" * 40)
    print("Select Input Mode:")
    print("[1] Voice Mode (Standard)")
    print("[2] Night Mode (Type commands, audio responses)")
    print("[3] Silent Mode (Type commands, text responses only - no audio)")

    mode = input("\nEnter mode (1/2/3): ").strip()
    
    is_silent = (mode == "3") 
    
    greetings(muted=is_silent)

    while True:
        try:
            task = ""
            if mode == "1":
                task = listen()
            elif mode in ["2", "3"]:
                print("\nListening...")
                task = input("You: ").strip()
                
            if "exit" in task.lower() or "shutdown" in task.lower():
                if is_silent:
                    print("Goodbye sir!")
                else:
                    say("Goodbye sir!")
                break
                
            performAction(task, muted=is_silent)
            
        except KeyboardInterrupt:
            print("\nForce quitting...")
            exit()

if __name__ == "__main__":
    main()