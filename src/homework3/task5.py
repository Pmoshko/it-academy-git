def unique_elements(*args):
    a = [*args]
    b = []
    for i in a:
        if a.count(i) == 1:
            b.append(i)
    return print(b)

unique_elements(1,4,'z',1,1,4,5,6)