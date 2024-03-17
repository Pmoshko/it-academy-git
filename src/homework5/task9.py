a = 'pythonist'
dic = {}
for key in a:
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
print(dic)
