"""
====================================================
                QUIZ APPLICATION
====================================================

Concepts:

    list
    dictionary
    loops
    conditions
"""


questions = [

    {
        "question": "Which language is Python?",
        "options": [
            "A. Programming language",
            "B. Database",
            "C. Operating system",
            "D. Browser"
        ],
        "answer": "A"
    },

    {
        "question": "Which keyword defines a function?",
        "options": [
            "A. function",
            "B. def",
            "C. fun",
            "D. define"
        ],
        "answer": "B"
    },

    {
        "question": "Which data type stores key-value pairs?",
        "options": [
            "A. List",
            "B. Tuple",
            "C. Dictionary",
            "D. Set"
        ],
        "answer": "C"
    }

]


score = 0


for question in questions:

    print("\n", question["question"])


    for option in question["options"]:

        print(option)


    answer = input(
        "Enter your answer: "
    ).upper()


    if answer == question["answer"]:

        print("Correct!")

        score += 1

    else:

        print("Wrong!")


print("\nYour score:", score)

print(
    "Out of:",
    len(questions)
)