# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения
#  кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего
# выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.

import datetime
from datetime import datetime

start = datetime.now()


def counter(func):
    def inner(*a, **kw):
        inner.count += 1
        return func(*a, **kw)

    inner.count = 0
    return inner


@counter
def render():
    pass


@counter
def show():
    pass


render()
show()
render()
render()
render()

text_1 = f"render, {str(render.count)}, {start.strftime('%d.%m.%Y %H:%M')}"
text_2 = f"show, {str(show.count)}, {start.strftime('%d.%m.%Y %H:%M')}"


def logger():
    fd = open('debug.log', mode='wt', encoding='UTF-8')
    fd.write(''.join(text_1))
    fd.write('\n')
    fd.write(''.join(text_2))
    fd.close()


logger()
