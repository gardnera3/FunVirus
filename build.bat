@echo off
pip install pyinstaller
pyinstaller --onefile --windowed Virus.py
echo Compilation complete. Check the 'dist' folder for Virus.exe