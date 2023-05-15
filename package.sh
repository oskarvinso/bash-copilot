#!/bin/bash
virtualenv venv
source venv/bin/activate
sudo apt-get install python3-tk python3-dev -y
pip3 install pyperclip spacy openai nltk bs4 pyautogui screeninfo
sudo apt-get install scrot -y
python -m spacy download en_core_web_lg

