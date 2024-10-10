import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTabWidget, QScrollArea

import buttonFunctions


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # [1] Load UI File, so we can easily edit and update via code.
        uic.loadUi("template.ui", self)

        # [2] Widgets that are edited.
        self.ButtonWidgetSave = self.findChild(QPushButton, "pushButton")
        self.ButtonWidgetReset = self.findChild(QPushButton, "pushButton_2")
        self.ButtonWidgetRandom1 = self.findChild(QPushButton, "pushButton_3")

        # [3] Connect buttons to the def clicked function -> buttonFunctions.py -> def buttonSort.
        self.ButtonWidgetSave.clicked.connect(lambda: self.clicked(self.ButtonWidgetSave))
        self.ButtonWidgetReset.clicked.connect(lambda: self.clicked(self.ButtonWidgetReset))
        self.ButtonWidgetRandom1.clicked.connect(lambda: self.clicked(self.ButtonWidgetRandom1))

        # [4] Show App
        self.show()

    # [5] Sends any button presses identified above [3] to buttonFunctions.py
    def clicked(self, button):
        buttonFunctions.buttonSort(self, button)

def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

if __name__ == '__main__':
    main()
