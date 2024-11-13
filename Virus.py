import importlib
import threading
import time
# import main  # Uncomment this if `main` is needed

# Sample toggle array and file array
toggle_array = [0, 1, 0, 0, 0, 0, 0, 0]
file_array = [
    "FUNctionalities.stewietest", 
    "FUNctionalities.BSOD", 
    "FUNctionalities.UpdateScreen", 
    "FUNctionalities.notifications", 
    "FUNctionalities.plays_sounds", 
    "FUNctionalities.audio", 
    "FUNctionalities.youtube", 
    "FUNctionalities.rotate"
]

# Function to import a module based on its name
def import_module(name):
    if name == "FUNctionalities.BSOD":
        time.sleep(300)  # Wait for 5 minutes
    if name == "FUNctionalities.UpdateScreen":
        time.sleep(300)  # Wait for 5 minutes
    importlib.import_module(name)

# List to keep track of threads
threads = []

# Loop through the toggle array
for i in range(len(toggle_array)):
    if toggle_array[i] == 1:
        name = file_array[i]

        # Create and start a new thread for each module that needs to be imported
        thread = threading.Thread(target=import_module, args=(name,))
        threads.append(thread)
        thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
