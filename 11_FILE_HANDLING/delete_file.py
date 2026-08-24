"""
DELETE A FILE

Be careful when using remove().
The file will be permanently deleted.
"""

import os


file_name = "students.txt"


if os.path.exists(file_name):

    os.remove(file_name)

    print("File deleted successfully.")

else:

    print("File does not exist.")