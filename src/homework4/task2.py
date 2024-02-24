def countries(*args, **kwargs):
    c = int(input('Введите количество стран:'))
    g = {}
    for i in range(1, c + 1):
        i = input('Введите страну, а затем города этой страны:')
        i = i.split()
        for j in range(1, len(i)):
            g[i[j]] = i[0]
    d = int(input('Введите количество городов, которые хотите проверить:'))
    p = []
    for m in range(1, d + 1):
        m = input('введите город который хотите проверить:')
        p.append(m)
    for x in p:
        print(g.get(x))
    return













