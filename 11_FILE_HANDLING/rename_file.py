"""
RENAME A FILE
"""

import os


old_name = "student.txt"

new_name = "students.txt"


if os.path.exists(old_name):

    os.rename(old_name, new_name)

    print("File renamed successfully.")

else:

    print("File does not exist.")