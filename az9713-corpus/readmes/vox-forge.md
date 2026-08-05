# Voice Web Builder

A real-time voice-controlled web application builder powered by AI. Speak your commands and watch as AI generates live, working web pages, games, and interactive experiences - no coding required!

## What is Voice Web Builder?

Voice Web Builder lets you create web pages using just your voice. Instead of writing code, you simply describe what you want:

- Say "Create a page with a blue heading that says Hello World" and watch it appear
- Say "Add a bouncing ball animation" and see physics in action
- Say "Generate an image of a sunset" and AI creates it for you

This is made possible by combining three AI technologies:
1. **Speech Recognition** (OpenAI Whisper) - Converts your voice to text
2. **Code Generation** (Google Gemini) - Turns your text into working code
3. **Image Generation** (Google Imagen) - Creates images from descriptions

## Quick Links

- **New to this project?** Start with the [Quick Start Guide](docs/QUICK_START.md)
- **Want to use the app?** Read the [User Guide](docs/USER_GUIDE.md)
- **Want to develop?** Read the [Developer Guide](docs/DEVELOPER_GUIDE.md)

## Features at a Glance

| Feature | Description |
|---------|-------------|
| Voice Control | Press T key to talk, release to execute |
| Real-time Preview | See your creation instantly in the browser |
| AI Images | Generate any image by describing it |
| Package Support | Use libraries like Three.js, Chart.js automatically |
| Incremental Editing | Build on top of what you've created |
| Safe Execution | Code runs in a secure sandbox |

## System Requirements

Before you begin, ensure you have:

1. **Node.js 18 or newer**
   - Download from: https://nodejs.org/
   - To check your version: `node --version`

2. **FFmpeg** (for audio processing)
   - Windows: `winget install ffmpeg`
   - Mac: `brew install ffmpeg`
   - Linux: `sudo apt install ffmpeg`
   - To check: `ffmpeg -version`

3. **A modern web browser**
   - Chrome, Edge, Firefox, or Safari
   - Must allow microphone access

4. **API Keys** (free tiers available)
   - OpenAI API key: https://platform.openai.com/api-keys
   - Google AI Studio API key: https://aistudio.google.com/apikey

## Installation (Step-by-Step)

### Step 1: Download the Project

If you have Git installed:
```bash
git clone https://github.com/az9713/vox-forge.git
cd vox-forge
```

Or download and extract the ZIP file, then open a terminal in that folder.

### Step 2: Install Dependencies

```bash
npm install
```

This downloads all required packages. Wait until it completes (may take 1-2 minutes).

### Step 3: Configure API Keys

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   On Windows without bash, manually copy `.env.example` to `.env`

2. Open `.env` in a text editor and add your keys:
   ```
   OPENAI_API_KEY=sk-your-openai-key-here
   GEMINI_API_KEY=your-gemini-key-here
   PORT=3000
   ```

### Step 4: Start the Server

```bash
npm start
```

You should see:
```
Voice Web Builder server running on http://localhost:3000
```

### Step 5: Open in Browser

Navigate to `http://localhost:3000` in your browser.

### Step 6: Grant Microphone Permission

When prompted, click "Allow" to enable microphone access.

## Your First Voice Command

1. **Press and hold the T key** on your keyboard
2. **Say**: "Create a heading that says Hello World"
3. **Release the T key**
4. Watch as the AI transcribes your speech and generates the page!

## Example Commands to Try

| Command | What Happens |
|---------|--------------|
| "Add a red button that says Click Me" | Creates a styled button |
| "Make a bouncing ball animation" | Creates animated physics |
| "Add an image of a cute cat" | Generates an AI image |
| "Create a counter that increases when I click" | Interactive JavaScript |
| "Start over" or "Reset the page" | Clears everything |

## Troubleshooting

### "Microphone not working"
- Check browser permissions (click the lock icon in the address bar)
- Make sure no other app is using the microphone
- Try refreshing the page

