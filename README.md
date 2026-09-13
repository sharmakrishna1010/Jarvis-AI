# J.A.R.V.I.S. - Intelligent AI Desktop Assistant

An advanced, modular, and voice-activated AI desktop assistant built with Python. J.A.R.V.I.S. operates as an active agent, utilizing a Tool Registry pattern to intelligently route actions, manage files, and bootstrap development projects. It features a resilient four-step Multi-Brain LLM fallback architecture (Gemini 3.5 Flash → Mistral → Gemini 3.5 Flash-Lite → OpenRouter), a fully dynamic ChromaDB-backed memory and preference system, live news fetching, media playback control, and local GPU-accelerated Kokoro-82M text-to-speech for zero-latency, human-like voice responses.

## Features
* **Multi-Brain Fallback System:** A four-step reasoning cascade for maximum uptime against rate limits and outages:
  1. `gemini-3.5-flash` — primary reasoning engine for complex action routing
  2. `mistral-small-latest` — first fallback
  3. `gemini-3.5-flash-lite` — second fallback, higher free-tier quota than the primary model
  4. OpenRouter's free pool — last-resort safety net

  All four steps cap output at 500 tokens and log the actual exception on failure, so a dead provider never goes unnoticed.
* **Dynamic Preference & Memory System (ChromaDB):**
  * *Preferences:* Stored in a dedicated `preference` collection with full CRUD support (`save_preference`, `delete_preference`, `recall_preference_memories`). Saving upserts by key with a timestamp, so the newest value always wins — no static config file required.
  * *Long-Term Recall:* A separate `conversation_history` collection provides semantic search and stateful recall of general facts across reboots.
  * *Short-Term Working Memory:* A sliding-window context buffer keeps multi-turn conversations coherent without losing the immediate topic.
  * Greetings and personalization (name, honorific, etc.) are resolved live from ChromaDB on every run — nothing is hardcoded.
* **Live News Fetching:** Four news tools backed by Google News RSS:
  * `GET_TOP_HEADLINES` — top global headlines
  * `GET_TOPIC_NEWS` — news by topic (e.g. technology, business)
  * `GET_GEO_NEWS` — news by country, using a locale-aware `COUNTRY_CODES` map (~195 countries + common aliases like `uk`, `usa`, `uae`) with automatic fallback to keyword search when a country has no dedicated Google News edition
  * `GET_SEARCH_NEWS` — free-text news search
  * Results are returned as clean numbered lists, ready for the TTS layer.
* **Media Playback Control:** Hotkey-based control via `pyautogui` — play/pause, volume up/down, next/previous track — triggerable entirely by voice.
* **Dynamic Context Awareness:** Automatically injects real-time date, time, and location data into the agent's processing pipeline for accurate, context-aware responses without relying on web searches.
* **Real-Time System Monitoring:** Native OS-level resource tracking, allowing the AI to instantly analyze and audibly report live CPU utilization and RAM capacity on command.
* **Multi-Mode Interface:** Select how you interact based on your environment:
  * *Voice Mode:* Standard hands-free speech recognition.
  * *Night Mode:* Type your commands, but J.A.R.V.I.S. replies audibly through your headphones.
  * *Silent Mode:* Pure text input/output for quiet environments.
* **Scalable Tool Registry:** Built on an extensible dispatcher pattern. `TOOL_REGISTRY` maps action tags directly to isolated tool functions, and `SPEAK_RESULT_ACTIONS` is derived dynamically from its keys — adding a new tool never requires touching the dispatch logic by hand.
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
Install the core Python packages, including the required API SDKs, vector database, news, media control, and system utilities:
```bash
pip install mistralai google-genai openrouter soundfile sounddevice speechrecognition python-dotenv kokoro chromadb psutil pygooglenews pyautogui
```
Install the CUDA-enabled version of PyTorch for GPU acceleration:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**4. Environment Variables**
Create a `.env` file in the root directory and add your API credentials:
```env
GEMINI_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

**5. First-run preferences**
There's no config file to edit before launch. On first run, just tell J.A.R.V.I.S. how to address you and where you're based, and it saves those as preferences in ChromaDB automatically, for example:
```text
You: call me Boss
You: my location is Delhi, India
```
Every preference is upserted by key with a timestamp, so the latest value you give always takes priority, and it persists across reboots.

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
Allowing an LLM to interface with your OS inherently carries risk. This project utilizes an `is_safe_command()` filter within the tools directory that blocks dangerous keywords (`del`, `format`, `rmdir`, etc.). Do not remove this filter without understanding the consequences of unrestricted subprocess execution. Ensure your `jarvis_memory` directory is added to your `.gitignore` to prevent sensitive data (including your ChromaDB preference store) from being pushed to public repositories.