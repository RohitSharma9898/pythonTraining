"""
====================================================
                  DATAFRAME
====================================================

A DataFrame is a two-dimensional table.

Think of it like an Excel spreadsheet.

Rows    -> Records
Columns -> Fields
"""


import pandas as pd


data = {

    "Name": [
        "Rohit",
        "Rahul",
        "Aman"
    ],

    "Marks": [
        85,
        90,
        75
    ],

    "City": [
        "Vadodara",
        "Delhi",
        "Mumbai"
    ]
}


df = pd.DataFrame(data)


print(df) 