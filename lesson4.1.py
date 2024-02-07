# names = ["Kirill", "Vitya", "Kolya"]
#
# #  кол-во итераций == len(obj)
# for name in names:
#     if "i" in name:
#         print(name)
#     else:
#         print("name", name, "нет i")


# fruits = {"apple": 10, "peach": 20, "banana": 30}
# fruit = "Orange"
#
# for fruit in fruits.values():
#     print(fruit)
#
# print(fruit)

# keys_and_values = fruits.items() #[("apple", 10), ("peach", 20), ("banana", 30)]
# print(keys_and_values)
# for fruit, price in fruits.items():
#     print(fruit, price)

# portfolios = [
#     ("Kirill", 22, "python", 182, "80336656018"),
#     ("Ivan", 25, "c++", 189, "80336612312"),
#     ("Vitya", 23, "java", 160, "8033661241248"),
#     ("Kolya", 20, "html", 120, "8033665142412418"),
# ]
#
# for name, age, profession, rost, phone_number in portfolios:
#     print(name, age, profession, rost, phone_number)

# a, b, c = [1, 2, 3]
# print(a)


# range(start, stop, step) - stop(обязательный), start=0, step=1

# a = list(range(0, 10, 2))
# print(a)

# numbers = [1,10,1,000,24,42125,2151825]
#
# for i in range(len(numbers)):
#     print(numbers[i])

# enumerate - возвращает список кортежей(индекс, значение)
# a = ("asd", "asdd", "asddd", "asddddd")
# b = list(enumerate(a))
#
# print(b)
# for index, value in enumerate(a):
#     print(a[index])


# у цикла for есть else(этот блок исполняется когда цикл завершился до конца)
# for i in range(10):
#     print(i)
# else:
#     print("Я завершился")

# break - пренудительное завершение цикла
# continue - принудительный переход к следующей итерации
# a = [1,2,2,3,4,5.8,5,"asd", 10, 20, 24, 124]
# b = []
# for i in a:
#     if isinstance(i, (int, float)):
#         i += 10# i = i + 10 (//, %, *, **, -, /)
#     else:
#         continue
#     i -= 100
#     b.append(i)
# else:
#     print(f"Я список {b}, {True}, {1 + 10}")# f string

# for i in a:
#     if isinstance(i, (int, float)):# Вернет True если первый объект является типом второго аргумента
#         print(i + 10)
#     else:
#         break
# else:
#     print("Я никогда не выведусь потому что в списке есть строка")


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# itaration_1 = []
# itaration_2 = []
# c = []
# for i in a:
#     itaration_1.append(i)
#     for j in a:
#         itaration_2.append(j)

# print(len(itaration_1), len(itaration_2))


a = 1

# while a < 10:
#     if a % 2 == 0:
#         print(a)
#         a += 1
#         continue
#     a += 1
# else:
#     print("Я завершился")
# a = 1
# while True:
#     print(a)
#     a *= 100
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = [i for i in b if i % 2 == 0 or i % 3 == 0]
# a = tuple((i for i in range(10)))
# a = {k: v + 1 for k, v in enumerate(range(10)) if k % 3 == 0}
#
# a = {}
# for i, v in enumerate(range(10)):
#     if i % 3 == 0:
#         a[i] = v + 1
# print(a)

#тернарный оператор
a = "a7sd"
b = 3 if len(a) == 3 else "undefined"
print(b)



