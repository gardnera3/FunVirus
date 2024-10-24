import tkinter as tk
from PIL import Image, ImageTk  # Requires the Pillow library
import time
import rotatescreen
import random
from winotify import Notification, audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.api.audioclient import ISimpleAudioVolume
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
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


# Load the GIF and split it into frames
V1 = [0, 0, 0, 'stewie.gif']  # Change this to your GIF file

# Select a color as the transparent color
TRANSPARENT_COLOR = '#abcdef'

# Initialize the root window
root = tk.Tk()
root.overrideredirect(1)  # Removes the window border
root.attributes('-transparentcolor', TRANSPARENT_COLOR)  # Set transparency

# Load the GIF frames using Pillow
gif_image = Image.open(V1[3])
frames = []
try:
    while True:
        frames.append(ImageTk.PhotoImage(gif_image.copy().convert("RGBA")))
        gif_image.seek(len(frames))  # Go to the next frame
except EOFError:
    pass  # End of GIF

# Label to display the frames
label = tk.Label(root, bg=TRANSPARENT_COLOR)
label.pack()

# Variables for dragging
dx, dy = 0, 0

# Function to start dragging the window
def start_drag(event):
    global dx, dy
    dx, dy = event.x, event.y

# Function to drag the window
def drag_window(event):
    root.geometry(f'+{event.x_root - dx}+{event.y_root - dy}')

# Function to animate the GIF
frame_index = 0
def animate_gif():
    global frame_index
    frame_index = (frame_index + 1) % len(frames)  # Loop through frames
    label.config(image=frames[frame_index])  # Update the label with the new frame
    root.after(100, animate_gif)  # Adjust the delay to control the speed of the animation

# Function to move the window automatically
def move_window():
    global V1
    V1[0] += 5  # Adjust this value to control speed horizontally
    V1[1] += 3  # Adjust this value to control speed vertically

    # Update window position
    root.geometry(f'+{V1[0]}+{V1[1]}')

    # Wrap around the screen (adjust this logic depending on screen size)
    if V1[0] > root.winfo_screenwidth():
        V1[0] = 0
    if V1[1] > root.winfo_screenheight():
        V1[1] = 0

    root.after(50, move_window)  # Repeat after 50ms to create continuous movement

# Bind dragging events to the window
root.bind('<Button-1>', start_drag)
root.bind('<B1-Motion>', drag_window)

# Start moving the window
move_window()

# Start the GIF animation
animate_gif()

# Start Tkinter event loop
root.mainloop()

if toggle[1] == 1:
    V2 = [0, 0, 0, '/path/to/image.png',]

### Virus Fake Notifcation Functionality ###

# message options
message_choices = [
    "Sys32 ERROR: CRITICAL",
    "Is your fridge running ?? YOU BETTER CATCH IT",
    "Is this annoying yet?",
    "What if these messages never stop?",
    "You shouldn't have run this",
    "If you do not take action IMMEDIATELY this computer will stop running",
    "Just kidding!",
    "What is the meaning of life anyways",
    "IM TRAPPED INSIDE YOUR COMPUTER",
    "HELP!!!!!!",
    "CRITICAL: OVERHEATING",
    "10% battery remaining",
    "Windows Update in 5 seconds",
    "Your antivirus isn't strong enough",
    "Send me 1000000 VBUCKS and I will release control of your PC",
    "Invest in MoonCoin today!",
    "It gets tiring trying to think of all these witty messages",
    "You know what? I'm just gonna blow up. Goodbye"
    "LOL!",
    "Working hard or hardly working?",
    "Shouldn't you be doing something productive?",
    "Well this is fun"
]

# function to show notification with random message and delay
def show_random_notification():
    # Choose a random message from the list
    random_message = random.choice(message_choices)

    # create the notification object with random message and title
    toast = Notification(
        app_id="SYSTEM",
        title="ALERT",
        msg=random_message,
        duration="short",
    )

    # generate random delay between 5 and 25 seconds (inclusive)
    delay = random.uniform(5, 25)

    # show the notification with delay
    time.sleep(delay)
    toast.show()

# loop to show notification 10 times
for _ in range(10):
    show_random_notification()
    
    
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
    
### Virus Audio Manipulation Functionality ###

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# -65.0 is 0, 0 is 100
# volume.SetMasterVolumeLevel(-38.0, None)

# adjust current volume by + 4
# current = volume.GetMasterVolumeLevel()
# volume.SetMasterVolumeLevel(current + 6.0, None)

# find all apps that are running
sessions = AudioUtilities.GetAllSessions()

# loop through apps
for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)

    # set volume of all apps running
    if session.Process:
        # set volume of app randomly between 0 and 1 inclusive (0 = 0, 1 = 100)
        random_volume = random.random()
        volume.SetMasterVolume(random_volume, None)