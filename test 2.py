# def isPalindrome(n1 = int):
#     digit = n1 % 10
#     n2 = digit
#     n1 = n1 // 10
#     while n1 > 0:
#         digit = n1 % 10
#         n1 = n1 // 10
#         n2 = n2 * 10
#         n2 = n2 + digit
#
#
#
# isPalindrome(1243234)
#
# def plusOne(a = []):
#     b = ("".join(map(str,a)))
#     c = int(b) + 1
#     print(c)
# plusOne()


student = int(input())
l = []
for v in range(student):
  v = int(input())
    for z in range(1, v +1):
        z = input()
        l.append(z)
for w in range(len(l)):
    if l.count(l[w]) == student:
        print(l[w])
    if l.count(l[w]) == 1:
        print(l[w])


    # h = {}
    # for g in range(len(l)):
    #     if l[g] in h:
    #         h[l[g]] += 1
    #     else:
    #         h[l[g]] = 1
    # for k, v in h.values():
    #     if h.values() : 1:
    #         print(k)

# r = []
# for w in range(len(l)):
#     if l.count(l[w]) == student:
#         print(l.count(l[w]) // student)
#         r.append(l[w])
#         print(l[w])
#         print(len(set(r)))
#     if l.count(l[w]) == 1:
#         print(l[w])