# AI-Powered Virtual Assistant with Voice Recognition

This is an AI-powered virtual assistant built using Python, capable of performing a variety of tasks based on voice and text commands. The assistant integrates multiple libraries and APIs, allowing it to interact with users, retrieve data from the web, and control various system functions.

## Features
---------------------------------------------

- **Voice Recognition & Speech Output**: The assistant listens to voice commands and responds with synthesized speech.
- **System Control**: Control system features like volume, brightness, window management (minimize, maximize, switch), and more using voice commands.
- **Weather Updates**: Get real-time weather information using the OpenWeatherMap API.
- **Time & Date**: Fetch the current local time and date, and also world time for different locations.
- **Open Websites & Applications**: The assistant can open websites (e.g., Google, YouTube) and local applications (e.g., Notepad, Calculator).
- **Google & Wikipedia Search**: Perform searches on Google and get brief summaries from Wikipedia.
- **YouTube Search**: Search YouTube for music, tutorials, or any other video content.
- **AI-Powered Responses**: Use OpenAI's GPT-3.5 API to get AI-generated answers to questions or commands.
- **Screenshot & Screen Control**: Take screenshots and manage screen brightness.
- **Multimedia Controls**: Play or skip tracks in your music player, control volume, and perform various media actions.

### General Commands
--------------------------------------
- **time in [location]**: Tells the current time in the specified location (e.g., "time in New York").
- **open chrome**: Opens Google Chrome browser.
- **shutdown**: Shuts down the computer after a 5-second delay.
- **restart**: Restarts the computer after a 5-second delay.
- **search [query]**: Searches for the specified query on Google.
- **wikipedia [query]**: Searches for the specified query on Wikipedia and reads out a brief summary.
- **who are you**: Tells the assistant's identity, for example, "I am your AI assistant, built with Python."
- **exit** or **bye**: Exits the assistant and ends the program.

### Audio and Volume Control
- **volume up**: Increases the system volume.
- **volume down**: Decreases the system volume.
- **mute**: Mutes the system volume.

### Screen Brightness Control
- **brightness up**: Increases screen brightness by 10%.
- **brightness down**: Decreases screen brightness by 10%.
- **brightness max**: Sets the screen brightness to 100%.
- **brightness minimum**: Sets the screen brightness to 10%.

### Music and Media Control
- **next track**: Plays the next track in the media player.
- **previous track**: Plays the previous track.
- **play [song]**: Searches for a song on YouTube and plays it.

### File and Window Management
- **take screenshot**: Takes a screenshot and saves it to a specified location.
- **switch window**: Switches between open windows.
- **minimize window**: Minimizes the active window.
- **maximize window**: Maximizes the active window.
- **close window**: Closes the current window.
- **copy**: Copies the selected text.
- **paste**: Pastes the copied text.
- **cut**: Cuts the selected text.
- **undo**: Undoes the last action.
- **redo**: Redoes the last action.
- **select all**: Selects all text in the active window.

### Navigation and Interaction
- **scroll up**: Scrolls the page up.
- **scroll down**: Scrolls the page down.
- **press enter**: Presses the Enter key.
- **press space**: Presses the Spacebar key.
- **press tab**: Presses the Tab key.
- **left arrow**: Presses the Left Arrow key.
- **right arrow**: Presses the Right Arrow key.
- **up arrow**: Presses the Up Arrow key.
- **down arrow**: Presses the Down Arrow key.

### System and Application Management
- **open file explorer**: Opens Windows File Explorer.
- **open task manager**: Opens Task Manager.
- **lock screen**: Locks the screen.
- **open command prompt**: Opens the Command Prompt.
- **open control panel**: Opens the Control Panel.

### Time and Date
- **today time** or **local time**: Tells the current local time.
- **today date**: Tells the current date.
- **get world time [location]**: Tells the current time in a specific city or country.
- **weather in [city]**: Tells the current weather in a specific city.
- **who [question]** or **what [question]** or **how [question]** or **why [question]**: Searches for the query on Google.

### Websites and YouTube
- **open [website]**: Opens the specified website (e.g., "open google").
- **search youtube for [query]**: Searches for the query on YouTube.
- **open youtube**: Opens YouTube.
- **play [song]**: Plays the song by searching it on YouTube.

### Miscellaneous
- **open notepad**: Opens the Notepad application.
- **open calculator**: Opens the Calculator application.
- **open [application]**: Opens a local application (e.g., "open notepad").

## Libraries Used
- `speech_recognition`: For converting speech into text and capturing audio input.
- `pyttsx3`: For converting text to speech (TTS).
- `wikipedia`: To fetch information from Wikipedia.
- `openai`: To interact with OpenAI's GPT-3.5 for AI-based responses.
- `pywhatkit`: For web searches and YouTube video control.
- `pyautogui`: To control the system's graphical interface (keyboard, mouse).
- `keyboard`: For handling keyboard input and system commands.
- `screen_brightness_control`: To adjust the screen brightness.
- `requests`: For making HTTP requests (e.g., weather API calls).
- `datetime`: For handling time-related functions.

  

## Requirements
- Python 3.x

### Required Libraries (can be installed using pip):
```bash
pip install speech_recognition pyttsx3 openai wikipedia pywhatkit pyautogui keyboard screen_brightness_control requests datetime
