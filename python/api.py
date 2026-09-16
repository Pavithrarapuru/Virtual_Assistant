from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import speech_recognition as sr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "NIVI backend is running"}


@app.post("/listen")
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("NIVI is listening...")
        
        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )
        except sr.WaitTimeoutError:
            return {
                "success": False,
                "message": "I didn't hear anything."
            }

    try:
        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print("You:", text)

        return {
            "success": True,
            "text": text
        }

    except sr.UnknownValueError:
        return {
            "success": False,
            "message": "I couldn't understand what you said."
        }

    except sr.RequestError as e:
        return {
            "success": False,
            "message": f"Speech recognition service error: {e}"
        }