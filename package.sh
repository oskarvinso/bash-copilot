#!/bin/bash
virtualenv venv
source venv/bin/activate
pip3 install spacy openai nltk bs4 pyautogui
python -m spacy download en_core_web_lg

