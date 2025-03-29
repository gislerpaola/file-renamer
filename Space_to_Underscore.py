# Replace space with underscore

import os
import sys
from pathlib import Path

print("This program renames files changing space to underscore")

# Get the name of folder where files need to be renamed
while True:
    folder_to_rename = input("Which folder would you like to rename? - Please type the full path: ")

    if not Path(folder_to_rename).exists():
        print("\nInvalid folder path. Please try again.\n")
        continue  # Go back to asking for the folder

    print(f"\nFolder found: {folder_to_rename}\n")

# List files within that folder

    ignored_files = {".DS_Store", "desktop.ini", "Thumbs.db"}  # Add Windows + macOS hidden files

    print("Files Found:")

    for file in Path(folder_to_rename).iterdir():
        if file.is_file() and " " in file.name and file.name not in ignored_files:
            print(file.stem)

# Confirm these are the files

    correct_files = input("\nAre these the correct files? (y/n): ").strip().lower()

    if correct_files == 'y':
        break  # Exit loop and proceed with renaming
    elif correct_files == 'n':
        print("\nLet's try again.\n")
        continue
    else:
        print("\nInvalid input. Please enter 'y' or 'n'.\n")

# Loop through files and adds underscore

for file in Path(folder_to_rename).iterdir():
    if file.is_file() and " " in file.name and file.name not in ignored_files:
        new_name = file.name.replace(" ", "_")  # Replace spaces with underscores
        new_path = file.with_name(new_name)
        os.rename(file, new_path)

# Print confirmation
print("\nYour files have been renamed!")

another_folder = input("\nWould you like to rename another folder? (y/n): ").strip().lower()

if another_folder == 'y':
    print("\nRestarting process...\n")
    os.execv(sys.executable, ['python'] + sys.argv)  # Restart the program
elif another_folder == 'n':
    print("\nThank you! Exiting...")
    exit()  # End the script
else:
    print("\nInvalid input. Please enter 'y' or 'n'.")


