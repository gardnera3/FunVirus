import tkinter as tk
import os
from PIL import Image, ImageTk  # Requires the Pillow library

current_directory = os.path.dirname(os.path.abspath(__file__))
with open('stewieSettings', 'r') as f:
    # Default is '100'
    animationSpeed = f.readline().strip()
    # Default is = '50'
    dragSpeed = f.readline().strip()
    # Default is 'Stewie Mode'
    gifselection = f.readline().strip()
f.close()

if gifselection == 'Sonic Mode':
    gif = os.path.join(current_directory, '..', 'Assets', 'sonic.gif')
elif gifselection == 'Stewie Mode':
    gif = os.path.join(current_directory, '..', 'Assets', 'stewie.gif')
elif gifselection == 'Thanos Mode':
    gif = os.path.join(current_directory, '..', 'Assets', 'thanos.gif')
else:
    gif = os.path.join(current_directory, '..', 'Assets', 'stewie.gif')


V1 = [0, 0, 5, 3, gif]  # Change this to your GIF file. V1[2] = dx, V1[3] = dy

# Select a color as the transparent color
TRANSPARENT_COLOR = '#abcdef'

# Initialize the root window
root = tk.Tk()
root.overrideredirect(1)  # Removes the window border
root.attributes('-transparentcolor', TRANSPARENT_COLOR)  # Set transparency

# Load the GIF frames using Pillow
gif_image = Image.open(V1[4])
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
    root.after(animationSpeed, animate_gif)  # Adjust the delay to control the speed of the animation

# Function to move the window automatically and bounce on edges
def move_window():
    global V1
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Update position
    V1[0] += V1[2]  # Horizontal movement
    V1[1] += V1[3]  # Vertical movement

    # Check for bouncing on screen edges
    if V1[0] <= 0 or V1[0] + label.winfo_width() >= screen_width:
        V1[2] = -V1[2]  # Reverse horizontal direction
    if V1[1] <= 0 or V1[1] + label.winfo_height() >= screen_height:
        V1[3] = -V1[3]  # Reverse vertical direction

    # Update window position
    root.geometry(f'+{V1[0]}+{V1[1]}')

    root.after(dragSpeed, move_window)  # Repeat after 50ms to create continuous movement

# Bind dragging events to the window
root.bind('<Button-1>', start_drag)
root.bind('<B1-Motion>', drag_window)

# Start moving the window
move_window()

# Start the GIF animation
animate_gif()

# Start Tkinter event loop
root.mainloop()

