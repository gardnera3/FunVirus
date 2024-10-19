# widgetSetup.py

import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton, QCheckBox, QComboBox, QWidget, QTabWidget, QSlider

import styles

def widgetSetup(ui_instance):
    # Current directory and assets directory
    current_directory = os.path.dirname(os.path.abspath(__file__))
    assets_directory = os.path.join(current_directory, 'assets')

    # Locate widgets that are going to be edited.
    ui_instance.ButtonWidgetSave = ui_instance.findChild(QPushButton, "saveButton")
    ui_instance.ButtonWidgetReset = ui_instance.findChild(QPushButton, "resetButton")
    ui_instance.CheckBoxWidgetPNG = ui_instance.findChild(QCheckBox, "visualsPNGCheckBox")
    ui_instance.CheckBoxWidgetMOV = ui_instance.findChild(QCheckBox, "visualsMOVCheckBox")
    ui_instance.CheckBoxWidgetGIF = ui_instance.findChild(QCheckBox, "visualsGIFCheckBox")
    ui_instance.ComboBoxWidgetPresets = ui_instance.findChild(QComboBox, "visualsPresetsComboBox")
    ui_instance.ComboBoxWidgetStyles = ui_instance.findChild(QComboBox, "visualsStylesComboBox")
    ui_instance.TabWidgetVisuals = ui_instance.findChild(QTabWidget, "tabWidget")

    # stylesheets directory
    checkbox_mark_path = os.path.join(assets_directory, 'checkbox_mark.png').replace('\\', '/')
    checkbox_unchecked_path = os.path.join(assets_directory, 'checkbox.png').replace('\\', '/')
    arrow_path = os.path.join(assets_directory, 'combobox_arrow.png').replace('\\', '/')

    # Apply checkbox stylesheets
    ui_instance.CheckBoxWidgetPNG.setStyleSheet(styles.get_checkbox_styles(checkbox_mark_path, checkbox_unchecked_path))
    ui_instance.CheckBoxWidgetMOV.setStyleSheet(styles.get_checkbox_styles(checkbox_mark_path, checkbox_unchecked_path))
    ui_instance.CheckBoxWidgetGIF.setStyleSheet(styles.get_checkbox_styles(checkbox_mark_path, checkbox_unchecked_path))

    # Apply combobox stylesheets
    ui_instance.ComboBoxWidgetPresets.setStyleSheet(styles.get_combobox_styles(arrow_path))
    ui_instance.ComboBoxWidgetStyles.setStyleSheet(styles.get_combobox_styles(arrow_path))

    # Apply tab icon stylesheets
    icon1 = QIcon(os.path.join(assets_directory, 'stewie.png'))
    icon2 = QIcon(os.path.join(assets_directory, 'sound.png'))
    icon3 = QIcon(os.path.join(assets_directory, 'bluescreen.png'))
    icon4 = QIcon(os.path.join(assets_directory, 'popups.png'))

    # Set icons for each tab in TabWidget
    ui_instance.TabWidgetVisuals.setTabIcon(0, icon1)
    ui_instance.TabWidgetVisuals.setTabIcon(1, icon2)
    ui_instance.TabWidgetVisuals.setTabIcon(2, icon3)
    ui_instance.TabWidgetVisuals.setTabIcon(3, icon4)

    # Optionally, set tab text as well
    ui_instance.TabWidgetVisuals.setTabText(0, "Visuals")
    ui_instance.TabWidgetVisuals.setTabText(1, "Sounds")
    ui_instance.TabWidgetVisuals.setTabText(2, "Displays")
    ui_instance.TabWidgetVisuals.setTabText(3, "Pop-Ups")

    # Connect buttons to actions (buttonFunctions.py)
    ui_instance.ButtonWidgetSave.clicked.connect(lambda: ui_instance.clicked(ui_instance.ButtonWidgetSave))
    ui_instance.ButtonWidgetReset.clicked.connect(lambda: ui_instance.clicked(ui_instance.ButtonWidgetReset))

    # Connect checkboxes to actions (checkboxFunctions.py)
    ui_instance.CheckBoxWidgetPNG.toggled.connect(lambda: ui_instance.checked(ui_instance.CheckBoxWidgetPNG))
    ui_instance.CheckBoxWidgetMOV.toggled.connect(lambda: ui_instance.checked(ui_instance.CheckBoxWidgetMOV))
    ui_instance.CheckBoxWidgetGIF.toggled.connect(lambda: ui_instance.checked(ui_instance.CheckBoxWidgetGIF))

    # Add items to comboboxes
    ui_instance.ComboBoxWidgetPresets.addItems(["Default...", "Stewie Mode", "Thanos Mode", "Sonic Mode"])
    StewieMode = QIcon(os.path.join(assets_directory, 'stewie.png').replace('\\', '/'))
    ui_instance.ComboBoxWidgetPresets.setItemIcon(1, StewieMode)
    ThanosMode = QIcon(os.path.join(assets_directory, 'thanos.png').replace('\\', '/'))
    ui_instance.ComboBoxWidgetPresets.setItemIcon(2, ThanosMode)
    SonicMode = QIcon(os.path.join(assets_directory, 'sonic.png').replace('\\', '/'))
    ui_instance.ComboBoxWidgetPresets.setItemIcon(3, SonicMode)

    ui_instance.ComboBoxWidgetStyles.addItems(["Default...", "Christmas Style", "Halloween Style", "idk add more"])

    # Connect comboboxes to actions (comboboxFunctions.py)
    ui_instance.ComboBoxWidgetPresets.currentIndexChanged.connect(lambda: ui_instance.selection(ui_instance.ComboBoxWidgetPresets))
    ui_instance.ComboBoxWidgetStyles.currentIndexChanged.connect(lambda: ui_instance.selection(ui_instance.ComboBoxWidgetStyles))
