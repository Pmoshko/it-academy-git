# когда переменную не используем дальше в  циклах используем нижнее подчеркивание вместо i(_)
# Тема урока: типы  программирования. функциональное программирование
# функция всегда что-то возврощает,  если вернуть нечего возвращает - None.
# Для  написания создания своей функции необходимо писать def
def hello_world():
    print("Hello world")
# Принцип программирования DRY (don't repeat yourself) - не повторяйся
# В python все является  объектами и построено все  на ссылках
# В python объект существует до тех пор пока к объекту есть ссылка,  если к  объекту нет ссылки то сборщик мусора удаляет его из оперативной
# памяти:
# В функциях есть return, который  указывает, что должна вернуть функция. Всегда возвращает один объект. Функция занчивает свою работу на работу return.
# Слайсирование
# *args - неограниченное количество позиционных  аргументов,  *kwargs - неограниченно количество име тннованных аргументов.