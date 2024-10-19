import os
import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow

# Import widget setup function from widgetSetup.py
import widgetSetup
import buttonFunctions
import checkboxFunctions
import comboboxFunctions

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Set window icon and load the UI
        self.setWindowIcon(QIcon('assets/icon.png'))
        uic.loadUi("main.ui", self)

        # Handles widget initialization and connections.
        # It looks ugly, don't look into it.
        widgetSetup.widgetSetup(self)

        # Show the app
        self.show()

    # Sends button clicks to buttonFunctions.py
    def clicked(self, button):
        buttonFunctions.buttonSort(self, button)

    # Sends checkbox changes to checkboxFunctions.py
    def checked(self, checkbox):
        checkboxFunctions.checkboxSort(self, checkbox)

    # Sends combobox changes to comboboxFunctions.py
    def selection(self, combobox):
        comboboxFunctions.comboboxSort(self, combobox)

# Main
def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

    # Checks if tempData exists, deletes it when the program ends
    if os.path.exists("tempData.txt"):
        os.remove("tempData.txt")

# ---> Startup <---
if __name__ == '__main__':
    main()
