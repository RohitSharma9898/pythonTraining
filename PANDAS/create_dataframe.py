"""
====================================================
            DIFFERENT WAYS TO CREATE
                  DATAFRAME
====================================================
"""


import pandas as pd


# ==================================================
# FROM DICTIONARY
# ==================================================

data = {

    "Name": ["Rohit", "Rahul", "Aman"],

    "Marks": [85, 90, 75]
}


df = pd.DataFrame(data)


print(df)


# ==================================================
# FROM LIST OF DICTIONARIES
# ==================================================

students = [

    {
        "Name": "Rohit",
        "Marks": 85
    },

    {
        "Name": "Rahul",
        "Marks": 90
    },

    {
        "Name": "Aman",
        "Marks": 75
    }
]


df = pd.DataFrame(students)


print(df)