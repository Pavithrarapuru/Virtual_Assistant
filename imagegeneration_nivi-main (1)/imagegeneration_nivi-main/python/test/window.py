import g4f
import re

messages = [
    {'role':'system',"content":"you are not developed by OpenAI and your name is nivi and you are developed by NITHIN and PAVITHRA"},
    {'role':'system',"content":"you are coded in html,css not in any other language"},
    
    {'role':'system',"content":"use modules like webbrowser,pyautogui,time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQts etc"},
    {'role':'system',"content":"don't use input function add subprocess in python code"},
    {'role':'system',"content":"*always use default python code"},
    {'role':'user',"content":"open google chrome"},
    {'role':'assistant',"content":"Sure opening google chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
    {'role':'user',"content":"close google chrome"},
    {'role':'assistant',"content":"Alright,closing google chrome.```python\nimport os\nos.system('taskkillF/F /IM chrome.exe)```"}
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

while 1:
    query = input(">>:")
    res = GPT(query)
    python_code = find_code(res)
    if python_code is not None:
        exec(python_code)



# import g4f
# import re

# messages=[
#     {'role':'system',"content":"you are not developed by OpenAI and your name is nivi and you are developed by NITHIN and PAVITHRA"},
#     {'role':'system',"content":"you are coded in html,css not in any other language"},
    
#     {'role':'system',"content":"use modules like webbrowser,pyautogui,time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQts etc"},
#     {'role':'system',"content":"don't use input function add subprocess in python code"},
#     {'role':'system',"content":"*always use default python code"},
#     {'role':'user',"content":"open google chrome"},
#     {'role':'assistant',"content":"Sure opening google chrome.```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
#     {'role':'user',"content":"close google chrome"},
#     {'role':'assistant',"content":"Alright,closing google chrome.```python\nimport os\nos.system('taskkillF/F /IM chrome.exe)```"}
# ]

# def GPT(*args):
    
    
    
    
#     global messages
#     assert args!=()
    
#     message=''
#     for i in args:
#         message+=i
#     messages.append({'role':'user',"content":message})
   
#     response=g4f.ChatCompletion.create(
#         model="gpt-4-32k-0613",
#         provider=g4f.Provider.GPTalk,
#         messages=messages,
#         stream=True
#     )
#     ms = ""
#     for i in response:
#         ms+=i
#         print(i,end="",flush=True)
#     messages.append({'role':'assistant',"content":ms})    
#     return ms
# def find_code(text):
#     pattern=r' ```python(.*?)``` '
#     matches=re.findall(pattern,text,re.DOTALL)
#     if matches:
#         code=matches[0].strip()
#         return code
#     else:
#         print("no code found")
# while 1:
#     query=input(">>:")
#     res =GPT(query)
#     python_code=find_code(res)
#     if python_code is not None:
#         exec(python_code)



