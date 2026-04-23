# J.A.R.V.I.S. - Intelligent Dual-Mode Desktop Assistant

An advanced, modular, and voice-activated AI desktop assistant built with Python. J.A.R.V.I.S. operates as an active agent, utilizing a Tool Registry pattern to intelligently route actions, manage files, and bootstrap development projects. It features a Dual-Brain LLM architecture (Google Gemini with a Mistral AI fallback) and local GPU-accelerated Kokoro-82M text-to-speech for zero-latency, human-like voice responses.

## ✨ Features
* **Dual-Brain Fallback System:** Uses `gemini-2.5-flash` as the primary reasoning engine for complex action routing, with automatic seamless fallback to `mistral-small-latest` during rate limits or server outages.
* **Multi-Mode Interface:** Select how you interact based on your environment:
  * *Voice Mode:* Standard hands-free speech recognition.
  * *Night Mode:* Type your commands, but J.A.R.V.I.S. replies audibly through your headphones.
  * *Silent Mode:* Pure text input/output for quiet environments.
* **Scalable Tool Registry:** Built on an extensible dispatcher pattern. The AI outputs structured `[ACTION]` tags, which Python dynamically routes to isolated tools without relying on raw, fragile shell commands.
* **Local GPU-Accelerated Voice:** Uses Kokoro-82M running locally on PyTorch/CUDA for incredibly fast and realistic voice synthesis.
* **Built-in Developer Tools:** Natively understands how to bootstrap React, Next.js, Django, and Flutter apps in specified local directories via standard paths (e.g., "Downloads" or "Desktop").
* **Command Security Firewall:** Includes a strict blocklist to intercept and block destructive terminal operations.



## 🗂️ Project Structure
```text
Jarvis-AI/
├── main.py              # The core execution loop and Multi-Mode selector
├── llm_brain.py         # Dual-Brain wrapper handling Gemini & Mistral APIs and system prompts
├── audio_engine.py      # Manages STT input and Kokoro local TTS output
├── action.py            # The Dispatcher: parses AI intent and routes to the registry
├── registry.py          # The Tool Registry mapping action tags to Python functions
├── tools/               # Isolated skills directory
│   ├── file_ops.py      # File creation, text writing, and directory management
│   ├── dev_ops.py       # Scaffolding tools (React, Next.js, Flutter, etc.)
│   └── system_ops.py    # Safe CMD execution, browser automation, etc.
├── sites.py             # Configuration for hardcoded quick-launch websites
├── userPref.py          # User personalization (Username, Call Name, OS Version)
├── .env                 # Environment variables (API Keys)
└── .gitignore           # Git tracking exclusions
```

## 🛠️ Prerequisites
* **Python 3.12** (Highly recommended for package compatibility)
* **NVIDIA GPU** with CUDA support (for fast local TTS)
* **eSpeak-NG**: Required backend for Kokoro TTS. [Download here](https://github.com/espeak-ng/espeak-ng/releases) (Windows `.msi` installer).

## 🚀 Installation & Setup

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/Jarvis-AI.git
cd Jarvis-AI
```

**2. Set up the virtual environment**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**3. Install dependencies**
Install the core Python packages, including the new Google GenAI SDK:
```bash
pip install mistralai google-genai soundfile sounddevice speechrecognition python-dotenv kokoro
```
Install the CUDA-enabled version of PyTorch for GPU acceleration:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**4. Configure User Preferences**
Configure the `userPref.py` file in the root directory:
```python
# userPref.py
userName = "Your Name"
callMe = "Sir" 
operatingSystem = "Windows 11" 
```

**5. Environment Variables**
Create a `.env` file in the root directory and add your API credentials:
```env
GEMINI_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
HF_TOKEN=your_huggingface_token_here
```

## 💻 Usage
Ensure your virtual environment is active, then start the system:
```powershell
python main.py
```
Upon launching, you will be prompted to select your input mode:
```text
========================================
 JARVIS INITIALIZED
========================================
Select Input Mode:
[1] Voice Mode (Standard)
[2] Night Mode (Type commands, audio responses)
[3] Silent Mode (Type commands, text responses only - no audio)

Enter mode (1/2/3): 
```
Select your mode, wait for the TTS models to load on CUDA, and begin issuing commands!

## 🛡️ Security Note
Allowing an LLM to interface with your OS inherently carries risk. This project utilizes an `is_safe_command()` filter within `tools/system_ops.py` that blocks dangerous keywords (`del`, `format`, `rmdir`, etc.). **Do not remove this filter** without understanding the consequences of unrestricted `subprocess.Popen` execution.