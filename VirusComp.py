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
    V1 = [0, 0, 0, 'stewie.gif',]
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

# Message options
message_choices = [
    "Sys32 ERROR: CRITICAL",
    "Is your fridge running ?? YOU BETTER CATCH IT",
    "Is this annoying yet?",
    "What if these messages never stop?",
    "You shouldn't have run this",
]

# Function to show notification with random message and delay
def show_random_notification():
    # Choose a random message from the list
    random_message = random.choice(message_choices)

    # Create the notification object with random message and title
    toast = Notification(
        app_id="Annoying Notifications Script",
        title="Friendly Reminder",
        msg=random_message,
        duration="short",
    )

    # Generate random delay between 5 and 25 seconds (inclusive)
    delay = random.uniform(5, 25)

    # Show the notification with delay
    time.sleep(delay)
    toast.show()

# Loop to show notification 10 times
for _ in range(10):
    show_random_notification()