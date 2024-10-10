import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load UI File, so we can easily edit and update via code.
        uic.loadUi("template.ui", self)

        # Widgets that are edited.
        self.ButtonWidgetSave = self.findChild(QPushButton, "pushButton")
        self.ButtonWidgetReset = self.findChild(QPushButton, "pushButton_2")

        # Connect both buttons to the same clicked function, passing the button object
        self.ButtonWidgetSave.clicked.connect(lambda: self.clicked(self.ButtonWidgetSave))
        self.ButtonWidgetReset.clicked.connect(lambda: self.clicked(self.ButtonWidgetReset))

        # Show App
        self.show()

    # Button, figures out which was pressed.
    ## To-Do: Make it switch case and put it in its own file.
    ## Reason for it is to have multiple cases under one function.
    def clicked(self, button):
        if button == self.ButtonWidgetSave:
            print('Save! Pressed')
        elif button == self.ButtonWidgetReset:
            print('Reset! Pressed')
        else:
            print("Error! Unknown button.")

def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

if __name__ == '__main__':
    main()
