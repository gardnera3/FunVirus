import tkinter as tk
import time
from winotify import Notification, audio
#This method compiles the results from the UI and combines the presets to become the customized export


#This array is for choosing the virus types
#-- on (1) or off (0)
#column1: toggle option1 (running sprite)
#column2: toggle option2 (sound)
#column3: toggle option3 (display)
#column4: toggle option4 (popups)
#column4: toggle option5 (bluescreen of death)
toggle = [0, 0, 0, 0, 0,]

#This V1 array customizes option 1 (running sprite)
#column1: speed ranging from 0-2
#column2: frequency (0-2)
#column 3: size (0-1000) pixels
#column 4: image path
if toggle[0] == 1:
    V1 = [0, 0, 0, '/path/to/image.png',]
    import tkinter as tk

    # select a color as the transparent color
    TRNAS_COLOR = '#abcdef'

    root = tk.Tk()
    root.overrideredirect(1)
    root.attributes('-transparentcolor', TRNAS_COLOR)

    image = tk.PhotoImage(file= V1[3])
    tk.Label(root, image=image, bg=TRNAS_COLOR).pack()

    # support dragging window

    def start_drag(event):
        global dx, dy
        dx, dy = event.x, event.y

    def drag_window(event):
        root.geometry(f'+{event.x_root-dx}+{event.y_root-dy}')

    root.bind('<Button-1>', start_drag)
    root.bind('<B1-Motion>', drag_window)

    root.mainloop()

if toggle[1] == 1:
    V2 = [0, 0, 0, '/path/to/image.png',]