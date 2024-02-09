def FizzBuzz(a,b):
    x = list(range(a, b))
    z = []
    for i in x:
        if i % 3 == 0 and i % 5 == 0:
            i = "FizzBuzz"
            z.append(i)
        elif i % 5 == 0:
            i = "Buzz"
            z.append(i)
        elif i % 3 == 0:
            i = "Fizz"
            z.append(i)
        else:
            i = i
            z.append(i)
    else:
        print(z)

# FizzBuzz(100,1000)
