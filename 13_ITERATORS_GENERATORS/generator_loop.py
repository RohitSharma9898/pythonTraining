"""
GENERATOR WITH FOR LOOP
"""


def numbers():

    for number in range(1, 6):

        yield number


for number in numbers():

    print(number)