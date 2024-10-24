import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
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
        # Show the app
        self.show()

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

# ---> Startup <---
if __name__ == '__main__':
    main()
