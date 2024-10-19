import os

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
    with open('tempData.txt', 'r') as f, open('saveData.txt', 'a') as f2:
        f2.seek(0)
        f2.truncate()
        for line in f:
            f2.write(line)
    f.close()
    f2.close()
    os.remove('tempData.txt')

# [3] Reset Button Action
def resetButton():
    # Create 'factory default' settings.
    print('Reset button action!')

# [4] Another (Undeveloped) Button Action
