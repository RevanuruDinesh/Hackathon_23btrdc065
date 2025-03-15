
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import time
import os
import re
import requests
import openai
import wikipedia
import pywhatkit
import pyautogui
import keyboard
import screen_brightness_control as sbc
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()
openai.api_key = "hear your api_key" 

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 150)  

def speak(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture voice command and convert to text"""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Please try again.")
            return None
        except sr.RequestError:
            speak("There was an issue with the speech recognition service.")
            return None
        except sr.WaitTimeoutError:
            speak("You didn't say anything.")
            return None

def get_local_time():
    """Get current system time"""
    now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The local time is {now}")

def get_date():
    """Get current date"""
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")
def open_calculator():
    os.system("calc.exe")

def get_world_time(location):
    """Get the current time for a specific city or country using TimeAPI.io"""
    try:
        url = f"https://www.timeapi.io/api/Time/current/zone?timeZone={location.replace(' ', '_')}"
        response = requests.get(url)
        data = response.json()

        if 'dateTime' in data:
            time = data['dateTime'].split('T')[1][:5] 
            speak(f"The current time in {location} is {time}")
        else:
            speak("Sorry, I couldn't fetch the time for that location.")
    except Exception as e:
        print("Error:", e)
        speak("There was an error fetching the time.")

def open_website(site):
    """Open a website"""
    webbrowser.open(site)
    speak(f"Opening {site}")

def open_application(app):
    """Open a local application"""
    try:
        os.system(f"start {app}")
        speak(f"Opening {app}")
    except Exception:
        speak(f"Sorry, I couldn't open {app}")

def get_weather(city="New York"):
    """Get weather information using OpenWeatherMap API"""
    api_key = "379b179b481b31afafb2788742d07379" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response["cod"] == 200:
            temp = response["main"]["temp"]
            desc = response["weather"][0]["description"]
            speak(f"The weather in {city} is {desc} with a temperature of {temp} degrees Celsius.")
        else:
            speak("Sorry, I couldn't fetch the weather information.")
    except Exception:
        speak("Network error while fetching weather details.")

def ask_openai(question):
    """Get an AI-powered response using OpenAI's ChatGPT API"""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        speak(answer)
        return answer
    except Exception:
        speak("Sorry, I couldn't get an AI response.")
        return None

def search_wikipedia(query):
    """Get a brief summary from Wikipedia"""
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
        return summary
    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results, please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("I couldn't find anything on Wikipedia.")
def search_youtube(query):
    url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    webbrowser.open(url)
    speak(f"Searching YouTube for {query}")


def process_command(command):
    """Process the given command and perform the corresponding action"""
    if "time in" in command:
        location = command.replace("time in", "").strip()
        get_world_time(location)

    elif "open chrome" in command:
            speak("Opening Chrome")
            os.system("start chrome")
    elif "shutdown" in command:
            speak("Shutting down your computer")
            os.system("shutdown /s /t 5")
    elif "restart" in command:
            speak("Restarting your computer")
            os.system("shutdown /r /t 5")
    elif "search" in command:
            query = command.replace("search", "").strip()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Searching {query} on Google")
    elif "wikipedia" in command:
            query = command.replace("wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=2)
            speak(result)

       
    elif "volume up" in command:
            pyautogui.press("volumeup", presses=5)
            speak("Increasing volume")
    elif "volume down" in command:
            pyautogui.press("volumedown", presses=5)
            speak("Decreasing volume")
    elif "mute" in command:
            pyautogui.press("volumemute")
            speak("Muting volume")
    elif "brightness up" in command:
            current_brightness = sbc.get_brightness(display=0)[0]  
            new_brightness = min(current_brightness + 10, 100)
            sbc.set_brightness(new_brightness, display=0)
            speak(f"Increasing brightness to {new_brightness}%")

    elif "brightness down" in command:
            current_brightness = sbc.get_brightness(display=0)[0] 
            new_brightness = max(current_brightness - 10, 0)
            sbc.set_brightness(new_brightness, display=0)
            speak(f"Decreasing brightness to {new_brightness}%")

    elif "brightness max" in command:
            sbc.set_brightness(100, display=0)
            speak("Brightness set to maximum")

    elif "brightness minium" in command:
            sbc.set_brightness(10, display=0)
            speak("Brightness set to minimum")


    elif "next track" in command:
            pyautogui.press("nexttrack")
            speak("Playing next track")
    elif "previous track" in command:
            pyautogui.press("prevtrack")
            speak("Playing previous track")

       
    elif "take screenshot" in command:
        screenshot = pyautogui.screenshot()
        screenshot.save(r"C:\Users\Windows\OneDrive\Pictures/screenshot.png")

        speak("Screenshot saved successfully.")

    elif "switch window" in command:
            keyboard.press_and_release("alt+tab")
            speak("Switching window")
    elif "minimize window" in command:
            keyboard.press_and_release("win+down")
            speak("Minimizing window")
    elif "maximize window" in command:
            keyboard.press_and_release("win+up")
            speak("Maximizing window")
    elif "close window" in command:
            keyboard.press_and_release("alt+f4")
            speak("Closing window")



    elif "copy" in command:
            keyboard.press_and_release("ctrl+c")
            speak("Copied text")
    elif "paste" in command:
            keyboard.press_and_release("ctrl+v")
            speak("Pasting text")
    elif "cut" in command:
            keyboard.press_and_release("ctrl+x")
            speak("Cutting text")
    elif "undo" in command:
            keyboard.press_and_release("ctrl+z")
            speak("Undoing last action")
    elif "redo" in command:
            keyboard.press_and_release("ctrl+y")
            speak("Redoing last action")
    elif "select all" in command:
            keyboard.press_and_release("ctrl+a")
            speak("Selecting all text")

    elif "scroll up" in command:
            pyautogui.scroll(300)
            speak("Scrolling up")
    elif "scroll down" in command:
            pyautogui.scroll(-300)
            speak("Scrolling down")
    elif "press enter" in command:
            keyboard.press_and_release("enter")
            speak("Pressed Enter")
    elif "press space" in command:
            keyboard.press_and_release("space")
            speak("Pressed Space")
    elif "press tab" in command:
            keyboard.press_and_release("tab")
            speak("Pressed Tab")
    elif "left arrow" in command:
            keyboard.press_and_release("left")
            speak("Pressed Left Arrow")
    elif "right arrow" in command:
            keyboard.press_and_release("right")
            speak("Pressed Right Arrow")
    elif "up arrow" in command:
            keyboard.press_and_release("up")
            speak("Pressed Up Arrow")
    elif "down arrow" in command:
            keyboard.press_and_release("down")
            speak("Pressed Down Arrow")

      
    elif "open file explorer" in command:
            keyboard.press_and_release("win+e")
            speak("Opening File Explorer")
    elif "open task manager" in command:
            keyboard.press_and_release("ctrl+shift+esc")
            speak("Opening Task Manager")

    elif "lock screen" in command:
            speak("Locking screen")
            os.system("rundll32.exe user32.dll,LockWorkStation")
    elif "open command prompt" in command:
            speak("Opening Command Prompt")
            os.system("cmd")

    elif "open control panel" in command:
            speak("Opening Control Panel")
            os.system("control")


    elif "today time" in command or "local time" in command:
        get_local_time()
    elif "today date" in command:
        get_date()
    elif "open google" in command:
        open_website("https://www.google.com")
    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        search_youtube(query)


    elif "open youtube" in command:
        open_website("https://www.youtube.com")
    elif "open notepad" in command:
        open_application("notepad")
    elif "open calculator" in command:
        open_calculator()

    elif "weather in" in command:
        city = command.replace("weather in", "").strip()
        get_weather(city)
    elif "who are you" in command:
        speak("I am your AI assistant, built with Python to help with various tasks.")
    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a great day.")
        exit()
    elif "who" in command or "what" in command or "how" in command or "why" in command:
        query = command.replace(" ", "+")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching Google for {command}")
    elif "search for" in command:
        query = command.split("search for", 1)[1].strip()
        speak(f"Searching Google for {query}.")
        webbrowser.open("https://www.google.com/search?q=" + query.replace(" ", "+"))
    elif "play" in command:
        query = command.replace("play", "").strip()
        search_youtube(query)

    else:
        speak("I did not understand that command. Searching Google for you.")
        webbrowser.open("https://www.google.com/search?q=" + command.replace(" ", "+"))


if __name__ == "__main__":
    speak("Hello! How can I assist you today?")
    while True:
        command = listen()
        if command:
            process_command(command)


