import tkinter as tk
from PIL import Image, ImageTk  # Requires the Pillow library
import time
import rotatescreen
import random
from winotify import Notification, audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL


### Virus Rotate Screen Functionality ###

screen = rotatescreen.get_primary_display()
for i in range(3):
    # Rotate Left
    time.sleep(2)
    screen.set_portrait_flipped()

    # Flip Upside Down
    time.sleep(2)
    screen.set_landscape_flipped()

    # Rotate Right
    time.sleep(2)
    screen.set_portrait

    # Rotate Right
    # Program stays rotated for x amount of time slept
    time.sleep(2)
    screen.set_landscape()