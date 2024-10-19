import writeToTemp

# [1] Sorting dictionary for each checkbox. If checkbox not defined, print error.
def checkboxSort(self, checkbox):
    checkboxDict = {
        self.CheckBoxWidgetPNG: pngCheck, #[2]
        self.CheckBoxWidgetGIF: gifCheck, #[3]
        self.CheckBoxWidgetMOV: movCheck, #[4]
        self.CheckBoxWidgetSoundOne: check, #[5]
        self.CheckBoxWidgetSoundTwo: check, #[6]
        self.CheckBoxWidgetSoundThree: check, # [7]
        self.CheckBoxWidgetRotateScreen: check, #[8]
        self.CheckBoxWidgetBSOD: check, #[9]
        self.CheckBoxWidgetPopUps: check, #[10]
    }
    checkboxDict.get(checkbox, lambda: print('Unknown Checkbox.'))(self, checkbox)

# [2] Checkbox action for PNG Checkbox
def pngCheck(self, checkbox):
    toggleVisualsCheckboxes(self, checkbox)
    if checkbox.isChecked():
        print('PNG Checked!')
        writeToTemp.writeInTempFile('PNG', 0)
    else:
        print('PNG Unchecked!')

# [3] Checkbox action for GIF Checkbox
def gifCheck(self, checkbox):
    toggleVisualsCheckboxes(self, checkbox)
    if checkbox.isChecked():
        print('GIF Checked!')
        writeToTemp.writeInTempFile('GIF', 0)
    else:
        print('GIF Unchecked!')

# [4] Checkbox action for MOV Checkbox
def movCheck(self, checkbox):
    toggleVisualsCheckboxes(self, checkbox)
    if checkbox.isChecked():
        print('MOV Checked!')
        writeToTemp.writeInTempFile('MOV', 0)
    else:
        print('MOV Unchecked!')
        
# [5] Function to enable/disable other checkboxes
def toggleVisualsCheckboxes(self, current_checkbox):
    # For Visuals Checkboxes
    checkboxes = [self.CheckBoxWidgetPNG, self.CheckBoxWidgetGIF, self.CheckBoxWidgetMOV]

    if current_checkbox.isChecked():
        # Disable all other checkboxes if the current one is checked
        for checkbox in checkboxes:
            if checkbox != current_checkbox:
                checkbox.setDisabled(True)
    else:
        # Enable all checkboxes if the current one is unchecked
        for checkbox in checkboxes:
            checkbox.setEnabled(True)
            writeToTemp.writeInTempFile('', 0)
            
# [6] Function for non visual checkboxes (want to be able to check more than one for non visual options)
def check (self, checkbox):
    checkBoxName = checkbox.objectName()
    if checkbox.isChecked():
        print(f'{checkBoxName} Checked!')
        writeToTemp.writeInTempFile(checkBoxName, 0)
    else:
        print(f'{checkBoxName} Unchecked!')
            