import speech_recognition as sr
import pygame
import time


def record_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio_data = recognizer.listen(source)
        print("Recording Complete.")
        with open(file_path, "wb") as audio_file:
            audio_file.write(audio_data.get_wav_data())

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