### "WebSocket disconnected"
- The page will try to reconnect automatically
- If it fails, refresh the page
- Check if the server is still running

### "Rate limit error"
- The app will automatically retry after waiting
- If it persists, wait 30 seconds between commands

### "Transcription failed"
- Speak clearly and hold T key for at least 1 second
- Check the server console for specific errors

## Project Structure

```
voice-web-builder/
├── server/           # Backend (Node.js)
│   ├── index.js      # Server entry point
│   ├── websocket.js  # Real-time communication
│   ├── services/     # AI integrations
│   └── tools/        # AI-callable tools
├── public/           # Frontend (Browser)
│   ├── index.html    # Main page
│   ├── css/          # Styles
│   └── js/           # JavaScript modules
├── docs/             # Documentation
│   ├── QUICK_START.md
│   ├── USER_GUIDE.md
│   └── DEVELOPER_GUIDE.md
├── CLAUDE.md         # AI assistant guide
└── package.json      # Project config
```

## Documentation

| Document | For | Description |
|----------|-----|-------------|
| [Quick Start](docs/QUICK_START.md) | Everyone | 10 hands-on examples to get started |
| [User Guide](docs/USER_GUIDE.md) | Users | Complete guide to using the app |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Developers | Technical docs for extending the app |
| [CLAUDE.md](CLAUDE.md) | AI Assistants | Context for AI coding assistants |

## How It Works (The Big Picture)

```
┌─────────────────────────────────────────────────────────────────┐
│                        YOUR BROWSER                              │
├─────────────────────────────────────────────────────────────────┤
│  1. You press T and speak     4. Preview updates live           │
│  2. Audio is captured         ←─────────────────────────        │
│  3. Sent to server            │                                 │
│         │                     │                                 │
└─────────┼─────────────────────┼─────────────────────────────────┘
          │                     │
          ▼                     │
┌─────────────────────────────────────────────────────────────────┐
│                        THE SERVER                                │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │   Whisper    │───▶│   Gemini     │───▶│  Generated   │      │
│  │  (Speech to  │    │  (Text to    │    │    Code      │──────┘
│  │    Text)     │    │    Code)     │    │  (HTML/CSS)  │
│  └──────────────┘    └──────────────┘    └──────────────┘
│                             │
│                             ▼
│                      ┌──────────────┐
│                      │   Imagen     │
│                      │  (Generate   │
│                      │   Images)    │
│                      └──────────────┘
└─────────────────────────────────────────────────────────────────┘
```

## Acknowledgments

This project was inspired by [Shipmas Day 15: Gemini 3 Flash CHANGED My Life!](https://www.youtube.com/watch?v=imrmbtvDV6c) by All About AI.

### Generated with AI

All code and documentation for this project were generated by **[Claude Code](https://claude.com/claude-code)** powered by **Claude Opus 4.5** (Anthropic's most advanced AI model).

## API Documentation References

This project uses the following APIs. Refer to their official documentation for more details:

| API | Documentation |
|-----|---------------|
| **Gemini Text Generation** | https://ai.google.dev/gemini-api/docs/text-generation |
| **Gemini Function Calling** | https://ai.google.dev/gemini-api/docs/function-calling |
| **Google Imagen** | https://ai.google.dev/gemini-api/docs/imagen |
| **OpenAI Speech-to-Text** | https://platform.openai.com/docs/guides/speech-to-text |

## Contributing

Contributions are welcome! Please read the [Developer Guide](docs/DEVELOPER_GUIDE.md) first.

## License

MIT License - feel free to use, modify, and distribute.

## Support

If you encounter issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Read the detailed [User Guide](docs/USER_GUIDE.md)
3. Check the server console for error messages
4. Open an issue on GitHub

---

**Happy voice coding!** Start with the [Quick Start Guide](docs/QUICK_START.md) to see what you can build.
