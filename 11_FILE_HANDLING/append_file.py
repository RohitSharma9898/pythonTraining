"""
APPEND MODE

"a" is used to add new data
at the end of an existing file.

Old data is not deleted.
"""


file = open("student.txt", "a")


file.write("City: Vadodara\n")
file.write("Marks: 90\n")


file.close()


print("Data added successfully.")