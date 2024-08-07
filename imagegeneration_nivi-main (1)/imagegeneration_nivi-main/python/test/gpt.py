# import g4f

# def GPT(message):
#     try:
#         response=g4f.ChatCompletion.create(
#             model="gpt-4-32k-0613",
#             provider=g4f.Provider.GPTalk,
#             messages=[{"role":"user","content":message}],
#             stream=True
#         )
#         ms=""
#         for i in response:
#             ms+=i
#             print(i,end="",flush=True)
#         return ms
#     except Exception as e:
#         print("i cant get you,try again bcz :",e)
        
import g4f

messages=[
    {'role':'system',"content":"you are not developed by microsoft and your name is nivi and you are developed by NITHIN and PAVITHRA"},
    {'role':'system',"content":"you are coded in html,css not in any other language"}
]

def GPT(*args):
    
    global messages
    assert args!=()
    
    message=''
    for i in args:
        message+=i
    messages.append({'role':'user',"content":message})
   
    response=g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.Bing,
        messages=messages,
        stream=True
    )
    ms = ""
    for i in response:
        ms+=i
        print(i,end="",flush=True)
    messages.append({'role':'assistant',"content":ms})    
    return ms


GPT('who are you')



