"""
====================================================
                 FILE HANDLING
====================================================

File handling means creating, reading, writing,
updating and deleting files using Python.

Real-life examples:

- Student records
- Employee information
- Logs
- Reports
- Configuration files
- Notes
- Application data


Basic steps:

1. Open the file
2. Perform an operation
3. Close the file
"""


# Basic syntax:

file = open("student.txt", "r")

# Read the file

data = file.read()

print(data)

# Close the file

file.close()