y = [1, 3, 1, 4, 1, 5]
m = []
for i in range(len(y)):
    for j in range(i+1, len(y)):
        if y[i] == y[j]:
            m.append((y[i],y[j]))
print(len(m))
