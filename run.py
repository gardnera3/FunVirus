import subprocess
import os
import shutil

# Specify the path to your Python script and assets folder
script_path = "Virus.py"
assets_folder = "Assets"  # Folder containing assets (images, data files, etc.)

# Additional modules that may not be automatically detected by PyInstaller
additional_modules = [
    "FUNctionalities.stewietest",
    "FUNctionalities.BSOD",
    "FUNctionalities.UpdateScreen",
    "FUNctionalities.notifications",
    "FUNctionalities.plays_sounds",
    "FUNctionalities.audio",
    "FUNctionalities.youtube",
    "FUNctionalities.rotate",
]

# Verify if the main script exists
if os.path.isfile(script_path):
    # Generate PyInstaller command with additional import options and assets
    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",
        "--console",
        f"--add-data={assets_folder};assets",  # Include assets folder
        script_path,
    ] + [f"--hidden-import={module}" for module in additional_modules]

    # Run PyInstaller command
    try:
        # Run PyInstaller to create the executable
        result = subprocess.run(pyinstaller_cmd, check=True)
        print("PyInstaller ran successfully. Check the 'dist' folder for the executable.")
        
        # Check if assets folder needs to be manually copied to dist (for testing or additional files)
        dist_assets_path = os.path.join("dist", "assets")
        if not os.path.exists(dist_assets_path):
            shutil.copytree(assets_folder, dist_assets_path)
            print("Assets folder copied to dist folder.")

    except subprocess.CalledProcessError as e:
        print("Error occurred while running PyInstaller:", e)
else:
    print(f"{script_path} not found. Please check the file path.")
