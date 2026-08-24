"""
EXCEPTION HANDLING WITH FILES

File operations can also cause exceptions.

Example:

Trying to open a file that doesn't exist.
"""


try:

    file = open("student.txt", "r")

    data = file.read()

    print(data)

    file.close()

except FileNotFoundError:

    print("File does not exist")


# ==========================================
# FINALLY
# ==========================================

file = None

try:

    file = open("student.txt", "r")

    print(file.read())

except FileNotFoundError:

    print("File not found")

finally:

    if file is not None:

        file.close()

    print("File operation completed")