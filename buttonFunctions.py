# [1] Sorting dictionary for each button. If button not defined, print error.
def buttonSort(self, button):
    buttonDict = {
        self.ButtonWidgetSave: saveButton, #[2]
        self.ButtonWidgetReset: resetButton, #[3]
    }
    buttonDict.get(button, lambda: print('Unknown Pressed.'))()

# [2] Save Button action
def saveButton():
    print('Save button action!')

# [3] Reset Button Action
def resetButton():
    print('Reset button action!')

# [4] Another (Undeveloped) Button Action
