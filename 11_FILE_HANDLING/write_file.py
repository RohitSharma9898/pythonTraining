"""
WRITE TO A FILE

"w" means write mode.

If the file already contains data,
write mode replaces the old data.
"""


file = open("student.txt", "w")


file.write("Name: Rohit\n")
file.write("Age: 21\n")
file.write("Course: Python\n")


file.close()


print("Data written successfully.")