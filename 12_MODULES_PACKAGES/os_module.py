"""
OS MODULE

The os module allows Python to interact
with the operating system.
"""

import os


# Current working directory

print("Current directory:")

print(os.getcwd())


# List files and folders

print("\nFiles and folders:")

print(os.listdir())


# Create a folder

folder_name = "test_folder"


if not os.path.exists(folder_name):

    os.mkdir(folder_name)

    print("Folder created.")

else:

    print("Folder already exists.")