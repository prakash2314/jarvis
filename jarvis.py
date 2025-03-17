import time
import threading
import keyboard
import numpy as np
import sounddevice as sd
import speech_recognition as sr
import os
import wolframalpha
import pyautogui
import subprocess
import webbrowser
import imdb
from main import sp, speak, webdriver, generate_ai_essay, send_email
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from conv import SCREEN_HEIGHT, SCREEN_WIDTH
from online import youtube, search_on_wikipedia, search_on_google, weather_forecast, find_my_ip
from jarvis_button import JarvisButton
from decouple import config

# Load configuration
USER = config('USER')
HOSTNAME = config('BOT')
APP_ID = config("WOLFRAM_APP_ID")
client = wolframalpha.Client(APP_ID)

class Jarvis(Widget):
    def __init__(self, **kwargs):
        super(Jarvis, self).__init__(**kwargs)
        self.volume = 0
        self.volume_history = [0] * 7
        self.volume_history_size = 140

        self.min_size = 0.2 * SCREEN_WIDTH
        self.max_size = 0.7 * SCREEN_WIDTH

        self.add_widget(Image(source='border.eps.png', size=(1980, 1080)))
        self.circle = JarvisButton(size=(284.0, 284.0), background_normal='')
        self.circle.bind(on_press=self.start_recording)
        self.add_widget(self.circle)

        self.gif = Image(source='static/jarvis.gif',
                         size=(self.min_size, self.min_size),
                         pos=(SCREEN_WIDTH / 2 - self.min_size / 2, SCREEN_HEIGHT / 2 - self.min_size / 2))
        self.add_widget(self.gif)

        time_layout = BoxLayout(orientation='vertical', pos=(150, 900))
        self.time_label = Label(text='', font_size=24, markup=True, font_name='static/mw.ttf')
        time_layout.add_widget(self.time_label)
        self.add_widget(time_layout)

        Clock.schedule_interval(self.update_time, 1)

        self.title = Label(text='[b][color=3333ff]ERROR BY NIGHT[/color][/b]', font_size=42, markup=True,
                           font_name='static/dusri.ttf', pos=(920, 900))
        self.add_widget(self.title)

        self.subtitles_input = TextInput(
            text="Hey VJ! I am Jarvis",
            font_size=24,
            readonly=True,
            background_color=(0, 0, 0, 0),
            foreground_color=(1, 1, 1, 1),
            size_hint_y=None,
            height=80,
            pos=(720, 100),
            width=1200,
            font_name='static/teesri.otf',
        )
        self.add_widget(self.subtitles_input)

        self.vrh = Label(text='', font_size=30, markup=True, font_name='static/mw.ttf', pos=(1500, 500))
        self.vlh = Label(text='', font_size=30, markup=True, font_name='static/mw.ttf', pos=(400, 500))
        self.add_widget(self.vrh)
        self.add_widget(self.vlh)

        keyboard.add_hotkey('`', self.start_recording)

    def start_recording(self, *args):
        print("Recording started")
        threading.Thread(target=self.run_speech_recognition, daemon=True).start()

    def run_speech_recognition(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r.listen(source)
                query = r.recognize_google(audio, language="en-in")
                Clock.schedule_once(lambda dt: setattr(self.subtitles_input, 'text', query))
                self.handle_jarvis_commands(query.lower())
            except sr.UnknownValueError:
                print("Speech not understood.")
            except sr.RequestError as e:
                print(f"Speech Recognition Error: {e}")

    def update_time(self, dt):
        current_time = time.strftime('TIME\n\t%H:%M:%S')
        self.time_label.text = f'[b][color=3333ff]{current_time}[/color][/b]'

    def handle_jarvis_commands(self, query):
        if "how are you" in query:
            speak("Yes boss, I am fine. What about you?")
        elif "open youtube" in query:
            speak("What do you want me to play on YouTube, sir?")
            video = self.run_speech_recognition()
            youtube(video)
        elif "google" in query:
            speak(f"What do you want me to search on Google, {USER}?")
            query = self.run_speech_recognition()
            search_on_google(query)
