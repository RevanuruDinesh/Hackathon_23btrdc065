# AI-Powered Virtual Assistant with Voice Recognition
This is an AI-powered virtual assistant built using Python, capable of performing a variety of tasks based on voice and text commands. The assistant integrates multiple libraries and APIs, allowing it to interact with users, retrieve data from the web, and control various system functions.

Features
Voice Recognition & Speech Output: The assistant listens to voice commands and responds with synthesized speech.
System Control: Control system features like volume, brightness, window management (minimize, maximize, switch), and more using voice commands.
Weather Updates: Get real-time weather information using the OpenWeatherMap API.
Time & Date: Fetch the current local time and date, and also world time for different locations.
Open Websites & Applications: The assistant can open websites (e.g., Google, YouTube) and local applications (e.g., Notepad, Calculator).
Google & Wikipedia Search: Perform searches on Google and get brief summaries from Wikipedia.
YouTube Search: Search YouTube for music, tutorials, or any other video content.
AI-Powered Responses: Use OpenAI's GPT-3.5 API to get AI-generated answers to questions or commands.
Screenshot & Screen Control: Take screenshots and manage screen brightness.
Multimedia Controls: Play or skip tracks in your music player, control volume, and perform various media actions.
Libraries Used
speech_recognition: For converting speech into text and capturing audio input.
pyttsx3: For converting text to speech (TTS).
wikipedia: To fetch information from Wikipedia.
openai: To interact with OpenAI's GPT-3.5 for AI-based responses.
pywhatkit: For web searches and YouTube video control.
pyautogui: To control the system's graphical interface (keyboard, mouse).
keyboard: For handling keyboard input and system commands.
screen_brightness_control: To adjust the screen brightness.
requests: For making HTTP requests (e.g., weather API calls).
Requirements
Python 3.x
Required Libraries (can be installed using pip):
speech_recognition
pyttsx3
openai
wikipedia
pywhatkit
pyautogui
keyboard
screen_brightness_control
requests
datetime
How to Use
Clone this repository to your local machine.
Install the required libraries using pip install -r requirements.txt.
Replace the openai.api_key with your own OpenAI API key.
Run the script and interact with the assistant by speaking commands.
Example Commands
"What's the weather in New York?"
"Open YouTube"
"Play some music"
"What's the time in London?"
"Take a screenshot"
"Search Wikipedia for Python programming"
Future Improvements
Add more personalized user features.
Integrate with smart home devices.
Add more APIs for additional functionalities like sending emails, reminders, etc.
