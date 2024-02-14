a = ['a', 'b', 'c']
print(tuple(a))

b = ('a', 'b', 'c')
print(list(b))

a, b, c = 'a', int(2), 'python'
print(c)

x = ("123",)
for i in x:
    for j in i:
        print(j)
print(f"Длина исходного кортежа  - {len(x)}")