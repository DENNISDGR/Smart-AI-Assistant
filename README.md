# Smart-AI-Assistant

Welcome to the Smart-AI-Assistant repository! This project is a Python-based voice assistant designed to help with various tasks using speech recognition and OpenAI's GPT-4. 

## Features
- **Voice Recognition**: Uses the `speech_recognition` library to understand and process spoken commands.
- **Text-to-Speech**: Utilizes the `pygame` library to provide audible responses.
- **AI Integration**: Incorporates OpenAI's GPT-4 for intelligent responses and interactions.

## How It Works
1. **Voice Input**: The assistant uses the microphone to capture your voice.
2. **Speech Recognition**: The captured audio is processed to convert speech into text using speech_recognition.
3. **AI Response**: The text is sent to OpenAI's GPT-4 to generate a context-aware response.
4. **Text-to-Speech**: The response is then converted back into speech using pygame and played back to the user.

## Try it yourself
### Installation

To get started, clone the repository and install the necessary dependencies using `requirements.txt`:

```sh
git clone https://github.com/DENNISDGR/Smart-AI-Assistant.git
cd Smart-AI-Assistant
pip install -r requirements.txt
```
Get an API key from [OpenAI](https://platform.openai.com/api-keys) and place it here:

```py
os.environ['OPENAI_API_KEY'] = 'your_api_key'
```

### Usage

To run the assistant, simply execute the main Python script:

```sh
python app.py
```

The assistant will start listening for your commands. Speak clearly into your microphone and wait for the assistant to process and respond to your query.

## Stay updated

This is only the beginning. For more information, detailed code explanations, updates, and other interesting projects, visit [my site](https://dennisdgr.ddns.net).
