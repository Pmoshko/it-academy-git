a = ['a', 1, 2, 'b', 2, 'a', 5, 9]
b = []
for i in a:
    if a.count(i) == 1:
        b.append(i)
print(b)


