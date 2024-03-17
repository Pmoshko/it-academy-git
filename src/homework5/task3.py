def count_it(c):
    c = c.split(", ")
    g = {int(i) : c.count(i) for i in c}
    sort = sorted(g.items(), key=lambda element: element[1])
    return print(sort[-3:])


count_it('1, 2, 3, 3, 4, 1, 2, 1, 5, 4, 4, 5, 1, 6, 4, 7, 8, 9, 1')

