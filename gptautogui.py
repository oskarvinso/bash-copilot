import pyautogui
import time

class AutoguiGPT4:
    def __init__(self, **kwargs):
        self.quest = kwargs.get('quest', '')
        self.response = kwargs.get('response', '')

def gpt4ask(prompt):
    write_on_chatgpt(prompt)
    time.sleep(10)
    return get_chatgpt_response()

def write_on_chatgpt(message):
    # Obtener la posición del cursor donde queremos escribir
    #x, y = pyautogui.locateCenterOnScreen('chatgpt_cursor.png')
    # Hacer clic en la posición del cursor para enfocar el campo de entrada
    #pyautogui.click(x, y)
    # Escribir el mensaje en el campo de entrada
    pyautogui.typewrite(message)
    pyautogui.press('enter')
    # Esperar un momento para que el mensaje sea enviado
    time.sleep(1)
    
def get_chatgpt_response():
    # Esperar a que aparezca la respuesta de ChatGPT
    time.sleep(5)
    
    # Obtener la posición del cursor donde aparece la respuesta
    #x, y = pyautogui.locateCenterOnScreen('chatgpt_response.png')
    
    # Hacer clic en la posición del cursor para copiar la respuesta
    #pyautogui.click(x, y, button='right')
    pyautogui.press('down')
    pyautogui.press('enter')
    
    # Esperar un momento para que se copie la respuesta
    time.sleep(1)
    
    # Obtener la respuesta del portapapeles y devolverla
    response = pyautogui.hotkey('ctrl', 'v')
    return response

