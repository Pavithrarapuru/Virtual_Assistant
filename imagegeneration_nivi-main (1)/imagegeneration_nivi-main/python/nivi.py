import os
import pygame
import speech_recognition as sr
from test import *
from time import sleep
import pyautogui
import pywhatkit
from datetime import datetime
from emailnivi import *
from mailbot import *
# from head.speak import speak
# from head.listen import take_command


def speak(text):
    
    # python_path = r'C:\users\nithin\anaconda3\python.exe'  # Replace with your actual Python path
    voice = "en-US-AriaNeural"
    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'
    
    os.system(command)
    pygame.mixer.init()
    try:
        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            clock = pygame.time.Clock()
            clock.tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        

sleep_mode=False
global query    
    
def take_command():
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
    
        # print("Adjusting for ambient noise...")
        r.adjust_for_ambient_noise(source, duration=5)
        if sleep_mode ==False:
            speak("tell me what to do now")
        print("you can speak now..")
        r.pause_threshold=0.8
        audio=r.listen(source, timeout=5)
    
    try:
        print("recognizing..")
        global query
        query=r.recognize_google(audio,language='en-us')
    except Exception as e:
        print(e)
        return ""
    return query


speak("hello sir, I am your virtual assistant nivi.")

global order
chatnumber=2
while True:
    take_command()
    
    if query=='':
        take_command()
    elif 'open' in query:
        app_name=query.replace('open','')
        speak("opening"+app_name)
        pyautogui.press('super') 
        pyautogui.sleep(1)
        pyautogui.typewrite(app_name)
        pyautogui.sleep(1)
        pyautogui.press("enter")
    elif 'switch' in query:
        pyautogui.hotkey('ctrl','tab')
    elif 'close tab' in query:
        pyautogui.hotkey('ctrl','w')
        
    elif 'close' in query:
        pyautogui.hotkey('alt','f4')
        speak("done sir! ")
    elif 'play' in query:
        song_name=query.replace('play','')
        speak("sure sir,playing" +song_name+ "on youtube")
        pywhatkit.playonyt(song_name)
    elif 'time' in query:      
        current_time = datetime.now().strftime('%I:%M %p')
        speak('current time is '+current_time)
    elif 'sleep' in query:
        speak("ok sir iam going to sleep")
        sleep_mode=True
    
    
    elif 'send an email' in query or 'write an email' in query :
        
        speak("sure sir,tell me the mail id of the recipient below ")
        reciever=input("enter his or her mail id :")
        speak("what should be the subject of the email")
        sleep_mode=True
        subject=take_command()
        print(subject)
        speak("what should be the content")
        print("describe the purpose of your email,so that i can make one for you")
        email_prompt=take_command()
        sleep(10)
        sleep_mode=False
        sleep(2)
        content=auto_mail("write an email for " + email_prompt)
        sleep(1)
        send_mail(reciever,subject,content)
        speak("done sir!,email has been sent") 
        print("\n")
        
        
    else:
        
        def retriveData():
            sendQuery(take_command())
            sleep(15)
            print('Retriving Chat...')
            sleep(1)
            global p
            global chatnumber
            p = driver.find_element(By.XPATH, f'/html/body/div/div/div/div[2]/div[1]/div/div/div[{chatnumber}]/div/div[2]/div/div/div/div/div/p')
            chatnumber+=2
            print("\nNIVI: " + p.text) 
            nivi=p.text
            return(p.text)
        retriveData()
        speak(p.text)

        sleep(5)
    while sleep_mode:
        query=take_command().lower()
        if 'wake up' in query:
            speak('iam awake now')
            sleep_mode=False