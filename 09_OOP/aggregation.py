"""
AGGREGATION

Aggregation is also a HAS-A relationship.

The contained object can exist
independently of the container.
"""


class Teacher:

    def __init__(self, name):

        self.name = name


class Department:

    def __init__(self, teacher):

        self.teacher = teacher

    def show_teacher(self):

        print("Teacher:", self.teacher.name)


teacher = Teacher("Rohit")

department = Department(teacher)

department.show_teacher()