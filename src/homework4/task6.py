a = 'Определите, сколько  в в в в в  различных слов, слов слов слов содержится в этом тексте.'
b = a.replace(',', "")
c = b.replace('.', '')
d = c.split()
g = {}
for i in d:
    if i in g:
        g[i] += 1
    else:
        g[i] = 1
print(len(g))
