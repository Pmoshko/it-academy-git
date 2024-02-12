y = [1, 3, 1, 4, 1, 5, 1, 3]
pairs = []
for i in range(len(y)):
    for j in range(i+1, len(y)):
        if y[i] == y[j]:
            pairs.append((y[i], y[j]))
pair_count = len(pairs)
print(pairs)
