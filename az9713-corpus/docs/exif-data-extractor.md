---
repo: exif-data-extractor
description: Extracts geolocation and date from images
language: Python
stars: 0
forks: 0
created: 2025-07-12
updated: 2025-07-12
topics: 
is_fork: False
kb: 5
---

# exif-data-extractor
# EXIF Data Extractor

This Python application extracts EXIF (Exchangeable Image File Format) data from images, including geolocation and the time the picture was taken. It features both a command-line interface (CLI) and a graphical user interface (GUI) for ease of use.

## Features

- **Dual-Mode Operation:** Run the application from the command line or use the intuitive drag-and-drop GUI.
- **EXIF Data Extraction:** Extracts key metadata from images, including GPS coordinates and the original date and time.
- **Reverse Geocoding:** Converts GPS coordinates into human-readable addresses using the Nominatim API.
- **Batch Processing:** Process a single image, multiple images, or an entire folder of images at once.
- **Progress Indicators:** Stay informed with progress indicators in both CLI and GUI modes.
- **Markdown Reports:** Generates a clean and easy-to-read markdown table with the extracted information.

## Dependencies

The application requires the following Python libraries:

- `exifread`: For extracting EXIF data from images.
- `geopy`: For reverse geocoding GPS coordinates.
- `tkinterdnd2`: For adding drag-and-drop functionality to the GUI.

## API Keys and Environment Variables

This application can optionally use the Gemini API for advanced image understanding features (though not currently implemented in the provided script). If you plan to extend the application to use the Gemini API, you will need to set up your API key.

1. **Obtain a Gemini API Key:**
   Follow the instructions [here](https://ai.google.dev/gemini-api/docs/get-started/python) to get your Gemini API key.

2. **Set up your environment variables:**
   Copy the `.env.example` file to a new file named `.env`:
   ```bash
   cp .env.example .env  # On Windows, use `copy .env.example .env`
   ```
   Open the newly created `.env` file and insert your Gemini API key:
   ```
   GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
   ```
   Replace `"YOUR_GEMINI_API_KEY"` with your actual API key.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/exif-data-extractor.git
   cd exif-data-extractor
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

The application can be run in either command-line mode or GUI mode.

### Command-Line Mode

To use the CLI, you need to provide the path to one or more images or folders as command-line arguments.

**To process a single image:**
```bash
python main.py path/to/your/image.jpg
```

**To process multiple images:**
```bash
python main.py image1.jpg image2.png
```

**To process a folder of images:**
```bash
python main.py path/to/your/folder
```

By default, the application will generate a markdown file named `exif_report.md`. You can specify a different output file using the `--output` flag:

```bash
python main.py path/to/your/folder --output my_report.md
```

### GUI Mode

To launch the GUI, use the `--gui` flag:

```bash
python main.py --gui
```

A window will appear where you can drag and drop your image files or folders. Once you've added your files, click the "Process Images" button to generate the report.

## Output

The application will generate a markdown file with a table containing the following information for each image:

| Image Name | Location | Time Taken |
|---|---|---|
| image1.jpg | 123 Main St, Anytown, USA | 2023:10:27 10:30:00 |
| image2.png | 456 Oak Ave, Somecity, USA | 2023:10:27 11:00:00 |

## Acknowledgements

This codebase was generated with the assistance of the Gemini CLI, a tool by Google.

## Contributing

Contributions are welcome! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
