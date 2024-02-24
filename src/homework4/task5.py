try:
    student = int(input('Введите количество учеников:'))
except ValueError:
    student = int(input('Епт, сказано же ввести число!!!. Еще раза, введите число учеников:'))
l = []
o = []
for v in range(student):
    try:
        v = int(input('Введите количество языков, которое знает ученик:'))
    except ValueError:
        v = int(input('Что за дела? не надо пихать туда буквы,поставь цифру:'))
    for z in range(v):
        z = input('Введите язык, который знает ученик:')
        l.append(z)
g = {}
for i in range(len(l)):
    if l[i] in g:
        g[l[i]] += 1
    else:
        g[l[i]] = 1
for k,w in g.items():
    if w == student:
        print(f'количество языков, которые знают все школьники: {w//student}')
        print(f'список таких языков:{k}')
    if w == 1:
        o.append(k)
print(f'количество языков, которые знает хотя бы один школьник: {len(o)}')
for q in range(len(o)):
    print(f'Язык, который знает хотя бы один школьник:{o[q]}')

