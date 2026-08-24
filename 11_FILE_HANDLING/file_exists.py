"""
CHECK WHETHER A FILE EXISTS
"""

import os


file_name = "student.txt"


if os.path.exists(file_name):

    print("File exists.")

else:

    print("File does not exist.")