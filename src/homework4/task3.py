a = [1, 2, 1, 5, 6, 5, 4, 3, 2, 1]
b = [6, 5, 9, 5, 6, 5, 4, 5, 8, 1]
c = a + b
x = {}
for i in c:
    if i in x:
        x[i] +=1
    else:
        x[i] = 1
print(len(x))


