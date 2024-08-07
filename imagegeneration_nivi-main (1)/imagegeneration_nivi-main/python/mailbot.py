import g4f

def auto_mail(message):
    try:
        response=g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",
            provider=g4f.Provider.GPTalk,
            messages=[{"role":"user","content":message}],
            stream=True
        )
        ms=""
        for i in response:
            ms+=i
            print(i,end="",flush=True)
        return ms
    except Exception as e:
        print("i cant get you,try again bcz :",e)

