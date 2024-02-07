a = input()
b = list(a)
c = []
d = []
for i in b:
    if i.isupper():
        c.append(i)
    else:
        d.append(i)
else:
    print(f"Количество прописных букв - {len(c)} шт. строчных букв - {len(d)} шт.")

