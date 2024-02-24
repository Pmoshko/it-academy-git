def count_pairs(*args):
    y = [*args]
    m = []
    for i in range(len(y)):
        for j in range(i+1, len(y)):
            if y[i] == y[j]:
                m.append((y[i],y[j]))
    return print(len(m))

count_pairs(1, 1, 2, 3, 2, 5, 5)
