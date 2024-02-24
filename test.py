# nums = [2, 7, 11, 15]
# t = 9
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == t:
#             print([i],[j])

# nums = [2, 7, 11, 15]
# t = 9
# for i in range(len(nums)):
#     if nums[i] + nums[i+1] == t:
#         print([i],[i+1])
#
# f = 123321
# d = []
# for i in range(f):
#     d.append(i)
#     print(len(d))




# def countries(*args, **kwargs):
#     c = int(input())
#     g = {}
#     for i in range(1, c + 1):
#         i = input()
#         i = i.split()
#         for j in range(1, len(i)):
#             g[i[j]] = i[0]
#     d = int(input())
#     p = []
#     for m in range(1, d + 1):
#         m = input()
#         p.append(m)
#     for x in p:
#         print(g.get(x))
# countries(2,3)

# a = {i:i**3 for i in range(1,21)}
# print(a)

# a = [1, 2, 1, 5, 6, 5, 4, 3, 2, 1]
# b = [6, 5, 9, 5, 6, 5, 4, 5, 8, 1]
# c = a + b
# x = {}
# for i in c:
#     if i in x:
#         x[i] +=1
#     else:
#         x[i] = 1
# print(len(x))

# a = [1, 2, 1, 5, 6, 5, 4, 3, 2, 1]
# b = [8, 5, 5, 5, 8, 5, 4, 5, 8, 1]
# c = {}
# x = {}
# for i in a:
#     if i in c:
#         c[i] += 1
#     else:
#         c[i] = 1
# for j in b:
#     if j in x:
#         x[j] += 1
#     else:
#         x[j] = 1
# print(len(x), len(c))


