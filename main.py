import sys
import subprocess
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import resources_rc  # Import the compiled resource file
from widgetSetup import widgetSetup

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("controlpanel.ui", self)  # Load the UI file
        # Remove tab bar on top
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Call widgetSetup (button functions, checkboxes, etc.)
        widgetSetup(self)

        # Create a big red "EXPORT!" button
        self.export_button = QPushButton("EXPORT!")
        self.export_button.setFixedSize(100, 160)  # Set button size
        self.export_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
        self.export_button.clicked.connect(self.run_script)  # Connect button to run script

        # Add the button to the bottom of the main layout
        self.central_widget = self.centralWidget()  # Get the central widget from the loaded .ui file
        self.layout = self.central_widget.layout()  # Access the layout of the central widget
        self.layout.addWidget(self.export_button, alignment=Qt.AlignBottom)  # Add button at the bottom

        # Show the app
        self.show()

    def run_script(self):
        # Run the external Python script
        subprocess.Popen(["python", "run.py"])

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.sizeGrip.underMouse():
                self.resizing = True
            else:
                self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos and not self.resizing:
            # Dragging
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        elif self.resizing:
            # Handle resizing
            delta = event.globalPos() - self.geometry().bottomRight()
            newWidth = self.width() + delta.x()
            newHeight = self.height() + delta.y()
            self.resize(newWidth, newHeight)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = None
            self.resizing = False

    def minimize_window(self):
        self.showMinimized()

    def maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_window(self):
        self.close()

# Main
def main():
    app = QApplication(sys.argv)
    # Load the main window
    UIWindow = UI()
    app.exec_()

    toggle = [0,0,0,0,0,0,0,0]
    # 0 = stewie.py
    # 1 = BSOD.py
    # 2 = UpdateScreen.py
    # 3 = notifications.py
    # 4 = play_sound.py
    # 5 = audio.py
    # 6 = youtube.py
    # 7 = rotate.py

# ---> Startup <---
if __name__ == '__main__':
    main()
