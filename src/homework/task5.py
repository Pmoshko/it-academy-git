a = 1
b = a

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n) - 2

while n > 0:
    a, b = b, a + b
    n -= 1

print("Значение этого элемента:", b)