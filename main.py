import pyttsx3
import speech_recognition as sr
import keyboard
import os
import imdb
import time
import pyautogui
import webbrowser
import subprocess as sp
from decouple import config
import wolframalpha
from decouple import config
from datetime import datetime
from conv import random_text
from random import choice
from selenium import webdriver
from online import find_my_ip,search_on_google,search_on_wikipedia,youtube,send_email,weather_forecast,get_news




import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found! Set the GOOGLE_API_KEY environment variable.")

# Configure Google AI Client
genai.configure(api_key=API_KEY)



import time

def generate_ai_essay():
    model = genai.GenerativeModel("gemini-2.0-flash")

    while True:  # Keep listening for new queries
        try:
            query = take_command()
            if query.lower() in ["exit", "quit", "stop"]:  # Exit condition
                print("Exiting...")
                speak("Goodbye!")
                break  

            if not query or query == "None":  
                continue  # If no input, continue listening

            response = model.generate_content(query)
            full_response = response.text

            # Summarizing response
            summary_prompt = f"Summarize this in 2-3 sentences: {full_response}"
            summary = model.generate_content(summary_prompt).text  

            print(summary)
            speak(summary)

            time.sleep(1)  # Pause before the next command

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, something went wrong.")
            time.sleep(2)  # Pause to prevent crashing













APP_ID = config("WOLFRAM_APP_ID")
client = wolframalpha.Client(APP_ID)

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
voice =engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

USER =config('USER')
HOSTNAME =config('BOT')












