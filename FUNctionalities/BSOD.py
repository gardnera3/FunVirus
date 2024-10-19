import tkinter as tk
from PIL import Image, ImageTk

# Function to close the program (like forcing a shutdown)
def close_program(event=None):
    root.destroy()

# Create the root window
root = tk.Tk()
root.title("Blue Screen of Death")

# Set fullscreen mode and background to #0078d7 (BSOD blue)
root.attributes('-fullscreen', True)
root.configure(bg='#0078d7')

# Load the BSOD image
try:
    image = Image.open("Assets\BSOD.png")
    print(f"Image loaded with size: {image.size}")  # Check if the image is loaded

    bsod_photo = ImageTk.PhotoImage(image)

    # Create a label to hold the image and pack it in the window
    label = tk.Label(root, image=bsod_photo, bg='#0078d7')
    label.pack(fill="both", expand=True)

except Exception as e:
    print(f"Error loading image: {e}")

# Close the window when any key is pressed
root.bind('<Escape>', close_program)


# Start the Tkinter main loop
root.mainloop()
