"""
None Data Type

None represents the absence of a value.

It is different from:
0
False
""
"""

value = None

print(value)
print(type(value))


# ==============================
# None in variables
# ==============================

result = None

print(result)


# Later we can assign a value

result = 100

print(result)


# ==============================
# Checking None
# ==============================

value = None

if value is None:
    print("Value is not available")
else:
    print("Value is available")


# ==============================
# None vs False
# ==============================

print(None == False)
print(None == 0)
print(None == "")


# Use 'is' when checking None

value = None

print(value is None)
print(value is not None)


# ==============================
# Function returning None
# ==============================

def display_message():
    print("Hello Python")


result = display_message()

print("Returned value:", result)
print("Returned type:", type(result))