def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour>=6) and (hour < 12):
        speak(f"Good Morning {USER}")
    elif (hour >=12) and (hour <=16):
        speak(f"Good afternoon {USER}")
    elif(hour>=16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you? {USER}")

listening= False


def start_listening():
    global listening
    listening=True
    print("Started Listening")

def pause_listening():
    global listening
    listening=False
    print("Stopped Listening")

keyboard.add_hotkey('ctrl+alt+k',start_listening)
keyboard.add_hotkey('ctrl+alt+p',pause_listening)




def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected!")
            return "None"
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "None"
        except sr.RequestError:
            print("Speech Recognition service error")
            return "None"
        
       






if __name__ =='__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("Yes boss iam fine...., What about you")
                
            elif "i am fine" in query:
                speak("That's cool boss. Need any help")
            
            elif "schedule" in query:
                speak("Boss today you have a project presentation. and its about me .  so be prepared. and do well ")
            
            elif "do my best" in query:
                speak("That's cool.     you are really awsome boss ")
                
                
                
            elif "open ai" in query:
                speak("NOW its turned on to open ai ask anything you want")
                generate_ai_essay()
                
                
                
                
                
            
            
            elif "command prompt" in query:
                speak("Opening command prompt")
                sp.Popen("start cmd", shell=True)

            elif "chrome" in query:
                speak("Opening chrome")
                sp.Popen("start chrome",shell=True)

            elif "ip address" in query:
                ip_address= find_my_ip()
                speak(f"Your ip address is {ip_address}")
                print(f"Your IP Address is {ip_address}")

            elif "youtube" in query:
                speak("what do you want me to play on youtube sir?")
                video=take_command().lower()
                youtube(video)

            elif "google" in query:
                speak(f"what do you want me to search on google {USER}")
                query=take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want me to search on wikipedia sir?")
                search=take_command().lower()
                result=search_on_wikipedia(search)
                speak(f"Accrding to wikipedia,{result}")
                speak(f"Iam printing it on Terminal {USER}")
                print(result)


            elif "send email" in query:
                speak("on what email address do you want me to send sir?.please enter in the terminal")
                receiver_add=input("Email Address:")
                speak("What should be the subject sir?")
                subject=take_command().capitalize()
                speak("what is the message ?")
                message=take_command().capitalize()
                if send_email(receiver_add,subject,message):
                    speak("I have sent the email sir")
                    print("I have sent the email sir")
                else:
                    speak("something went wrong. please check the error log")
                    
                    
            elif "open facebook" in query:
                speak("opening facebook")
                driver= webdriver.Chrome()
                driver.get("http://www.facebook.com/")
                
            elif "open instagram" in query:
                speak("opening instagram")
                driver= webdriver.Chrome()
                driver.get("http://www.instagram.com/")
            
            elif "open whatsapp" in query:
                speak("opening whatsapp")
                driver= webdriver.Chrome()
                driver.get("http://www.whatsapp.com/")
                
            elif "college" in query:
                speak("opening Dr.Mgr university website")
                webbrowser.open("https://www.drmgrdu.ac.in/")
                
                
                

            elif "close facebook" in query:
                speak("closing facebook")
                driver.close()  
                
            elif "close instagram" in query:
                speak("closing instagram")
                driver.close()
            
            elif "close whatsapp" in query:
                speak("closing whatsapp")
                driver.close()     
                
  

                
                
            elif "increase the volume" in query:
                pyautogui.press("volumeup")
                speak("volume increased")
                
                
            elif "decrease the volume" in query:
                pyautogui.press("volumedown")
                speak("volume decreased")
                   
                
            elif "mute" in query:
                pyautogui.press("volumemute") 
                speak("volume muted")
                
                
            


            elif "weather" in query:
                ip_address=find_my_ip()
                speak("tell me the name of your city")
                city=take_command()
                speak(f"Getting weather report for the city{city}")
                weather ,temp, feels_like = weather_forecast(city)
                speak(f"The current temperature is {temp},but it feels like{feels_like}")
                speak(f"Also, the weather report talks about{weather}")
                speak(f"For your convenience, I am printing it on the screen sir.")
                print(f"Description:{weather}\nTemperature: {temp}\nFeels like:{feels_like} ")


            elif "imdb" in query:
                movies_db = imdb.IMDb()
                speak("please tell me the movie name: ")
                text=take_command()
                movies=movies_db.search_movie(text)
                speak("searching for" + text)
                speak("I found these")
                speak("wait a second sir i should read the article")
                for movie in movies:
                    title = movie["title"]
                    year=movie["year"]
                    speak(f"{title}-{year}")
                    info =movie.getID()
                    movie_info=movies_db.get_movie(info)
                    rating = movie_info.get('rating', 'N/A')
                    cast=movie_info["cast"]
                    actor=cast[0:5]
                    plot=movie_info.get('plot outline','plot summary not available')
                    speak(f"{title} was released in {year} has imdb rating of {rating}. The" 
                          f"plot summary of movie is {plot}")
                    print(f"{title} was released in {year} has imdb rating of {rating}. It has a cast of{actor}. The" 
                          f"plot summary of movie is {plot}")
                    
            
                    

            elif "calculate" in query:
                try:
                    ind = query.lower().split().index("calculate")
                    text = query.split()[ind + 1:]
                    result = client.query(" ".join(text))
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                    print("The answer is " + ans)
                except (StopIteration, IndexError):
                    speak("I couldn't find that. Please try again") 


            elif any(x in query for x in ["what is", "who is", "which is"]):
                try:
                    result = client.query(query)
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                except StopIteration:
                   speak("I couldn't find that. Please try again")

            elif "subscribe" in query:
                speak("Everyone who are watching this video, Please subscribe for more amazing content from adam w "
                      ". I will show you how to do this ")
                speak("Firstly go to youtube")
                webbrowser.open("https://www.youtube.com/")
                speak("click on the search bar")
                pyautogui.moveTo(806, 125, 1)
                pyautogui.click(x=806, y=125, clicks=1, interval=0, button='left')
                speak("adam w")
                pyautogui. typewrite("adam w", 0.1)
                time.sleep(1)
                speak("press enter")
                pyautogui.press('enter')
                pyautogui.moveTo(971, 314, 1)
                speak("Here you will see our channel")
                speak("Click here to subscribe our channel")
                pyautogui.click(x=1688, y=314, clicks=1, interval=0, button='left')
                speak("And also Don't forget to press the bell icon")
                pyautogui.moveTo(1750, 314, 1)
                pyautogui.click(x=1750, y=314, clicks=1, interval=0, button='left')
                speak("turn on all notifications")
                pyautogui.click(x=1750, y=320, clicks=1, interval=0, button='left')           

                    
                

            


            elif "stop" in query or "exit" in query or "quit" in query:
                speak("okay, stopping now. call me if iam needed!")
                print("Exiting....")
                break


import pyautogui
print(pyautogui.position())  # Shows the current mouse position



