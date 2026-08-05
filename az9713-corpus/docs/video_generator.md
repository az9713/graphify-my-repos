---
repo: video_generator
description: 
language: Python
stars: 0
forks: 0
created: 2025-06-25
updated: 2025-06-25
topics: 
is_fork: False
kb: 9
---

# video_generator
# Video Generator with Synchronized Audio

A Python application that generates videos from text prompts using FAL.AI's Seedance and MMAudio APIs. The application creates a 5-second video (16:9 aspect ratio, 720p resolution) from your text description and then adds synchronized audio to create a complete audiovisual experience.

## Features

- 🎬 Generate videos from text descriptions using Seedance 1.0 Lite
- 🎵 Add synchronized audio using MMAudio-v2
- 📁 Automatic local video saving with timestamps
- 🔧 Cross-platform support (Windows, Linux, macOS)
- 📝 Comprehensive logging and error handling
- 🖥️ Command-line interface for easy usage
- ⚙️ Configurable output directories and audio prompts

## Prerequisites

- Python 3.8 or higher
- FAL.AI API key (get one at [https://fal.ai/dashboard/keys](https://fal.ai/dashboard/keys))
- Internet connection for API calls

## Installation

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd video_generator
```

### 2. Install Dependencies

#### For Google Colab:
```bash
pip install -r requirements.txt
```

#### For Local Development (with Virtual Environment):

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your FAL.AI API key:
   ```
   FAL_KEY=your_actual_fal_api_key_here
   ```

## Usage

### Command Line Interface

The application provides a simple command-line interface:

```bash
cd src
python cli.py "Your video prompt here"
```

#### Basic Examples:

```bash
# Generate a video with default audio
python cli.py "A cat playing in a sunny garden"

# Generate a video with custom audio prompt
python cli.py "A peaceful ocean sunset" --audio "Relaxing ocean waves and seagulls"

# Specify custom output directory
python cli.py "A bustling city street" --output ../my_videos
```

#### Command Line Options:

- `prompt` (required): Text description for video generation
- `--audio`, `-a`: Optional audio prompt (if different from video prompt)
- `--output`, `-o`: Output directory for generated videos (default: `videos`)

### Programmatic Usage

You can also use the VideoGenerator class directly in your Python code:

```python
from video_generator import VideoGenerator

# Initialize the generator
generator = VideoGenerator(output_dir="my_videos")

# Generate a video with synchronized audio
video_path = generator.generate_video_from_text(
    prompt="A dog running through a meadow",
    audio_prompt="Happy dog barking and nature sounds"
)

print(f"Video saved to: {video_path}")
```

## Configuration

### Environment Variables

You can configure the application using environment variables in your `.env` file:

```env
# Required: Your FAL.AI API key
FAL_KEY=your_fal_api_key_here

# Optional: Default output directory
OUTPUT_DIR=videos

# Optional: Log level (DEBUG, INFO, WARNING, ERROR)
LOG_LEVEL=INFO
```

### Video Generation Parameters

The application uses the following fixed parameters optimized for quality:

- **Aspect Ratio**: 16:9
- **Resolution**: 720p
- **Duration**: 5 seconds
- **Audio Steps**: 25
- **CFG Strength**: 4.5

## Project Structure

```
video_generator/
├── src/
│   ├── video_generator.py    # Main application logic
│   └── cli.py               # Command-line interface
├── videos/                  # Generated videos (created automatically)
├── logs/                   # Application logs (created automatically)
├── config/                 # Configuration files
├── tests/                  # Unit tests
├── requirements.txt        # Python dependencies
├── setup.py               # Package setup
├── .env.example           # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Output

Generated videos are saved in the `videos` directory (or your specified output directory) with the following naming convention:

```
generated_video_YYYYMMDD_HHMMSS.mp4
```

Example: `generated_video_20241225_143022.mp4`

## Logging

The application creates detailed logs in the `logs` directory with timestamps. Logs include:

- Video generation progress
- API call status
- Error messages and debugging information
- File download progress

Log files are named: `video_generator_YYYYMMDD_HHMMSS.log`

## Error Handling

The application handles various error scenarios:

- Missing or invalid API keys
- Network connectivity issues
- API rate limiting
- File system permissions
- Invalid prompts or parameters

All errors are logged with detailed information to help with troubleshooting.

## Troubleshooting

### Common Issues

1. **"FAL_KEY environment variable is required"**
   - Make sure you've created a `.env` file with your API key
   - Verify the API key is correct and has sufficient credits

2. **"Permission denied" errors**
   - Ensure the application has write permissions to the output directory
   - Try running with elevated permissions if necessary

3. **"Connection timeout" errors**
   - Check your internet connection
   - The APIs may be experiencing high load - try again later

4. **"Invalid prompt" errors**
   - Ensure your prompt is descriptive and not empty
   - Avoid prompts that might violate content policies

### Getting Help

If you encounter issues:

1. Check the logs in the `logs` directory for detailed error information
2. Verify your API key and credits at [https://fal.ai/dashboard](https://fal.ai/dashboard)
3. Ensure all dependencies are properly installed
4. Try with a simple prompt first to verify the setup

## API Costs

Please note that both Seedance and MMAudio APIs are paid services. Check your usage and costs at the [FAL.AI dashboard](https://fal.ai/dashboard).

Approximate costs per video generation:
- Seedance (video generation): ~$0.05-0.10
- MMAudio (audio addition): ~$0.03-0.08

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Acknowledgments

- [FAL.AI](https://fal.ai) for providing the Seedance and MMAudio APIs
- [Bytedance](https://www.bytedance.com) for the Seedance model
- The open-source community for the various Python packages used

---

**Note**: This application requires active internet connection and valid FAL.AI API credentials. Generated videos are subject to the terms of service of the respective AI models.