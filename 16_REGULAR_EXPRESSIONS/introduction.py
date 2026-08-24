"""
====================================================
              REGULAR EXPRESSIONS
====================================================

Regular Expression (Regex) is a pattern used
to search, match, extract or replace text.

Python provides the 're' module for regex.

Real-life uses:

    - Email validation
    - Phone number validation
    - Password validation
    - Finding numbers in text
    - Extracting URLs
    - Searching text
    - Replacing text
"""


import re


text = "My phone number is 9876543210."


# Find a sequence of digits

result = re.findall(r"\d+", text)


print(result)


"""
Output:

['9876543210']
"""


"""
IMPORTANT:

Regex does not search only for exact text.

It can search for PATTERNS.

Example:

\d

means:

Any digit from 0 to 9.
"""