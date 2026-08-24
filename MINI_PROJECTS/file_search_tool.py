"""
====================================================
                FILE SEARCH TOOL
====================================================

Search for a word inside a text file.

Concepts:

    file handling
    exceptions
    strings
"""


filename = input("Enter file name: ")

word = input("Enter word to search: ")


try:

    with open(filename, "r") as file:

        content = file.read()


    if word.lower() in content.lower():

        print("Word found.")

    else:

        print("Word not found.")


except FileNotFoundError:

    print("File does not exist.")