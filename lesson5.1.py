# a = ["Kirill" + str(i) for i in range(10)]
#
# print(a)

# a = [i for i in range(100) for j in range(i)]
#
# b = []
# for i in range(100):
#     for j in range(i):
#         b.append(i)
#
# a = 1 if input() != "asd" else 2 if input("asd") == "asd" else 5

# if input() != "asd":
#     a = 1
# else:
#     if input("asd") == "asd":
#         a = 2
#     else: a = 5

# Создание функции через def
# def hello_world():
#     return range(100)
#
# *a,v,b,c = hello_world()# *в присваивании - распаковка оставшихся объектов итерируемого объекта
#
# print(a, v, b, c)


# REFERENCES
# a = [1,2,3]
# b = a
# c = id(b)
# del a
# del b
# v = [1,2,3,4]
# print(c == id(v))
# print(id(a) == id(b))

# a = [1,2,3]
# print(id(a[0]) == id(1))



# a = "1,2,3,4,5,6,7,8,9,10"
# print(a[2:5:1])# slice [SSS] all are optional


# def sum_two_numbers(number_1, number_2): #Позиционные аргументы
#     return number_1 + number_2
#
# print(sum_two_numbers(10, 20))# Передал их по позиции
# print(sum_two_numbers(number_1=10, number_2=20))


# def sum_two_numbers(number_1, number_2=10):#Аргументы по позиции
#     return number_1 + number_2
#
#
# print(sum_two_numbers(20))# Передал 1 по позиции
# print(sum_two_numbers(100, 200))# Передал их по позиции
# print(sum_two_numbers(number_2=200, number_1=100))


len
# *args (tuple) - неограниченное количество позиционных аргументов:
# **kwargs (dict) - неограниченное кол-во именнованных аргументов
# Позиционные аргументы от именованных разделяет *args
# def a(i, v, j=20, *pos, h=10, b, **name):
#     print(pos, name, i, v, j, h, b)
#
# a(1,2,3,4,5,6,7,"asd", b=10, c=20, p=30, h=20)
# a(1,2,3,4,5,6,7,"asd", b=10, c=20, p=30, h=20)
# a(1,2,3,4,5,6,7,"asd", b=10, c=20, p=30, h=20)
# a(1,2,3,4,5,6,7,"asd", b=10, c=20, p=30, h=20)


# def sum_numbers(count, *args):
#     if count == 0:
#         return None
#     b = 0
#     for i in range(count):
#         b += args[i]
#     return b
#
# print(sum_numbers(4, 1,2,3,4,5,6,7))# -> 10
# print(sum_numbers(2, 100, 200, 300, 1000))# -> 300
# print(sum_numbers(1, 100, 200, 300))# -> 100
# print(sum_numbers(0, 100, 200, 300))# -> None
# print(sum_numbers(10, *range(100)))# -> 45


def roman_to_int(roman_number):
    pass

roman_to_int("III")# 3
roman_to_int("LVIII")# 58
roman_to_int("MCMXCIV")# 1994