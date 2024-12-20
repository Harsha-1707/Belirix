# Belirix: Image Analysis with Large Language Models

Belirix is a web application that allows users to analyze images using powerful Large Language Models (LLMs) through the Ollama framework. It leverages the LLaVA model family to provide insightful responses based on uploaded images and user-provided prompts.

## Features

*   **Image Upload and Preview:** Users can upload images (PNG, JPG, JPEG) and view a preview before analysis.
*   **Interactive Chat Interface:** A chat input allows users to ask specific questions about the uploaded image.
*   **LLaVA Model Integration:** Utilizes the LLaVA model family via Ollama for advanced image understanding.
*   **Streaming Responses:** Provides real-time, streamed responses from the LLM for a more interactive experience.
*   **Configurable Settings:** Allows customization of application title, available models, and system prompt.

## Prerequisites

*   Python 3.7+
*   Ollama (Installation instructions can be found on the [Ollama website](https://ollama.ai/))
*   Required Python packages (install using `pip`):

```bash
pip install -r requirements.txt
The requirements.txt file should contain the following:

streamlit
ollama
Pillow
python-dotenv
Installation
Clone the repository:
Bash

git clone [https://github.com/](https://github.com/)<your_username>/belirix.git # Replace with your repo url
cd belirix
Install the required Python packages:
Bash

pip install -r requirements.txt
Create a .env file in the project root directory and add your Replicate API key (Optional if running models locally via Ollama):
REPLICATE_API_KEY=YOUR_REPLICATE_API_KEY
You can obtain a Replicate API key by creating an account on the Replicate website. This is used for accessing the LLaVA models through Replicate if not running locally using Ollama.

Usage
Run the Streamlit application:
Bash

streamlit run app.py
Open your web browser and navigate to the URL displayed in the terminal (usually http://localhost:8501).

Upload an image using the file uploader.

Enter your question about the image in the chat input box and press Enter.

Belirix will process the image and stream the response from the LLaVA model.

Configuration
The config.py file contains several configuration options:

PAGE_TITLE: Sets the title of the web application.
OLLAMA_MODELS: A tuple containing the names of available LLaVA models.
SYSTEM_PROMPT: The system prompt given to the LLM, defining its role and capabilities.
Example config.py:

Python

import os
from dotenv import load_dotenv

load_dotenv()
replicate_api_key = os.getenv("REPLICATE_API_KEY") #Optional if running locally using Ollama

class Config:
    PAGE_TITLE = "Belirix Image Analyzer"
    OLLAMA_MODELS = ('llava:7b', 'llava:13b')
    SYSTEM_PROMPT = """You are a helpful chatbot that can analyze images. You can answer questions about the content of uploaded images."""
Project Structure
belirix/
├── app.py          # Main Streamlit application
├── config.py       # Configuration settings
├── helpers/
│   ├── image_helper.py # Image processing utilities
│   └── llm_helper.py   # LLM interaction utilities
├── requirements.txt  # Project dependencies
└── README.md       # This README file
Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details. 1    
1.
docs.rs
docs.rs


This is the entire README content as a single, copyable block of Markdown text. You can directly copy and paste this into your `README.md` file. Remember to replace `<your_username>` with your actual GitHub username.
