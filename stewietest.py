import tkinter as tk
from PIL import Image, ImageTk  # Requires the Pillow library

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
