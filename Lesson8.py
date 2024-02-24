# Основные  приницпы программирования KISS, YAGNI, DRY
# Два основных  направления в PYthon Функциональное и ООП - объектно ориентированное программирование.
# Построенно на классах
# 3 основных  и 1 дополнительный принцип
# Инкапсуляция
# Полиморфизм
# Наследование
# Абстракция
# Определяем класс через class
# 2 типа определения переменных snake_case(other) CamelCase(class)
# У класса есть атрибуты
# У класса  есть методы
#  Строгий порядок вначале идут атрибуты а  затем методы
#  Dnder Methods  - это методы, которые позволяют менять поведения объектов. Можем переодпределить или  написать новые.
# анотация типов  == типизация
# Билиотека import typing
# Инкапсуляция - это договоренность разработчиков  о сокрытии данных. Есть 3 типов:
# 1. public -  можно использовать везде
# 2. protected начинается с  нижнего подчеркивания использовать только в классе и наследниках
# 3. private -  используется только в пределе  класса и начинается с двух нижних подчеркивания (__)

# class MyFirstClass():
#     a = 10
#
#     def __init__(self, a: int, b: str, c: int = 10 ) -> None:
#         self.a = a # public
#         self._b = b # protected
#         self.__c = c # private
#
#     def get_a_x10(self) -> list[int]:
#         return [i for i in range(10)]
#
#     def __eq__(self, other):
#         if isinstance(other, int):
#             return self.a == other
#         raise ValueError("I cannot compare with")
#
#     def __gt__(self, other):
#         if isinstance(other, int):
#             return self.a > other
#         raise ValueError(f"I cannot compare with {type(other)}")
#
#     def __ge__(self, other):
#         if isinstance(other, int):
#             return self.a >= other
#         raise ValueError(f"I cannot compare with {type(other)}")
#
#     def __len__(self):
#         return self.b
#
#
#
#
# my_first_instance = MyFirstClass(10, "asd")  # экземпляр класса
# my_second_instance = MyFirstClass(20, "asldkald")
# # my_second_instance.a = 20
# # print(my_second_instance.get_a_x10())
# # print(my_first_instance.get_a_x10())
# # print(my_second_instance == 20)
# # print(my_second_instance == 20)
# # print(my_second_instance > 40)
# # a = my_first_instance.get_a_x10()
# # print(a.count(1))
# print(my_first_instance.a)
# print(my_first_instance._b)
# # print(my_first_instance.__c) #_MyFirstClass__c
# print(my_first_instance._MyFirstClass__c)
# Полиморфизм - это возможность обработки разных типов данных, т. е. принадлежащих к разным классам, с помощью "одной и той же" функции, или метода.
#Наследование  -  способ принятия атрибутов и методов у родительского класса. Класс В  -  дочерний
class A:
    a = 10

class B(A): # наследую все  атрибутты и методы класс А
    pass

b = B()
print(b.a)
# MRO - Method Resolution Order __mro__ -  порядок наследования. Чтобы  посмотреть (print(B.__mro__)/
# Не явно все  классы  наследуются от object
