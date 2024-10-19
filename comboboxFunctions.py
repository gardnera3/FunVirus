import writeToTemp

# [1] Sorting dictionary for each combobox. If combobox not defined, print error.
def comboboxSort(self, combobox):
    comboboxDict = {
        self.ComboBoxWidgetPresets: visualsPresets,  # [2]
        self.ComboBoxWidgetStyles: visualsStyles,  # [3]
    }
    # Get function from dictionary list and call, or print error.
    if combobox in comboboxDict:
        comboboxDict[combobox](self, combobox)
    else:
        print('Unknown Selected')

# [2] Function for ComboBoxWidgetPresets selection
def visualsPresets(self, combobox):
    current_text = combobox.currentText()
    print(f"Presets ComboBox: {current_text}")
    writeToTemp.writeInTempFile(current_text, 1)

# [3] Function for ComboBoxWidgetStyle selection
def visualsStyles(self, combobox):
    current_text = combobox.currentText()
    print(f"Styles ComboBox: {current_text}")
    writeToTemp.writeInTempFile(current_text, 2)
