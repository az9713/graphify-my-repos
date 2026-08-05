---
repo: news-tts-reader
description: AI-powered news reader with text-to-speech
language: Python
stars: 0
forks: 0
created: 2025-06-23
updated: 2025-06-23
topics: 
is_fork: False
kb: 19
---

# news-tts-reader
# News TTS Reader 🗞️🔊

A Python application that fetches today's top news headlines and converts them to speech using ElevenLabs Text-to-Speech API. Perfect for staying informed while multitasking or for accessibility purposes.

> **Developed using [Claude Code](https://docs.anthropic.com/en/docs/claude-code) with Context7 MCP for enhanced API documentation access and development assistance.**

## Features

- 📰 Fetches latest news from multiple reliable sources (BBC, CNN, Reuters)
- 🎙️ High-quality text-to-speech conversion using ElevenLabs AI
- 💾 Saves audio files for offline listening
- 🎵 Automatic audio playback (when supported)
- 📱 Clean text processing and formatting
- ⚙️ Configurable voice selection
- 🔧 Environment-based configuration

## How It Works

The application follows this workflow:

1. **News Fetching**: Retrieves RSS feeds from major news sources
2. **Content Processing**: Cleans and formats news articles for optimal speech synthesis
3. **Speech Generation**: Uses ElevenLabs API to convert text to natural-sounding speech
4. **Audio Output**: Saves audio file and attempts to play it automatically
5. **Text Display**: Shows the news summary in the terminal

## Code Structure

```
news_reader.py          # Main application file
├── NewsReader class    # Core functionality
│   ├── __init__()     # Initialize ElevenLabs client
│   ├── fetch_news()   # Retrieve news from RSS feeds
│   ├── clean_text()   # Process text for TTS
│   ├── generate_news_summary() # Create spoken summary
│   ├── text_to_speech() # Convert text to audio
│   ├── save_audio()   # Save MP3 file
│   └── run()          # Main execution flow
└── main()             # Entry point with error handling
```

## Requirements

### System Requirements

#### Windows
- **OS**: Windows 10 or later (Windows 11 recommended)
- **Python**: Python 3.7 or higher ([Download from python.org](https://python.org/downloads/))
- **Internet**: Broadband connection for news fetching and TTS API
- **Audio**: Windows audio drivers and speakers/headphones
- **Terminal**: Command Prompt, PowerShell, or Windows Terminal

#### Linux
- **OS**: Ubuntu 18.04+, Debian 10+, CentOS 7+, or other modern distributions
- **Python**: Python 3.7 or higher (usually pre-installed)
- **Internet**: Active network connection
- **Audio**: ALSA, PulseAudio, or pipewire for audio playback
- **Packages**: `python3-pip`, `python3-venv` (install via package manager)

#### Common Requirements
- **Storage**: 50MB free disk space minimum
- **Memory**: 512MB RAM minimum (1GB recommended)
- **Network**: Unrestricted HTTP/HTTPS access for RSS feeds and API calls

### Python Dependencies
- `requests` - HTTP requests for RSS feeds
- `elevenlabs` - ElevenLabs TTS API client  
- `python-dotenv` - Environment variable management
- `feedparser` - RSS feed parsing

## Installation & Setup

### Prerequisites Installation

#### Windows Setup

1. **Install Python**
   ```cmd
   # Download Python from https://python.org/downloads/
   # During installation, check "Add Python to PATH"
   # Verify installation:
   python --version
   python -m pip --version
   ```

2. **Install Git (Optional)**
   ```cmd
   # Download from https://git-scm.com/download/win
   # Or use GitHub Desktop for GUI
   ```

#### Linux Setup

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git
# Verify installation
python3 --version
pip3 --version
```

**CentOS/RHEL/Fedora:**
```bash
# CentOS/RHEL 7/8
sudo yum install python3 python3-pip git
# OR Fedora
sudo dnf install python3 python3-pip git

# Verify installation
python3 --version
pip3 --version
```

### Project Setup

#### 1. Download Project Files

**Option A: Using Git (Recommended)**
```bash
# Windows (Command Prompt/PowerShell)
git clone <repository-url>
cd news-tts-reader

# Linux/macOS
git clone <repository-url>
cd news-tts-reader
```

**Option B: Manual Download**
- Download and extract the project files to a folder
- Open terminal/command prompt in that folder

#### 2. Create Virtual Environment (Recommended)

**Windows:**
```cmd
# Create virtual environment
python -m venv news-tts-env

# Activate virtual environment
news-tts-env\Scripts\activate

# Your prompt should now show (news-tts-env)
```

**Linux:**
```bash
# Create virtual environment
python3 -m venv news-tts-env

# Activate virtual environment
source news-tts-env/bin/activate

# Your prompt should now show (news-tts-env)
```

#### 3. Install Python Dependencies

**Windows:**
```cmd
# Make sure virtual environment is activated
pip install -r requirements.txt

# Verify installation
pip list
```

**Linux:**
```bash
# Make sure virtual environment is activated
pip install -r requirements.txt
# OR if pip3 is required
pip3 install -r requirements.txt

# Verify installation
pip list
```

#### 4. ElevenLabs API Setup
1. Visit [ElevenLabs](https://elevenlabs.io/) and create an account
2. Navigate to your profile settings to get your API key
3. Copy the provided API key (starts with `sk-`)

#### 5. Environment Configuration

**Windows:**
```cmd
# Copy the example file
copy .env.example .env

# Edit with notepad or your preferred editor
notepad .env
# OR
code .env    # if you have VS Code installed
```

**Linux:**
```bash
# Copy the example file
cp .env.example .env

# Edit with your preferred editor
nano .env
# OR
vim .env
# OR
code .env    # if you have VS Code installed
```

Add your API key to the `.env` file:
```env
ELEVENLABS_API_KEY=sk-your-api-key-here
ELEVENLABS_VOICE_ID=JBFqnCBsd6RMkjVDRZzb
```

#### 6. Voice Selection (Optional)

Create a temporary script to list available voices:

**Windows:**
```cmd
# Create and run voice list script
echo from elevenlabs.client import ElevenLabs > list_voices.py
echo import os >> list_voices.py
echo from dotenv import load_dotenv >> list_voices.py
echo load_dotenv() >> list_voices.py
echo client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY')) >> list_voices.py
echo voices = client.voices.search() >> list_voices.py
echo for voice in voices.voices: print(f"Name: {voice.name}, ID: {voice.voice_id}") >> list_voices.py

python list_voices.py
del list_voices.py
```

**Linux:**
```bash
# Create and run voice list script
cat > list_voices.py << 'EOF'
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv
load_dotenv()
client = ElevenLabs(api_key=os.getenv('ELEVENLABS_API_KEY'))
voices = client.voices.search()
for voice in voices.voices:
    print(f"Name: {voice.name}, ID: {voice.voice_id}")
EOF

python3 list_voices.py
rm list_voices.py
```

Update `ELEVENLABS_VOICE_ID` in your `.env` file with your preferred voice ID.

## Usage

### Running the Application

#### Windows
```cmd
# Make sure virtual environment is activated (if using)
news-tts-env\Scripts\activate

# Run the application
python news_reader.py
```

#### Linux
```bash
# Make sure virtual environment is activated (if using)
source news-tts-env/bin/activate

# Run the application
python3 news_reader.py
```

### What Happens When You Run It
1. **Initialization**: Loads environment variables and initializes ElevenLabs client
2. **News Fetching**: Retrieves latest headlines from BBC, CNN, and Reuters
3. **Processing**: Cleans HTML tags and formats text for speech
4. **Summary Generation**: Creates a structured news summary with date
5. **TTS Conversion**: Converts text to high-quality speech audio
6. **Output**: Saves `news_summary.mp3` and displays text summary

### Sample Output
```
Fetching today's top news...
Found 5 articles. Generating summary...
Converting to speech...
Audio saved as news_summary.mp3
==================================================
NEWS SUMMARY:
==================================================
Good day! Here are today's top news stories for December 23, 2024.

Story 1: Breaking: Major Climate Agreement Reached at Global Summit.
World leaders announce unprecedented cooperation on carbon reduction targets...

Story 2: Technology Giant Announces Revolutionary AI Breakthrough.
New artificial intelligence system shows human-level reasoning capabilities...
...
```

## Configuration Options

### Environment Variables
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `ELEVENLABS_API_KEY` | Your ElevenLabs API key | None | Yes |
| `ELEVENLABS_VOICE_ID` | Voice ID for TTS | `JBFqnCBsd6RMkjVDRZzb` | No |

### Voice Options
- **Default Voice**: Natural, professional news reader voice
- **Custom Voices**: Use any voice from your ElevenLabs account
- **Voice Cloning**: Clone voices using ElevenLabs voice cloning feature

### News Sources
Currently configured sources:
- BBC News RSS Feed
- CNN International RSS Feed  
- Reuters Top News RSS Feed

## Troubleshooting

### Common Issues

#### Environment and Setup Issues

**"ELEVENLABS_API_KEY not found in environment variables"**

*Windows:*
- Ensure `.env` file exists in the project directory
- Check file contents with: `type .env`
- Verify no extra spaces around the API key
- Try restarting Command Prompt/PowerShell after creating `.env`

*Linux:*
- Ensure `.env` file exists: `ls -la .env`
- Check file contents with: `cat .env`
- Verify file permissions: `chmod 600 .env`
- Check for hidden characters: `cat -A .env`

**"python/python3 command not found"**

*Windows:*
- Reinstall Python with "Add to PATH" option checked
- Try `py` command instead of `python`
- Add Python manually to PATH in System Environment Variables

*Linux:*
- Install Python: `sudo apt install python3 python3-pip` (Ubuntu/Debian)
- Create symlink: `sudo ln -s /usr/bin/python3 /usr/bin/python`
- Check installation: `which python3`

**"pip command not found"**

*Windows:*
- Use `python -m pip` instead of `pip`
- Reinstall Python with pip option enabled

*Linux:*
- Install pip: `sudo apt install python3-pip`
- Use `python3 -m pip` instead of `pip`

#### Network and API Issues

**"Error fetching from [RSS URL]"**
- Check internet connection: `ping google.com`
- Test RSS URL in browser
- Check firewall/proxy settings
- RSS feeds may be temporarily unavailable

**"Error generating speech"**
- Verify ElevenLabs API key is valid and active
- Check account credits at https://elevenlabs.io/
- Test API key with simple curl command:
  ```bash
  curl -X GET "https://api.elevenlabs.io/v1/voices" \
       -H "xi-api-key: YOUR_API_KEY"
  ```
- Ensure voice ID is correct (try default voice first)

**"Connection timeout" or "Network error"**
- Check proxy settings if behind corporate firewall
- Try different network connection
- Increase timeout values in the code if needed

#### Audio Issues

**"Could not play audio automatically"**

The application has built-in cross-platform audio playback that works without ffmpeg:

*Windows:*
- Uses Windows' default audio player (`os.startfile()`)
- Should work automatically with Windows 10/11
- If issues persist, check Windows audio services are running
- Audio file is always saved as `news_summary.mp3` for manual playback

*Linux:*
- Automatically tries common audio players: `mpg123`, `ffplay`, `aplay`, `paplay`, `mplayer`, `vlc`
- Install recommended audio player: `sudo apt install mpg123`
- For other distros: `sudo yum install mpg123` or `sudo dnf install mpg123`
- Test audio system: `aplay /usr/share/sounds/alsa/Front_Left.wav`
- Check audio services: `pulseaudio --check -v`

*macOS:*
- Uses built-in `afplay` command (should work automatically)
- No additional software required

**"No audio output device found"**
- Connect headphones/speakers
- Check audio device settings in OS
- Verify audio services are running
- Try different audio backends

#### Permission Issues

**"Permission denied" errors**

*Windows:*
- Run Command Prompt as Administrator
- Check file/folder permissions
- Ensure antivirus isn't blocking execution

*Linux:*
- Check file permissions: `ls -la`
- Make script executable: `chmod +x news_reader.py`
- Check SELinux settings if applicable

#### Virtual Environment Issues

**Virtual environment not activating**

*Windows:*
```cmd
# If activation fails, try:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activating again
```

*Linux:*
```bash
# If activation fails, try:
source news-tts-env/bin/activate
# Or recreate the environment
rm -rf news-tts-env
python3 -m venv news-tts-env
```

### Platform-Specific Audio Setup

#### Windows Audio Setup
```cmd
# Install additional audio codecs if needed
# Windows should handle MP3 playback natively
# If issues persist, install VLC or similar media player
```

#### Audio Playback Setup

The application includes native audio playback for all platforms:

**Windows:**
- No additional setup required
- Uses Windows' default audio player
- Supports Windows 10/11 natively

**Linux - Recommended Setup:**

*Ubuntu/Debian:*
```bash
sudo apt update
sudo apt install mpg123 alsa-utils pulseaudio
# Test audio
speaker-test -t wav
mpg123 --test
```

*CentOS/RHEL/Fedora:*
```bash
# CentOS/RHEL
sudo yum install mpg123 alsa-utils pulseaudio
# Fedora
sudo dnf install mpg123 alsa-utils pulseaudio

# Test audio
speaker-test -t wav
```

**macOS:**
- No additional setup required
- Uses built-in `afplay` command

### Debug Mode
Enable verbose output by modifying the code:

```python
# Add at the beginning of main()
import logging
logging.basicConfig(level=logging.DEBUG)

# Or add debug prints in methods
def fetch_news(self, num_articles=5):
    print(f"DEBUG: Fetching {num_articles} articles...")
    # rest of the method
```

### Getting Help

1. **Check Requirements**: Ensure all system requirements are met
2. **Verify Installation**: Run `pip list` to see installed packages
3. **Test Components**: Test internet, API key, and audio separately
4. **Check Logs**: Look for detailed error messages in terminal output
5. **Update Dependencies**: Try `pip install --upgrade -r requirements.txt`

## Customization

### Adding News Sources
Edit the `news_sources` list in `fetch_news()` method:
```python
news_sources = [
    'https://feeds.bbci.co.uk/news/rss.xml',
    'https://rss.cnn.com/rss/edition.rss',
    'https://feeds.reuters.com/reuters/topNews',
    'https://your-additional-source.com/rss'  # Add more sources
]
```

### Modifying Summary Format
Edit the `generate_news_summary()` method to change how news is presented.

### Audio Settings
Adjust TTS parameters in `text_to_speech()` method:
```python
audio = self.client.text_to_speech.convert(
    text=text,
    voice_id=self.voice_id,
    model_id="eleven_multilingual_v2",  # Try different models
    output_format="mp3_44100_128"       # Adjust quality
)
```

## API Costs

ElevenLabs pricing (as of 2024):
- Free tier: 10,000 characters/month
- Paid plans: Starting from $5/month
- Each news summary typically uses 500-1500 characters

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Disclaimer

- This application is for educational and personal use
- News content belongs to respective news organizations
- ElevenLabs terms of service apply to TTS usage
- Ensure compliance with RSS feed usage policies

## Development Tools

This project was developed using modern AI-assisted development tools:

### 🤖 **Claude Code**
- **Tool**: [Anthropic Claude Code](https://docs.anthropic.com/en/docs/claude-code)
- **Usage**: Primary development environment for code generation, debugging, and documentation
- **Benefits**: Accelerated development with intelligent code assistance and cross-platform compatibility

### 📚 **Context7 MCP (Model Context Protocol)**
- **Tool**: Context7 MCP Server for API documentation access
- **Usage**: Real-time access to up-to-date ElevenLabs API documentation
- **Benefits**: Ensured compatibility with latest API changes and best practices
- **Integration**: Seamless documentation lookup during development

### 🎯 **ElevenLabs Integration**
- **API**: ElevenLabs Text-to-Speech API
- **Documentation**: Accessed via Context7 MCP for accurate implementation
- **Features**: High-quality voice synthesis with multiple voice options

### 🛠️ **Development Workflow**
1. **API Research**: Used Context7 MCP to fetch current ElevenLabs documentation
2. **Code Development**: Implemented features using Claude Code assistance
3. **Cross-Platform Testing**: Ensured Windows/Linux compatibility
4. **Documentation**: Comprehensive docs generated with AI assistance

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review ElevenLabs documentation
3. Check that all dependencies are correctly installed

---

**Enjoy staying informed with your personal AI news reader!** 🎧📰  
*Developed with Claude Code & Context7 MCP*