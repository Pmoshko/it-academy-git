a = [1, 2, 1, 5, 6, 5, 4, 3, 2, 1]
b = [8, 5, 5, 5, 8, 5, 4, 5, 8, 1]
c = {}
x = {}
for i in a:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
for j in b:
    if j in x:
        x[j] += 1
    else:
        x[j] = 1
print(len(x), len(c))