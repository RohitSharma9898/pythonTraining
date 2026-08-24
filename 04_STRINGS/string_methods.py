"""
STRING METHODS

Python provides many built-in methods
for working with strings.
"""

text = "python programming"


# ==========================================
# CASE CONVERSION
# ==========================================

print(text.upper())

print(text.lower())

print(text.capitalize())

print(text.title())

print(text.swapcase())


# ==========================================
# SEARCH METHODS
# ==========================================

text = "Python Programming"

print(text.find("Python"))

print(text.find("Java"))

print(text.index("Python"))


# Difference:

# find() returns -1 if not found.
# index() raises ValueError if not found.


# ==========================================
# COUNT
# ==========================================

text = "banana"

print(text.count("a"))
print(text.count("n"))


# ==========================================
# REPLACE
# ==========================================

text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)


# ==========================================
# STARTSWITH / ENDSWITH
# ==========================================

text = "Python Programming"

print(text.startswith("Python"))

print(text.endswith("Programming"))


# ==========================================
# STRIP
# ==========================================

text = "   Python   "

print(text.strip())

print(text.lstrip())

print(text.rstrip())


# ==========================================
# SPLIT
# ==========================================

text = "Python Java C++"

languages = text.split()

print(languages)


# Split using separator

data = "apple,banana,mango"

fruits = data.split(",")

print(fruits)


# ==========================================
# JOIN
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

result = ", ".join(fruits)

print(result)


# ==========================================
# CHECKING STRING CONTENT
# ==========================================

text = "Python123"

print(text.isalpha())

print(text.isdigit())

print(text.isalnum())


text = "Python"

print(text.isalpha())

print(text.isdigit())

print(text.isalnum())


# ==========================================
# SPACE CHECK
# ==========================================

text = "   "

print(text.isspace())


# ==========================================
# CASE CHECK
# ==========================================

print("python".islower())

print("PYTHON".isupper())


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================

username = input("Enter username: ")

username = username.strip().lower()

print("Formatted username:", username)