# Надо посмотреть конструкцию from
# Надо посмотреть конструкцию from as
# pip -  посмотреть  что такое pip
# poetry  - посмотреть
# создание пакетов,  посмотреть как  используется
# if __name__ == '__main__'
# Сериализация - преобразовать python объект к чему-то,  десериализация - обратный  процесс.
# import json
#
#
# a = {1:"1", 2:"2"}
# print(json.dumps(a))
#
# b = json.dumps(a) сериализация в json
# с =  json.loads(b) десирилизацяи из json
import json

# print(c)

# import pickle
#
# a = 'adsadasa'
# b = pickle.dumps(a)
# print(b)
# bytes - не изменяемый  and bytearray изменяемый


# f = open("test_file.txt","w")
# f.write("sd\nlkfjs\tlkfkls")
# f.close()

# Контекстный менеджер (инструкция with) -  это инструкция, которая релизует метод __enter__ и __exit__

# f = open("test_file.txt", "r")
# print(dir(f))

# with open("test_file.txt", "w") as file:
#     file.write("asd")
# import json
# #
# # with open("test_file.json", "w") as file:
# #     json.dump({"1": 1}, file)
# #
# # with open("test_file.json", "r") as file:
# #     a = json.load(file)
# #     print(a)

# Возбуждение ошибок и обработка ошибок
# raise Error - возбуждает ошибку
# a = int(input("Введите число до 10"))
# if a > 10:
#     raise ValueError("Вы ввели число больше 10")
# Traceback - последовательность действий,  которая  привела к  ошибке
# Конструкция обработки ошибок Try except finally else
# try:
#     raise TypeError("asdasfsdfsdfsdfds")
# except (TypeError, ValueError) as err:
#     print(f"была ошибка {err}")
# # несколько ошибок  можно обрабатывать,  если они записаны в  кортеж.
# try:
#     a = 10
# except ValueError as err:
#     print(f"была ошибка {err}")
# except TypeError as err:
#     print(f"другая обработка ошибки {err}")
# else:
#     print('Я else')
# finally:
#     print('Я finally')
# Try - может  быть только один
# Except - может  быть несколько
# Else,Finaly -  могут быть только одни т они опциональные
# try без except может существовать только в конструкции  с finally.
# try:
#     f = open("asd.txt", "w")
# finally:
#     f.close()
# Перед тем как делать дз - создаем ветку,  потом пушим  эту  ветку в репозиторий,  в  репозитории сделать пул реквест, и назначить ревуером.