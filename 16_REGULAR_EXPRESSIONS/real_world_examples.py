"""
====================================================
             REAL-WORLD REGEX EXAMPLES
====================================================
"""


import re


# ==================================================
# 1. EXTRACT ALL NUMBERS
# ==================================================

text = """
Rohit scored 85 marks.
Rahul scored 92 marks.
Aman scored 78 marks.
"""


marks = re.findall(r"\d+", text)


print("Marks:", marks)


# ==================================================
# 2. EXTRACT EMAILS
# ==================================================

text = """
Contact:
rohit@gmail.com
rahul@yahoo.com
admin@company.com
"""


emails = re.findall(
    r"[\w.-]+@[\w.-]+\.\w+",
    text
)


print("Emails:", emails)


# ==================================================
# 3. EXTRACT PHONE NUMBERS
# ==================================================

text = """
Call 9876543210 or 8765432109.
"""


phones = re.findall(
    r"\b[6-9]\d{9}\b",
    text
)


print("Phone numbers:", phones)


# ==================================================
# 4. REMOVE EXTRA SPACES
# ==================================================

text = "Python    is     very     easy"


clean_text = re.sub(
    r"\s+",
    " ",
    text
)


print(clean_text)


# ==================================================
# 5. HIDE PHONE NUMBER
# ==================================================

phone = "9876543210"


hidden_phone = re.sub(
    r"\d(?=\d{4})",
    "*",
    phone
)


print(hidden_phone)