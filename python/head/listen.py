import speech_recognition as sr
from time import sleep
sleep_mode=False
global query    
    
def take_command():

    global query

    # Clear the previous command first
    query = ""

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=2)

        print("You can speak now..")

        r.pause_threshold = 0.8

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
        except Exception as e:
            print("Listening error:", e)
            return ""

    try:
        print("Recognizing...")

        query = r.recognize_google(audio, language="en-us")

        # Convert to lowercase so command checking is consistent
        query = query.lower().strip()

        print("You said:", query)

    except Exception as e:
        print("Recognition error:", e)
        query = ""
        return ""

    return query