from PyQt5.QtCore import Qt, reset
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QFrame, QComboBox
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
assets_directory = os.path.join(current_directory, 'assets')

def widgetSetup(window):
    # Variables for dragging and resizing
    window.oldPos = None
    window.resizing = False

    # Size grip feature (bottom right)
    window.sizeGrip = window.findChild(QFrame, 'sizeGrip')
    window.testButton = window.findChild(QPushButton, 'pushButton_3')
    window.testButton.setAttribute(Qt.WA_TransparentForMouseEvents)
    # Change cursor
    window.sizeGrip.setCursor(QCursor(Qt.SizeFDiagCursor))

    # Minimize, maximize, and close buttons
    window.minimizeButton = window.findChild(QPushButton, 'minimizeButton')
    window.maximizeButton = window.findChild(QPushButton, 'maximizeButton')
    window.closeButton = window.findChild(QPushButton, 'closeButton')

    # Connect buttons to their respective methods/actions & stylesheets
    ## Window widgets
    window.minimizeButton.clicked.connect(window.minimize_window)
    window.maximizeButton.clicked.connect(window.maximize_window)
    window.closeButton.clicked.connect(window.close_window)

    window.pushButton_9.clicked.connect(lambda: closeNotifs(window))
    ## Tabs
    window.homeButton.clicked.connect(lambda: homeButton(window))
    window.visualsButton.clicked.connect(lambda: visualsButton(window))
    window.soundsButton.clicked.connect(lambda: soundsButton(window))
    window.displaysButton.clicked.connect(lambda: displaysButton(window))
    window.popupsButton.clicked.connect(lambda: popupsButton(window))
    ## Checkboxes
    window.pngCheckbox.clicked.connect(lambda: pngCheck(window))
    window.pngCheckbox.setStyleSheet(f"""
        QCheckBox::indicator {{
            image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
            width: 25px;
            height: 20px;
        }}
        """)
    window.gifCheckbox.clicked.connect(lambda: gifCheck(window))
    window.gifCheckbox.setStyleSheet(f"""
        QCheckBox::indicator {{
            image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
            width: 25px;
            height: 20px;
        }}
        """)
    window.movCheckbox.clicked.connect(lambda: movCheck(window))
    window.movCheckbox.setStyleSheet(f"""
        QCheckBox::indicator {{
            image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
            width: 25px;
            height: 20px;
        }}
        """)
    ## Comboboxes
    window.comboBox.currentIndexChanged.connect(lambda: visualsPresets(window))
    window.comboBox.addItems(["Default...", "Stewie Mode", "Thanos Mode", "Sonic Mode"])
    StewieMode = QIcon(os.path.join(assets_directory, 'stewie.png').replace('\\', '/'))
    window.comboBox.setItemIcon(1, StewieMode)
    ThanosMode = QIcon(os.path.join(assets_directory, 'thanos.png').replace('\\', '/'))
    window.comboBox.setItemIcon(2, ThanosMode)
    SonicMode = QIcon(os.path.join(assets_directory, 'sonic.png').replace('\\', '/'))
    window.comboBox.setItemIcon(3, SonicMode)
    window.comboBox.setStyleSheet(f"""
                QComboBox::down-arrow {{
                    image: url({os.path.join(assets_directory, 'combobox_arrow.png').replace('\\', '/')});
                    width: 20px;
                    height: 20px;
                }}
                QComboBox::drop-down {{
                    subcontrol-origin: padding;
                    subcontrol-position: center right;
                    border-left: 0px;
                    width: 12px;
                }}
                QComboBox{{
                    border: 2px solid #424549;
                    border-radius: 5px;
                    selection-background-color: #7289da;
                    selection-color: #424549;
                    padding: 3px;
                }}
                QComboBox QAbstractItemView {{
                    background-color: #1e2124;
                    color: white;
                    selection-background-color: #7289da;
                    selection-color: white;
                    border: 1px solid #444;
                    padding: 5px;
                    margin: 0px;
                    outline: 0px;
                }}""")

def homeButton(window):
    print('Home Tab accessed!')
    # Highlight (always first) vvv
    window.stackedWidget_3.setCurrentIndex(0)
    window.stackedWidget_2.setCurrentIndex(0)
    window.homeButton.setStyleSheet("""
            QPushButton {
                background-color: #1f232a;
            }
        """)
    window.visualsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.soundsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.displaysButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.popupsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
def visualsButton(window):
    print('Visuals Tab accessed!')
    window.stackedWidget_3.setCurrentIndex(1)
    window.stackedWidget_2.setCurrentIndex(1)
    window.visualsButton.setStyleSheet("""
            QPushButton {
                background-color: #1f232a;
            }
        """)
    window.homeButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.soundsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.displaysButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.popupsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
def soundsButton(window):
    print('Sounds Tab accessed!')
    window.stackedWidget_3.setCurrentIndex(2)
    window.stackedWidget_2.setCurrentIndex(2)
    window.soundsButton.setStyleSheet("""
            QPushButton {
                background-color: #1f232a;
            }
        """)
    window.homeButton.setStyleSheet("""
           QPushButton {
               background-color: #16191d;
           }
       """)
    window.visualsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.displaysButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.popupsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)

def displaysButton(window):
    print('Displays Tab accessed!')
    window.stackedWidget_3.setCurrentIndex(3)
    window.stackedWidget_2.setCurrentIndex(3)
    window.displaysButton.setStyleSheet("""
            QPushButton {
                background-color: #1f232a;
            }
        """)
    window.homeButton.setStyleSheet("""
           QPushButton {
               background-color: #16191d;
           }
       """)
    window.visualsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.soundsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.popupsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)

def popupsButton(window):
    print('Pop-Ups Tab accessed!')
    window.stackedWidget_3.setCurrentIndex(4)
    window.stackedWidget_2.setCurrentIndex(4)
    window.popupsButton.setStyleSheet("""
            QPushButton {
                background-color: #1f232a;
            }
        """)
    window.homeButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.visualsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.soundsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.displaysButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)

def pngCheck(window):
    toggleVisualsCheckboxes(window, window.pngCheckbox)
    if window.pngCheckbox.isChecked():
        print('PNG Checked!')
        window.pngCheckbox.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        print('PNG Unchecked!')
        window.pngCheckbox.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)

def gifCheck(window):
    toggleVisualsCheckboxes(window, window.gifCheckbox)
    if window.gifCheckbox.isChecked():
        print('GIF Checked!')
        window.gifCheckbox.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        print('GIF Unchecked!')
        window.gifCheckbox.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)

def movCheck(window):
    toggleVisualsCheckboxes(window, window.movCheckbox)
    if window.movCheckbox.isChecked():
        print('MOV Checked!')
        window.movCheckbox.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        print('MOV Unchecked!')
        window.movCheckbox.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def toggleVisualsCheckboxes(window, current_checkbox):
    # List of all the checkboxes
    checkboxes = [window.pngCheckbox, window.gifCheckbox, window.movCheckbox]
    if current_checkbox.isChecked():
        # Disable all other checkboxes
        for checkbox in checkboxes:
            if checkbox != current_checkbox:
                checkbox.setDisabled(True)
    else:
        # Enable all checkboxes if the current one is unchecked
        for checkbox in checkboxes:
            checkbox.setEnabled(True)

def closeNotifs(window):
    window.popupNotificationSubContainer.deleteLater()

def visualsPresets(window):
    current_text = window.comboBox.currentText()
    print(f"Selected preset: {current_text}")