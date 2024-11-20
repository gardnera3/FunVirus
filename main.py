import sys
import subprocess
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import resources_rc  # Import the compiled resource file
from widgetSetup import widgetSetup
from Virus import update_toggle

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("controlpanel.ui", self)  # Load the UI file
        # Remove tab bar on top
        self.setWindowFlags(Qt.FramelessWindowHint)
        # Set the size of the window (default, at start)
        self.resize(1433, 825)
        # Call widgetSetup (button functions, checkboxes, etc.)
        widgetSetup(self)
        # Show the app
        self.show()

        # Connect buttons
        self.pushButton_12.clicked.connect(self.run_script)
        self.youtubeBrainrot.clicked.connect(self.update_youtube_brainrot)

    def run_script(self):
        """Run an external script and save settings."""
        slider1_value = self.horizontalSlider.value()
        slider2_value = self.horizontalSlider2.value()
        combobox_value = self.comboBox.currentText()

        with open('Assets/stewieSettings.txt', 'w') as f:
            # Write data to the file
            f.write(f'{int(slider1_value)}\n')
            f.write(f'{int(slider2_value)}\n')
            f.write(f'{combobox_value}\n')
        f.close()

        subprocess.Popen(["python", "run.py"])

    def update_youtube_brainrot(self):
        """Update toggle_array[6] when youtubeBrainrot is clicked."""
        update_toggle(6, 1)  # Set toggle_array[6] to 1
        print("youtubeBrainrot button clicked. toggle_array[6] updated.")

    def mousePressEvent(self, event):
        """Handle mouse press for dragging and resizing."""
        if event.button() == Qt.LeftButton:
            if hasattr(self, 'sizeGrip') and self.sizeGrip.underMouse():
                self.resizing = True
            else:
                self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging and resizing."""
        if self.oldPos and not self.resizing:
            # Dragging
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        elif self.resizing:
            # Resizing
            delta = event.globalPos() - self.geometry().bottomRight()
            newWidth = self.width() + delta.x()
            newHeight = self.height() + delta.y()
            self.resize(newWidth, newHeight)

    def mouseReleaseEvent(self, event):
        """Handle mouse release."""
        if event.button() == Qt.LeftButton:
            self.oldPos = None
            self.resizing = False

    def minimize_window(self):
        """Minimize the window."""
        self.showMinimized()

    def maximize_window(self):
        """Toggle between maximized and normal states."""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_window(self):
        """Close the application."""
        self.close()

# Main
def main():
    app = QApplication(sys.argv)

    # Load the main window
    UIWindow = UI()
    app.exec_()

# ---> Startup <---
if __name__ == '__main__':
    main()
