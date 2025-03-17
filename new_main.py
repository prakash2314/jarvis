from dotenv import load_dotenv
load_dotenv()

from kivy.app import App
from kivy.clock import Clock
from jarvis import Jarvis

class MyKivyApp(App):
    def build(self):
        jarvis = Jarvis()
        Clock.schedule_interval(jarvis.circle.rotate_button, 1/60)
        return jarvis

if __name__ == "__main__":
    MyKivyApp().run()


from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

EMAIL = os.getenv("vjprakash2314@gmail.com")
PASSWORD = os.getenv("Thalapathy")

if not EMAIL or not PASSWORD:
    raise ValueError("EMAIL or PASSWORD not found in .env")
