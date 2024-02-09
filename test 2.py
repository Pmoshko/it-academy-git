a = list(range(1,101))
b =[list(range(100))]
c = []
for i in a:
    if i % 3 == 0 and i % 5 == 0 :
        i = "FizzBuzz"
        c.append(i)
    elif i % 5 == 0:
        i = "Fizz"
        c.append(i)
    elif i % 3 == 0:
        i = "Buzz"
        c.append(i)
    else:
        i = i
        c.append(i)
else:
    print(c)

