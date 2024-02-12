a = [(i+j) for i in 'abcd' for j in 'abcd' if (i == 'a' or i == 'b') and j != 'a']
print(a[:5:2])


a = [str(i) + 'a' for i in range(1,5)]
print(a.pop(1))
print(a)

b = a.copy()
b.insert(1,'2a')
print(b)
