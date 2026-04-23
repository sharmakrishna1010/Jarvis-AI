# J.A.R.V.I.S. - Intelligent Voice Desktop Assistant

An advanced, modular, and voice-activated desktop assistant built with Python. J.A.R.V.I.S. leverages the Mistral AI API for conversational intelligence and system command generation, combined with the Kokoro-82M local text-to-speech (TTS) model for lightning-fast, ultra-realistic voice responses powered by CUDA.

## ✨ Features
* **Conversational AI:** Powered by `mistral-small-latest` for quick, intelligent, and context-aware dialogue.
* **Local GPU-Accelerated Voice:** Uses Kokoro-82M running locally on PyTorch/CUDA for zero-latency, human-like voice synthesis.
* **System Automation:** Automatically generates and executes terminal commands to open applications, manage windows, and control the OS.
* **Command Security Firewall:** Built-in interception layer that scans AI-generated commands against a blocklist to prevent destructive actions (e.g., blocks `del`, `format`, chain commands).
* **Modular Architecture:** Clean separation of concerns (audio, LLM processing, action execution) for easy scaling and debugging.

## 🗂️ Project Structure
```text
Jarvis-AI/
├── main.py              # The core execution loop connecting audio, brain, and actions
├── llm_brain.py         # Handles Mistral API integration and system prompt instructions
├── audio_engine.py      # Manages Google STT input and Kokoro local TTS output
├── action.py            # Parses AI intent, enforces security, and executes system commands
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
Install the core Python packages:
```bash
pip install mistralai soundfile sounddevice speechrecognition python-dotenv kokoro
```
Install the CUDA-enabled version of PyTorch for GPU acceleration:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**4. Configure User Preferences**
You must create or configure the `userPref.py` file in the root directory so the AI knows who you are and what operating system commands to generate. 
```python
# userPref.py
userName = "Your Name"
callMe = "Sir" # Or "Boss", "Creator", etc.
operatingSystem = "Windows 11" # Specify your exact OS
```

**5. Environment Variables**
Create a `.env` file in the root directory and add your API credentials:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
HF_TOKEN=your_huggingface_token_here
```

## 💻 Usage
Ensure your virtual environment is active, then start the main loop:
```powershell
python main.py
```
Wait for the `Loading Voice Models on: CUDA...` prompt, and then simply speak into your microphone!

## 🛡️ Security Note
Allowing an LLM to execute shell commands inherently carries risk. This project includes an `is_safe_command()` filter in `action.py` that blocks destructive operations. **Do not remove this filter** without understanding the consequences of unrestricted `shell=True` subprocess execution.
