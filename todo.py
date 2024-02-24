# student = int(input())
# l = []
# for v in range(student):
#     v = int(input())
#     for z in range(v):
#         z = input()
#         l.append(z)


f = ['Russian', 'English', 'Russian', 'Belarusian', 'English', 'Russian', 'Italian', 'French']
for count, value  in enumerate(f):
    if f.count(value) == 3:
        print(len(count))

