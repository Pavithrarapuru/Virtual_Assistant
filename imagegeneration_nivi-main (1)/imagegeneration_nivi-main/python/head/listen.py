import speech_recognition as sr
from time import sleep
sleep_mode=False
global query    
    
def take_command():
 
    r=sr.Recognizer()
    with sr.Microphone() as source:
    
        # print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=5)
        print("you can speak now..")
        r.pause_threshold=0.8
        audio=r.listen(source, timeout=5)
        sleep(1)
    
    try:
        print("recognizing..")
        global query
        query=r.recognize_google(audio,language='en-us')
    except Exception as e:
        print(e)
        return ""
    return query
