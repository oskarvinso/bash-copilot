import openai
import sys
from os import popen as ba
from datetime import datetime
from mysecret import apikey


timestamp=datetime.now()


def cleanargs(args):
    outp=""
    i=False
    for wo in args:
        if i:
            outp= outp +' '+ wo
        i=True
    return outp.strip()


def getinstruction():
    args=joinall(sys.argv)
    args=args.replace(cleanargs(args), '')
    command=(f"write the code to {args} and add nice comments">
    ba(f"echo '{timestamp} {command}' >> ~/cbot>
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
