def biggest_dict(**kwargs):
    my_dict = {'first_one': 'we can do it.'}
    for k,v in kwargs.items():
         my_dict.update(**kwargs)
    return print(my_dict)

biggest_dict(a = 10, b = 100, c = 1000)