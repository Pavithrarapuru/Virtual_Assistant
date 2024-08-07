import g4f
import re
from head.speak import speak
from head.listen import take_command
from news import news
from time import sleep

latest_news=news()
messages = [
    
    {'role':'system',"content":"you are not developed by OpenAI and your name is nivi and you are developed by NITHIN and PAVITHRA"},
    {'role':'system',"content":"you are coded in html,css not in any other language"},
    {'role':'system',"content":f"todays latest news are{latest_news}"},    
    {'role':'system',"content":"use modules like webbrowser,pyautogui,time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQts etc"},
    {'role':'system',"content":"don't use input function add subprocess in python code"},
    {'role':'system',"content":"*always use default python code"},
    {'role':'system',"content":"when user say show me the image,use the following code to display the image : \n ```python\n from PIL import Image\n\nimage_path=r'C:\\Users\\NITHIN\\OneDrive\\Desktop\\python\\output\\0.jpeg'\nimage=Image.open(image_path)\nimage.show()\n```\nif you want to see another image,let me know."},
   
{
"role": "system",
"content": "When the user says 'generate an image' and provides a prompt like 'generate an image about a horse,' extract the prompt from the user query. Then, give this code to the user:\n```python\nfrom head.ucookie import u_cookie_value \nfrom os import system, listdir\n\ndef Generate_Images(prompt: str):\n system(f'python -m BingImageCreator --prompt \"{prompt}\" -U \" {u_cookie_value)\"')\nreturn listdir(\"output\")[-4:]\n\n# Example usage\nresult = Generate_Images('user_extracted_prompt')\nprint (result)\n``` While calling the function, replace 'user_extracted_prompt' with the actual prompt provided by the user to generate the desired image. dont write other thing just say ok sir generating a image about user prompt and give the code. also dont write other things like heres the code, you need assitant i am here dont write it. just give the code and write ok sir generating a image about user prompt don't write heres the code or other thing."},
    {'role':'user',"content":"open google chrome"},
    {'role':'assistant',"content":"Sure opening google chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {'role':'user',"content":"close google chrZome"},
    {'role':'assistant',"content":"Alright,closing google chrome.```python\nimport os\nos.system('taskkillF/F /IM msedge.exe)```"}
]

def GPT(*args):
    global messages
    assert args != ()
    
    message = ''
    for i in args:
        message += i
    messages.append({'role': 'user', "content": message})
   
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms += i
        print(i, end="", flush=True)
    messages.append({'role': 'assistant', "content": ms})    
    return ms

def find_code(text):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    if matches:
        code = matches[0].strip()
        return code
    else:
        print("no code found")
sleep_mode = False

while 1:
    def ai():
        query = take_command()
        res = GPT(query)
        python_code = find_code(res)
        if python_code is not None:
            res=res.replace(python_code,'')
            res=res.replace('python','')
            print("\n"+res)
            speak("done sir !")            
            exec(python_code)
        else:
            ai()
        speak(res)
    ai()