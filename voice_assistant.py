import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser


# -----------------------------
# Text-to-Speech Setup
# -----------------------------
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    """Speak the given text."""
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Voice Input
# -----------------------------
def listen():
    """Listen to the user's voice and convert it to text."""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            print("Recognizing...")

            command = recognizer.recognize_google(audio)

            print("You:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I didn't understand. Please repeat.")
            return ""

        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the speech service.")
            return ""


# -----------------------------
# Tell Time
# -----------------------------
def tell_time():

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    speak("The current time is " + current_time)


# -----------------------------
# Tell Date
# -----------------------------
def tell_date():

    current_date = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    speak("Today's date is " + current_date)


# -----------------------------
# Web Search
# -----------------------------
def web_search(query):

    query = query.replace("search for", "")
    query = query.replace("search", "")
    query = query.strip()

    if query:

        speak("Searching for " + query)

        url = "https://www.google.com/search?q=" + query.replace(" ", "+")
        webbrowser.open(url)

    else:

        speak("What would you like me to search for?")


# -----------------------------
# Process Commands
# -----------------------------
def process_command(command):

    if not command:
        return True

    # Hello / Greetings
    if "hello" in command or "hi" in command:

        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:

        tell_time()

    # Date
    elif "date" in command or "today" in command:

        tell_date()

    # Search
    elif "search" in command:

        web_search(command)

    # Open Google
    elif "open google" in command:

        speak("Opening Google.")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command:

        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")

    # Exit
    elif (
        "exit" in command
        or "quit" in command
        or "stop" in command
        or "goodbye" in command
    ):

        speak("Goodbye! Have a nice day.")
        return False

    # Unknown command
    else:

        speak("I don't know how to do that yet. Please try another command.")

    return True


# -----------------------------
# Main Program
# -----------------------------
def main():

    speak("Voice assistant started.")
    speak("How can I help you?")

    running = True

    while running:

        command = listen()

        running = process_command(command)


# -----------------------------
# Start Assistant
# -----------------------------
if __name__ == "__main__":
    main()