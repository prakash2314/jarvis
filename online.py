from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")  # Load API Key

if not EMAIL or not PASSWORD:   
    raise ValueError("EMAIL or PASSWORD not found. Check your .env file.")

def get_news():
    if not NEWS_API_KEY:
        return ["NEWS_API_KEY not found. Add it to .env file."]
    
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    if response.status_code != 200:
        return ["Failed to fetch news."]

    articles = response.json().get("articles", [])
    return [article["title"] for article in articles][:6]


import requests

def find_my_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    if response.status_code == 200:
        return response.json()["ip"]
    return "Unable to fetch IP."


import webbrowser

def search_on_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


import wikipedia

def search_on_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple results found: {e.options[:5]}"
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found for the given query."


import webbrowser

def youtube(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Opening YouTube search results for {query}"


import smtplib

def send_email(to_email, subject, body):
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    message = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message)
        server.quit()
        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {e}"


import requests

def weather_forecast(city):
    api_key = "your_api_key"  # Replace with your actual API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather_desc = data["weather"][0]["description"]
            temperature = main["temp"]
            humidity = main["humidity"]
            return f"Weather in {city}: {weather_desc}, Temperature: {temperature}°C, Humidity: {humidity}%"
        else:
            return "City not found."
    except Exception as e:
        return f"Error fetching weather data: {e}"
