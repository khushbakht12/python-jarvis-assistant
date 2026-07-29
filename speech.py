import pyttsx3
import speech_recognition as sr

# Initialize the speech engine only once
engine = pyttsx3.init("sapi5")

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Male voice
engine.setProperty("rate", 170)            # Speaking speed
engine.setProperty("volume", 1.0)          # Volume (0.0 to 1.0)


def speak(text):
    """
    Converts text to speech.
    """
    print(f"Jarvis: {text}")
    engine.say(str(text))
    engine.runAndWait()


def takeCommand():
    """
    Listens to the microphone and returns the recognized text.
    Returns an empty string if speech is not recognized.
    """
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-IN")
        print(f"User said: {query}\n")
        return query.lower()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand.")
        speak("Sorry, I didn't understand.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        speak("Speech recognition service is unavailable.")
        return ""

    except Exception as e:
        print(e)
        speak("Something went wrong.")
        return ""