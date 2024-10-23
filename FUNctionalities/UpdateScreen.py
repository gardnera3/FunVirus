import tkinter as tk
import cv2
from PIL import Image, ImageTk

# Function to close the program (like forcing a shutdown)
def close_program(event=None):
    root.destroy()

# Function to play video frame by frame in the label at triple speed
def play_video():
    global frame_counter
    ret, frame = cap.read()

    # Skip frames to increase playback speed
    if ret and frame_counter % 3 == 0:  # Show every 3rd frame
        # Resize the frame to fit the full screen with higher quality interpolation
        frame = cv2.resize(frame, (screen_width, screen_height), interpolation=cv2.INTER_LANCZOS4)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_image = ImageTk.PhotoImage(Image.fromarray(frame))
        label.config(image=frame_image)
        label.image = frame_image

    if ret:
        frame_counter += 1
        root.after(10, play_video)  # Adjust timing for frame rate (~3x speed)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Loop video from start
        frame_counter = 0

# Create the root window
root = tk.Tk()
root.title("Blue Screen of Death")

# Set fullscreen mode and background to #0078d7 (BSOD blue)
root.attributes('-fullscreen', True)
root.configure(bg='#0078d7')

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Load the video file using OpenCV
video_path = "assets/UPDATE.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    root.destroy()

# Initialize frame counter
frame_counter = 0

# Create a label to hold the video
label = tk.Label(root, bg='#0078d7')
label.pack(fill="both", expand=True)

# Start playing the video
play_video()

# Close the window when any key is pressed
root.bind('<Escape>', close_program)

# Start the Tkinter main loop
root.mainloop()

# Release the video capture when the window is closed
cap.release()
