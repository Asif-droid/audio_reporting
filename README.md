# Audio Speech Recognition and Processing

This repository contains tools and scripts for processing audio files, performing speech recognition, and generating content based on prompts. It leverages the `google.genai` library for AI-powered content generation.



### Key Files and Directories

- **`processor.py`**: Main script for uploading audio files, reading prompts, and generating AI-powered responses.
- **`Audio_Speech_Recognition.ipynb`**: Jupyter Notebook for speech recognition and audio processing experiments.
- **`prompts/`**: Contains text prompts used for content generation.
- **`wavs/`**: Directory containing audio files in `.wav` format.
- **`.gitignore`**: Specifies files to be ignored by Git, such as `.ogg` files.

## Dependencies

- Python 3.7 or higher
- `google.genai` library

Install dependencies using pip:

```bash
pip install google-genai
python processor.py

```