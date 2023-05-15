# -*- coding: utf-8 -*-
import subprocess
import pyperclip, pyautogui, time ,os, screeninfo

os.environ['PYTHONIOENCODING'] = 'utf-8'
curpath = os.getcwd()

class AutoguiGPT4:
    def __init__(self, **kwargs):
        self.quest = kwargs.get('quest', '')
        self.response = kwargs.get('response', '')

def gpt4ask(prompt):
    write_on_chatgpt(prompt)
    time.sleep(10)
    outp = get_chatgpt_response()
    os.system("rm buffer")
    return outp

def write_on_chatgpt(message):
    url = "https://chat.openai.com/"
    #url = "https://chatbot.goldhealthgroup.net"
    browser_cmd = "firefox"
    subprocess.Popen([browser_cmd, url])
    time.sleep(3)
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    
def get_chatgpt_response():
    while not finished():
        getposofcopy()
        saveclipboard()
    response = open("buffer", 'r').read()
    return response


def getposofcopy():
    # Encuentra la posición del botón en la pantalla
    m = screeninfo.get_monitors()[0]
    total_width = m.width
    total_height = m.height
    center_x = total_width // 2
    promth = 15*(total_height // 16) - 35 
    pyautogui.click(center_x, promth)
    pyautogui.keyDown('shift')
    for times in range(0,4,1): 
        pyautogui.press("tab")
    pyautogui.keyUp('shift')
    pyautogui.press("enter")

def finished():
    try:
        with open("buffer", 'r') as file:
            content = file.read()
            if content != '':
                return True
            else:
                return False
    except FileNotFoundError:
        return False

def saveclipboard():
    subprocess.Popen('xed')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('ctrl','s')
    time.sleep(0.5)
    pyautogui.typewrite("buffer")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.hotkey('alt','F4')



def get_window_titles():
    try:
        # Obtener la salida del comando 'xprop'
        output = os.popen('xprop -root _NET_CLIENT_LIST').read().strip()
        
        # Extraer la lista de identificadores de ventana
        window_ids = output.split(', ')
        
        window_titles = []
        
        for window_id in window_ids:
            # Obtener la salida del comando 'xprop' para cada identificador de ventana
            output = os.popen('xprop -id {} _NET_WM_NAME'.format(window_id)).read().strip()
            
            # Extraer el título de la ventana de la salida
            title = output.split('=')[-1].strip().strip('"')
            
            if title:
                window_titles.append(title)
        
        return window_titles
    
    except Exception as e:
        print("Error al obtener los títulos de las ventanas:", str(e))
        return []
    