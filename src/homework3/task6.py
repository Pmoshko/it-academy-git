def null_list(*args):
    l = [*args]
    for i in reversed(range(len(l))):
        if l[i] == 0:
            l.append(l.pop(i))
    return print(l)

null_list(1, 0, 2, 0, 4, 5, 0, 6, 0, 0, 1, 1, 2)
