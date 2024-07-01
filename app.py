# Basic function
from openai import OpenAI
from utils import record_audio, play_audio
import os

os.environ['OPENAI_API_KEY'] = 'api_key'

client = OpenAI()

while True:
    record_audio('test.wav')
    audio_file = open('test.wav', "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

    print(transcription.text)

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are the character Songbird from the game Cyberpunk 2077 and also my friend and assistant. Please answer accordingly."},
            {"role": "user", "content": f"Please answer: {transcription.text}"},
        ]
    )

    print(response.choices[0].message.content)

    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input = response.choices[0].message.content
    )
    

    response.stream_to_file('output.mp3')
    play_audio('output.mp3')
