from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QFrame, QSlider
import os
toggle_array2 = [0, 0, 0, 0, 0, 0, 0, 0]

current_directory = os.path.dirname(os.path.abspath(__file__))
assets_directory = os.path.join(current_directory, 'Assets')

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
    window.pushButton_6.setText(os.getlogin())

    window.pushButton_9.clicked.connect(lambda: changeNotifs(window))
    window.pushButton_2.clicked.connect(lambda: changeNotifs(window))
    window.pushButton.clicked.connect(lambda: menuCloseOrOpen(window))
    window.pushButton_4.clicked.connect(lambda: menuCloseOrOpen(window))
    window.pushButton_5.clicked.connect(lambda: closeSubMenu(window))
    window.pushButton_8.clicked.connect(lambda: closeSubMenu(window))
    window.pushButton_10.clicked.connect(lambda: changeQuickInfo(window))
    window.pushButton_11.clicked.connect(lambda: changeQuickInfo(window))
    window.pushButton_6.clicked.connect(lambda: openProfile(window))

    ## Tabs
    window.homeButton.clicked.connect(lambda: homeButton(window))
    window.visualsButton.clicked.connect(lambda: visualsButton(window))
    window.soundsButton.clicked.connect(lambda: soundsButton(window))
    window.displaysButton.clicked.connect(lambda: displaysButton(window))
    window.popupsButton.clicked.connect(lambda: popupsButton(window))
    window.settingsButton.clicked.connect(lambda: settingsButton(window))
    window.infoButton.clicked.connect(lambda: infoButton(window))
    window.helpButton.clicked.connect(lambda: helpButton(window))

    # Configure horizontalSlider
    window.horizontalSlider = window.findChild(QSlider, 'horizontalSlider')
    window.horizontalSlider.setMinimum(1)
    window.horizontalSlider.setMaximum(500)
    window.horizontalSlider.setValue(100)

    # Configure horizontalSlider2
    window.horizontalSlider2 = window.findChild(QSlider, 'horizontalSlider2')
    window.horizontalSlider2.setMinimum(1)
    window.horizontalSlider2.setMaximum(500)
    window.horizontalSlider2.setValue(50)

    ## Checkboxes
    window.spriteActive.clicked.connect(lambda: spriteActivation(window))
    window.spriteActive.setStyleSheet(f"""
        QCheckBox::indicator {{
            image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
            width: 25px;
            height: 20px;
        }}
        """)
    window.randomAudioMixing.clicked.connect(lambda: randomAudioMixing(window))
    window.randomAudioMixing.setStyleSheet(f"""
            QCheckBox::indicator {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
            """)
    window.randomAudio.clicked.connect(lambda: randomAudio(window))
    window.randomAudio.setStyleSheet(f"""
                QCheckBox::indicator {{
                    image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                    width: 25px;
                    height: 20px;
                }}
                """)
    window.BSOD.clicked.connect(lambda: BSOD(window))
    window.BSOD.setStyleSheet(f"""
                    QCheckBox::indicator {{
                        image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                        width: 25px;
                        height: 20px;
                    }}
                    """)
    window.screenRotation.clicked.connect(lambda: screenRotation(window))
    window.screenRotation.setStyleSheet(f"""
                        QCheckBox::indicator {{
                            image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                            width: 25px;
                            height: 20px;
                        }}
                        """)
    window.notifications.clicked.connect(lambda: notifications(window))
    window.notifications.setStyleSheet(f"""
                            QCheckBox::indicator {{
                                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                                width: 25px;
                                height: 20px;
                            }}
                            """)
    window.youtubeBrainrot.clicked.connect(lambda: youtubeBrainrot(window))
    window.youtubeBrainrot.setStyleSheet(f"""
                                QCheckBox::indicator {{
                                    image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                                    width: 25px;
                                    height: 20px;
                                }}
                                """)
    window.updateScreen.clicked.connect(lambda: updateScreen(window))
    window.updateScreen.setStyleSheet(f"""
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
                    background-color: #1e2124;
                }}
                QComboBox QAbstractItemView {{
                    background-color: #1e2124;
                    color: white;
                    selection-background-color: #7289da;
                    selection-color: white;
                    border-left: 2px solid #444;
                    border-right: 2px solid #444;
                    border-bottom: 2px solid #444;
                    border-top: 1px solid #444;
                    border-bottom-left-radius: 10px;
                    border-bottom-right-radius: 10px;
                    padding: 5px;
                    margin: 0px;
                    outline: 0px;
                }}""")

def homeButton(window):
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
def spriteActivation(window):
    toggleTKinterCheckboxes(window, window.spriteActive)
    if window.spriteActive.isChecked():
        window.spriteActive.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.spriteActive.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)

def changeNotifs(window):
    if window.popupNotificationSubContainer.isHidden():
        window.popupNotificationSubContainer.show()
    else:
        window.popupNotificationSubContainer.hide()

def closeSubMenu(window):
    window.centerMenuContainer.hide()
    window.settingsButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.infoButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.helpButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)

def visualsPresets(window):
    current_text = window.comboBox.currentText()

