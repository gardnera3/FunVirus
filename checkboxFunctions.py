# [1] Sorting dictionary for each checkbox. If checkbox not defined, print error.
def checkboxSort(self, checkbox):
    checkboxDict = {
        self.CheckBoxWidgetPNG: pngCheck, #[2]
        self.CheckBoxWidgetGIF: gifCheck, #[3]
        self.CheckBoxWidgetMOV: movCheck, #[4]
    }
    checkboxDict.get(checkbox, lambda: print('Unknown Checkbox.'))(self, checkbox)


# [2] Checkbox action for PNG Checkbox
def pngCheck(self, checkbox):
    toggleVisualsCheckboxes(self, checkbox)
    if checkbox.isChecked():
        print('PNG Checked!')
    else:
        print('PNG Unchecked!')


# [3] Checkbox action for GIF Checkbox
def gifCheck(self, checkbox):
    toggleVisualsCheckboxes(self, checkbox)
    if checkbox.isChecked():
        print('GIF Checked!')
    else:
        print('GIF Unchecked!')


# [4] Checkbox action for MOV Checkbox
def movCheck(self, checkbox):
    toggleVisualsCheckboxes(self, checkbox)
    if checkbox.isChecked():
        print('MOV Checked!')
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
