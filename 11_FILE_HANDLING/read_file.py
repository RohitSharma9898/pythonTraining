"""
READING A FILE

"r" means read mode.
"""


file = open("student.txt", "r")


data = file.read()


print(data)


file.close()





file = open("student.txt", "r")

data = file.read(10)

print(data)

file.close()