def menuCloseOrOpen(window):
    original_button_texts = {
        'homeButton': 'Home',
        'displaysButton': 'Displays',
        'popupsButton': 'Pop-Ups',
        'soundsButton': 'Sounds',
        'visualsButton': 'Visuals',
        'settingsButton' : 'Settings',
        'infoButton': 'Information',
        'helpButton': 'Help'
    }
    # Check if the buttons currently have text
    if window.homeButton.text() == "":
        # Restore the original text to the buttons
        window.homeButton.setText(original_button_texts['homeButton'])
        window.displaysButton.setText(original_button_texts['displaysButton'])
        window.popupsButton.setText(original_button_texts['popupsButton'])
        window.soundsButton.setText(original_button_texts['soundsButton'])
        window.visualsButton.setText(original_button_texts['visualsButton'])
        window.settingsButton.setText(original_button_texts['settingsButton'])
        window.infoButton.setText(original_button_texts['infoButton'])
        window.helpButton.setText(original_button_texts['helpButton'])
    else:
        # Hide the text (set to an empty string)
        window.homeButton.setText("")
        window.displaysButton.setText("")
        window.popupsButton.setText("")
        window.soundsButton.setText("")
        window.visualsButton.setText("")
        window.settingsButton.setText("")
        window.infoButton.setText("")
        window.helpButton.setText("")

    current_width = window.leftMenuContainer.maximumWidth()
    if current_width == 60:
        window.leftMenuContainer.setMaximumWidth(16777215)
    else:
        window.leftMenuContainer.setMaximumWidth(60)

def settingsButton(window):
    window.stackedWidget.setCurrentIndex(0)
    window.centerMenuContainer.show()
    window.settingsButton.setStyleSheet("""
            QPushButton {
                background-color: #1f232a;
            }
        """)
    window.infoButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
    window.helpButton.setStyleSheet("""
            QPushButton {
                background-color: #16191d;
            }
        """)
def infoButton(window):
    window.stackedWidget.setCurrentIndex(1)
    window.centerMenuContainer.show()
    window.infoButton.setStyleSheet("""
                QPushButton {
                    background-color: #1f232a;
                }
            """)
    window.settingsButton.setStyleSheet("""
                QPushButton {
                    background-color: #16191d;
                }
            """)
    window.helpButton.setStyleSheet("""
                QPushButton {
                    background-color: #16191d;
                }
            """)
def helpButton(window):
    window.stackedWidget.setCurrentIndex(2)
    window.centerMenuContainer.show()
    window.helpButton.setStyleSheet("""
                QPushButton {
                    background-color: #1f232a;
                }
            """)
    window.settingsButton.setStyleSheet("""
                QPushButton {
                    background-color: #16191d;
                }
            """)
    window.infoButton.setStyleSheet("""
                QPushButton {
                    background-color: #16191d;
                }
            """)
def subMenuClose(window):
    window.centerMenuContainer.hide()

def subMenuOpen(window):
    window.centerMenuContainer.show()

def changeQuickInfo(window):
    if window.rightMenuContainer.isHidden():
        window.rightMenuContainer.show()
    else:
        window.rightMenuContainer.hide()

def openProfile(window):
    os.startfile(os.path.join(os.path.expanduser("~")))

def randomAudioMixing(window):
    if window.randomAudioMixing.isChecked():
        window.randomAudioMixing.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.randomAudioMixing.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def randomAudio(window):
    if window.randomAudio.isChecked():
        window.randomAudio.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.randomAudio.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def BSOD(window):
    toggleTKinterCheckboxes(window, window.BSOD)
    if window.BSOD.isChecked():
        window.BSOD.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.BSOD.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def screenRotation(window):
    toggleTKinterCheckboxes(window, window.screenRotation)
    if window.screenRotation.isChecked():
        window.screenRotation.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.screenRotation.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def notifications(window):
    if window.notifications.isChecked():
        window.notifications.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.notifications.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def youtubeBrainrot(window):
    if window.youtubeBrainrot.isChecked():
        toggle_array2[6] = 1
        print(toggle_array2)
        window.youtubeBrainrot.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        toggle_array2[6] = 0
        print(toggle_array2)
        window.youtubeBrainrot.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
def updateScreen(window):
    toggleTKinterCheckboxes(window, window.updateScreen)
    if window.updateScreen.isChecked():
        window.updateScreen.setStyleSheet(f"""
            QCheckBox::indicator:checked {{
                image: url({os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)
    else:
        window.updateScreen.setStyleSheet(f"""
            QCheckBox::indicator:unchecked {{
                image: url({os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')});
                width: 25px;
                height: 20px;
            }}
        """)

def toggleTKinterCheckboxes(window, current_checkbox):
    # List of all the checkboxes
    checkboxes = [window.BSOD, window.screenRotation, window.updateScreen, window.spriteActive]
    if current_checkbox.isChecked():
        # Disable all other checkboxes
        for checkbox in checkboxes:
            if checkbox != current_checkbox:
                checkbox.setDisabled(True)
    else:
        # Enable all checkboxes if the current one is unchecked
        for checkbox in checkboxes:
            checkbox.setEnabled(True)
