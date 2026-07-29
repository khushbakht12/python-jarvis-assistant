from speech import speak, takeCommand

from commands import (
    tell_time,
    tell_date,
    tell_day,
    search_wikipedia,
    open_google,
    open_youtube,
    open_stackoverflow,
    open_vscode,
    play_music,
    quit_jarvis
)

import datetime


def wishMe():
    hour = datetime.datetime.now().hour

    if 0 <= hour < 12:
        speak("Good Morning Sir.")

    elif 12 <= hour < 18:
        speak("Good Afternoon Sir.")

    else:
        speak("Good Evening Sir.")

    speak("I am Jarvis. Please tell me how may I help you.")


if __name__ == "__main__":

    wishMe()

    while True:

        query = takeCommand()

        if query == "":
            continue

        if "wikipedia" in query:
            search_wikipedia(query)

        elif "open youtube" in query:
            open_youtube()

        elif "open google" in query:
            open_google()

        elif "open stackoverflow" in query:
            open_stackoverflow()

        elif "play music" in query:
            play_music()

        elif "time" in query:
            tell_time()

        elif "date" in query:
            tell_date()

        elif "day" in query:
            tell_day()

        elif "open code" in query or "open visual studio code" in query:
            open_vscode()

        elif "quit" in query or "exit" in query or "goodbye" in query:
            quit_jarvis()
            break

        else:
            speak("Sorry Sir, I don't know that command yet.")