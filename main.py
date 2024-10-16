import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QComboBox

import buttonFunctions
import checkboxFunctions


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        self.setWindowIcon(QIcon('Assets/icon.png'))

        # [1] Load UI File, so we can easily edit and update via code.
        uic.loadUi("Main.ui", self)

        # [2] Widgets that are edited.
        self.ButtonWidgetSave = self.findChild(QPushButton, "saveButton")
        self.ButtonWidgetReset = self.findChild(QPushButton, "resetButton")
        self.CheckBoxWidgetPNG = self.findChild(QCheckBox, "visualsPNGCheckBox")
        self.CheckBoxWidgetMOV = self.findChild(QCheckBox, "visualsMOVCheckBox")
        self.CheckBoxWidgetGIF = self.findChild(QCheckBox, "visualsGIFCheckBox")
        self.ComboBoxWidgetPresets = self.findChild(QComboBox, "visualsPresetsComboBox")

        # [3] Connect buttons to the def clicked function -> buttonFunctions.py -> def buttonSort.
        self.ButtonWidgetSave.clicked.connect(lambda: self.clicked(self.ButtonWidgetSave))
        self.ButtonWidgetReset.clicked.connect(lambda: self.clicked(self.ButtonWidgetReset))

        # [4] Connect checkboxes to the def checked function -> checkboxFunctions.py -> def checkboxSort.
        self.CheckBoxWidgetPNG.toggled.connect(lambda: self.checked(self.CheckBoxWidgetPNG))
        self.CheckBoxWidgetMOV.toggled.connect(lambda: self.checked(self.CheckBoxWidgetMOV))
        self.CheckBoxWidgetGIF.toggled.connect(lambda: self.checked(self.CheckBoxWidgetGIF))

        # [5] Add comboboxes
        self.ComboBoxWidgetPresets.addItems(["Default...", "Stewie Mode", "Thanos Mode", "Sonic Mode"])
        StewieMode = QIcon('Assets/stewie.png')
        self.ComboBoxWidgetPresets.setItemIcon(1, StewieMode)
        ThanosMode = QIcon('Assets/thanos.png')
        self.ComboBoxWidgetPresets.setItemIcon(2, ThanosMode)
        SonicMode = QIcon('Assets/sonic.png')
        self.ComboBoxWidgetPresets.setItemIcon(3, SonicMode)

        # [6] Show App
        self.show()

    # [7] Sends button clicks to buttonFunctions.py
    def clicked(self, button):
        buttonFunctions.buttonSort(self, button)

    # [8] Sends checkbox changes to checkboxFunctions.py
    def checked(self, checkbox):
        checkboxFunctions.checkboxSort(self, checkbox)

# [9] --- Main ---
def main():
    app = QApplication(sys.argv)
    UIWindow = UI()
    app.exec_()

# [10] ---> Startup <---
if __name__ == '__main__':
    main()
