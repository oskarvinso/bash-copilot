import openai
import sys
from os import popen as ba
from datetime import datetime
from mysecret import apikey

def joinall(words:list):
    output = ''
    for word in words:
        if word != ba('pwd').read():
            output = output + " " + str(word)
    return output.replace("climod.py", "")
timestamp=datetime.now()

def getinstruction():
    args=joinall( sys.argv)
    args=args.replace('/data/data/com.termux/files/home/chatgpt/services/', '')
    command=f'write a bash script that {args} on ubuntu'
    ba(f"echo '{timestamp} {command}' >> ~/cbot.log")
    return(executeinai(command))
def executeinai(comand):
    openai.api_key = apikey
    iaresponse = openai.Completion.create(
    model="text-davinci-003",
    prompt=comand,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0)
    ianswer= (iaresponse)
    possible= ianswer.choices[0]
    ans=possible["text"]
    print(ans)
    ba(f"echo {timestamp}{ans} >> ~/cbot.log")
    return ans

getinstruction()
