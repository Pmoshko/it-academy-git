import math
print('Расчет площади треугольника')
a = int(input('Введите сторону треугольника Х:'))
b = int(input('Введите сторону треугольника Y:'))
c = int(input('Введите сторону треугольника Z:'))
if a+b>c and b+c>a and a+c>b:
    p = (a+b+c) / 2
    print('Площадь треугольника:', math.sqrt(p * (p - a) * (p - b) * (p - c)))
else:
    print('Неверные данные')