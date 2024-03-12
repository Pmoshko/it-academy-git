# class Person():
#     def __init__(self, name, surname, age, place_of_birth):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.place_of_birth = place_of_birth
#     def get_age(self, year):
#         print(year - self.age)
#
# p1 = Person("Pavel", "Moshko", 1990, "Republic of Belarus")
# p2 = Person("Oksana", "Marchenko", 1990, "Republic of Belarus")
# p3 = Person("Nikita", "Moshko", 2018, "Republic of Belarus")
# p4 = Person("Zlata", "Moshko", 1990, "Republic of Belarus")
#
# p2.get_age(2024)
# print(p1.name, p2.name, p3.name, p4.name)
#
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_pirimetre(self):
#         return self.radius * 2 * 3.14
#     def get_area(self):
#         return 3.14 * self.radius ** 2
#
# c1 = Circle(3)
# print(c1.get_pirimetre())
# print(c1.get_area())
#
# c2 = Circle(7)
# print(c2.get_pirimetre())
# print(c2.get_area())

def decator(func):
    def inner(*args, **kwargs):
        print('start decorator ....')
        func(*args, **kwargs)
        print('finish decorator ....')
    return inner


def say(name, surname, age):
    print('hello', name, surname, age)

say = decator(say)
say('Vasya', 'Ivanov', 30)

