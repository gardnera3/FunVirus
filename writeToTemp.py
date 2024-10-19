import os

def writeInTempFile(item, index):
    file_path = "tempData.txt"

    # If "tempData.txt" hasn't been made yet...
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            # Create an empty file
            pass
    # Initialize an empty list
    with open(file_path, "r") as f:
        lines = f.readlines()
    # Check if index is within range; if not, extend with empty lines
    if index >= len(lines):
        lines.extend(["\n"] * (index - len(lines) + 1))
    lines[index] = item + '\n'
    with open(file_path, "w") as f:
        f.writelines(lines)
