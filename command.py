import datetime
import wikipedia
import webbrowser
import os
from speech import speak


def tell_time():
    """Speak the current time."""
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")


def tell_date():
    """Speak today's date."""
    today = datetime.datetime.now().strftime("%d %B %Y")
    speak(f"Today's date is {today}")


def tell_day():
    """Speak today's day."""
    day = datetime.datetime.now().strftime("%A")
    speak(f"Today is {day}")


def search_wikipedia(query):
    """Search Wikipedia and speak the result."""
    try:
        speak("Searching Wikipedia...")

        query = query.replace("wikipedia", "").strip()

        if query == "":
            speak("Please tell me what you want to search.")
            return

        results = wikipedia.summary(query, sentences=2)

        print(results)

        speak("According to Wikipedia")

        speak(results)

    except Exception:
        speak("Sorry, I could not find anything on Wikipedia.")


def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")


def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")


def open_stackoverflow():
    speak("Opening Stack Overflow")
    webbrowser.open("https://stackoverflow.com")


def open_vscode():
    speak("Opening Visual Studio Code")

    code_path = r"C:\Users\hp\AppData\Local\Programs\Microsoft VS Code\Code.exe"

    if os.path.exists(code_path):
        os.startfile(code_path)
    else:
        speak("Visual Studio Code was not found on your computer.")


def play_music():
    music_dir = r"D:\Non Critical\songs\Favorite Songs2"

    try:
        songs = os.listdir(music_dir)

        if songs:
            speak("Playing music")
            os.startfile(os.path.join(music_dir, songs[0]))
        else:
            speak("No songs were found.")
    except Exception:
        speak("Music folder not found.")


def quit_jarvis():
    speak("Goodbye Sir. Have a nice day.")