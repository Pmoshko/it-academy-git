a = input()
b = list(a)
c = []
d = []
for i in b:
    if ord(i) in range(65, 91) :
        c.append(i)
    if ord(i) in range(97, 123):
        d.append(i)
    else:
        continue
else:
    print(f"Количество прописных букв - {len(c)} шт. строчных букв - {len(d)} шт.")

