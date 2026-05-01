# J.A.R.V.I.S. - Intelligent AI Desktop Assistant

An advanced, modular, and voice-activated AI desktop assistant built with Python. J.A.R.V.I.S. operates as an active agent, utilizing a Tool Registry pattern to intelligently route actions, manage files, and bootstrap development projects. It features a resilient Multi-Brain LLM fallback architecture (Google Gemini → Mistral → OpenRouter), a dual-tier memory system, and local GPU-accelerated Kokoro-82M text-to-speech for zero-latency, human-like voice responses.

## Features
* **Multi-Brain Fallback System:** Uses `gemini-2.5-flash` as the primary reasoning engine for complex action routing, with an automatic, seamless fallback cascade to `mistral-small-latest` and OpenRouter's free pool as the final safety net. 
* **Dual-Tier Memory Architecture:** 
  * *Long-Term Persistent Recall:* Integrates a local ChromaDB vector database with chronological timestamping. This provides semantic search and stateful recall, allowing the agent to remember and accurately override user preferences across system reboots.
  * *Short-Term Working Memory:* Utilizes a sliding-window context buffer to maintain natural, multi-turn conversational flow without losing track of the immediate topic.
* **Dynamic Context Awareness:** Automatically injects real-time date, time, and location data into the agent's processing pipeline for accurate, context-aware responses without relying on web searches.
* **Real-Time System Monitoring:** Features native OS-level resource tracking, allowing the AI to instantly analyze and audibly report live CPU utilization and RAM capacity on command.
* **Multi-Mode Interface:** Select how you interact based on your environment:
  * *Voice Mode:* Standard hands-free speech recognition.
  * *Night Mode:* Type your commands, but J.A.R.V.I.S. replies audibly through your headphones.
  * *Silent Mode:* Pure text input/output for quiet environments.
* **Scalable Tool Registry:** Built on an extensible dispatcher pattern. The AI outputs structured action tags, which Python dynamically routes to isolated tools without relying on raw, fragile shell commands.
* **Local GPU-Accelerated Voice:** Uses Kokoro-82M running locally on PyTorch/CUDA (configured with a crisp British dialect) for incredibly fast and realistic voice synthesis.
* **Built-in Developer Tools:** Natively understands how to bootstrap React, Next.js, Django, and Flutter apps in specified local directories via standard paths.
* **Command Security Firewall:** Includes a strict blocklist to intercept and block destructive terminal operations.

## Prerequisites
* **Python 3.12** (Highly recommended for package compatibility)
* **NVIDIA GPU** with CUDA support (for fast local TTS)
* **eSpeak-NG**: Required backend for Kokoro TTS. [Download here](https://github.com/espeak-ng/espeak-ng/releases) (Windows `.msi` installer).

## Installation & Setup

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
Install the core Python packages, including the required API SDKs, vector database, and system utilities:
```bash
pip install mistralai google-genai openrouter soundfile sounddevice speechrecognition python-dotenv kokoro chromadb psutil
```
Install the CUDA-enabled version of PyTorch for GPU acceleration:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**4. Configure User Preferences**
Configure the `userPref.py` file inside the `config/` directory:
```python
# config/userPref.py
userName = "Your Name"
callMe = "Sir" 
operatingSystem = "Windows 11" 
preferredBrowser = "chrome" 
location = "Delhi, India"
```

**5. Environment Variables**
Create a `.env` file in the root directory and add your API credentials:
```env
GEMINI_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

## Usage
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
Select your mode, wait for the TTS models to load on CUDA, and begin issuing commands.

## Security Note
Allowing an LLM to interface with your OS inherently carries risk. This project utilizes an `is_safe_command()` filter within the tools directory that blocks dangerous keywords (`del`, `format`, `rmdir`, etc.). Do not remove this filter without understanding the consequences of unrestricted subprocess execution. Ensure your `jarvis_memory` directory is added to your `.gitignore` to prevent sensitive data from being pushed to public repositories.