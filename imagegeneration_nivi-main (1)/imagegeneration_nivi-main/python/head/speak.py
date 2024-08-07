import os
import pygame


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
        
# import pyttsx3

# engine=pyttsx3.init()
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
    