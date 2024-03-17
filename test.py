from datetime import datetime, date

class Staff():

    number_of_staff = 0
    def __init__(self, surname: str, name: str, age: date, position: str):
        self.surname = surname
        self.name = name
        self.age = date
        self.position = position
        Staff.number_of_staff = Staff.number_of_staff + 1

    @classmethod
    def total_object(cls):
        print(f"Total number of stuff:{ cls.number_of_staff}")

    @classmethod
    def name(cls):
        print(cls.__name__)

p1 = Staff('Mashko', 'Pavel', 1990, 'boss')
Staff.total_object()
Staff.name()