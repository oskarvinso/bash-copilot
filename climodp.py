import requests, openai, sys, googleit, subprocess, time
from bs4 import BeautifulSoup
from os import popen as ba
from datetime import datetime
from models import GenericResponse
from mysecret import apikey
from machinelearning import aiselectfromlist, semanticsearch, summarizer
from lists import bashcommands
from gptautogui import get_window_titles, gpt4ask

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
    args=cleanargs(sys.argv)
    command=f"{args}"
    ba(f"echo 'pregunta {timestamp} {command}' >> ~/cbot.log")
    ia = executeinai(comand=command)
    if ia.success:
        ba(f"echo respuesta {timestamp} {ia.data} >> ~/cbot.log")
        return ia.data
    aguim = gpt4autoguimethod(comand=command)
    if aguim.success:
        ba(f"echo respuesta {timestamp} {aguim.data} >> ~/cbot.log")
        return aguim.data
    lai= localai(comand=command)
    if lai.success:
        ba(f"echo respuesta {timestamp} {lai.data} >> ~/cbot.log")
        return lai.data
    gs = googlesearch(comand=command)
    if gs.success:
        ba(f"echo respuesta {timestamp} {gs.data} >> ~/cbot.log")
        return gs.data
    return "parece que no hay internet"


def executeinai(comand) -> GenericResponse:
    openai.api_key = apikey
    try:
        iaresponse = openai.Completion.create(
        model="text-curie-001",
        prompt=comand,
        temperature=0,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
        worked=True
        ianswer= (iaresponse)
        possible= ianswer.choices[0]
        ans=possible["text"]
    except:
        ans="pague la factura de la ia"
        worked= False
    return GenericResponse(data=ans, success=worked)

def gpt4autoguimethod(comand):
    return GenericResponse(data=gpt4ask(comand), success=True)


def googlesearch(comand):
    urls = googleit.getlistoflinks(comand=comand)
    relevant = googleit.extractrelevantcontet(urls, comand)
    secndsearch = semanticsearch(relevant, comand)
    return GenericResponse(data=secndsearch , success=True)

def localai(comand):
    outp=aiselectfromlist(tabla=bashcommands, query=comand)
    return GenericResponse(data=outp, success=True)

print (getinstruction())