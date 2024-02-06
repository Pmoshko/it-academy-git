a = [1,2,3]
# Индексы - порядковый номер объекта в массиве (начинается с 0 с шагом +1(с лево на право))
# и с -1 с шагом -1 с право на лево
# print(a[0], a[1], a[2], a[-3])
# b = a.append(4)
# c = a.pop()
# print(a, b, c)
b = {"name": "Kirill", 1: 2}
# print(b["name"], b[1], b[-1])

# Записать фамилию в словарь(способ добавить пару ключ/значение в словарь)
b["surname"] = "Klimko"
# Таким же способом можем заменить значение по ключу
b["name"] = None
# print(b)ф
# del b["surname"]
# print(b)



# a = ["asd", 1, 1.0, 4, {1,2,3}]
# a[4] = 5
# del a[1]
# print(a)


a = ["asd", "1", "asd", "123123"]

# print(a.index(4))
# a.insert(-2, 5)
# print(a)
# a.reverse()
# a.sort()
# print(a)

# c = a.copy()
# b = a.pop(2)
# a.remove(4)
# a.clear()
# a.extend({"name": "Kirill", "surname": "Klimko"}.values())

# print(a)


# a = None
# print(bool(a))


####  ОПЕРАТОРЫ СРАВНЕНИЯ
# == - сравнивает значения двух разных объектов
# != - не равно
# >= больше или равно
# <= меньше или равно
# > - больше
# < - меньше
# a = 5
# b = 5
# print(b <= 6)

# and or not
# and - возвращает последний True или первый False
# a = 1 and 6 and 3 and 5 and []
# print(a)
# or - (Или) возвращает первый True или последний False
# a = 1 == 2 or 4 and 8 or False and 5
# print(a)
# not - (НЕ) возвращает противоположное логическое значение
# print(not 0) #print(not bool(value))
# a = ["a", "b", " ", "c"]
# b = list(input("Введи свой пароль "))# то что пишу в input - всегда на выходе строка
 # Проверки (if-elif-else) блоки

#В блоке всегда выполниться 1 дейсвие или ничего
b = 10
a = int(input("Введите число")) + 91

if a == b and a > 100:
    a = a + 91
    if a > 100:
        if type(a) == int:
            print("ВЫ угадали")
    print(1)
elif a >= b:
    print("Вы ввели число больше чем надо")
else:
    print("Вы ввели число меньше чем надо")