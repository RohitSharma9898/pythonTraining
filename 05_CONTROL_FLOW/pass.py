"""
PASS STATEMENT

pass is a placeholder.

It does nothing when executed.

It is useful when we want to create
a block of code but don't want to write
the implementation yet.
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

if True:
    pass


# ==========================================
# FUNCTION PLACEHOLDER
# ==========================================

def login():
    pass


# We can implement it later.


# ==========================================
# CLASS PLACEHOLDER
# ==========================================

class Student:
    pass


student1 = Student()

# ==========================================
# LOOP WITH PASS
# ==========================================

for i in range(5):

    if i == 2:
        pass

    print(i)


# ==========================================
# PASS VS CONTINUE
# ==========================================

"""
pass:
    Does nothing.
    Program continues normally.

continue:
    Skips the current loop iteration.
"""

for i in range(5):

    if i == 2:
        pass

    print("pass:", i)


for i in range(5):

    if i == 2:
        continue

    print("continue:", i)