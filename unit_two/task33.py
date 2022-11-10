# todo: Реализовать собственный класс исключений, которые будут вызываться (бросаться) в случае:
#  1. пользователь ввел некорректное значение в заданном диапазоне
#  2. результат запроса вернул 0 строк
#  3. Произошел разрыв соединения с сервером

import psycopg2


#  1. пользователь ввел некорректное значение в заданном диапазоне


class ResultIsNotCorrect(Exception):

    def __init__(self, number):
        super().__init__(f"Значение переменной {number} находится за пределами заданного диапазона")
        self.number = number


try:
    val = int(input('Введите значение в интервале от 1 до 100: '))
    if val not in range(1, 101):
        raise ResultIsNotCorrect(val)
except ResultIsNotCorrect as e:
    print(e)

print()

# 2. результат запроса вернул 0 строк


conn = psycopg2.connect(
    host="localhost",
    database="auth",
    user="postgres",
    password="1234567")

cur = conn.cursor()


class EmptyString(Exception):

    def __init__(self):
        super().__init__()


salary_val = int(input('Введите верхнее значение заработной платы: '))

try:
    SQL_ROW_SELECTION = f"""SELECT surname
                            FROM profile
                            WHERE salary < {salary_val}"""

    cur.execute(SQL_ROW_SELECTION)
    records = cur.fetchall()
    if not records:
        raise EmptyString()

except EmptyString as e:
    print(e, end='')
    print('Пользователи с указанным порогом заработной платы не найдены.')
else:
    for row in records:
        print(row)

finally:
    print()


# 3. Произошел разрыв соединения с сервером

class ConnectionIsApart(Exception):
    def __init__(self):
        super().__init__()

    cur = conn.cursor()


try:
    conn = psycopg2.connect(
        host="localhost",
        database="auth",
        user="postgres",
        password="1234567")

except ConnectionIsApart as e:
    print(e, end='')
    print('Произошел разрыв соединения с сервером.')

else:
    print('Соединение установлено:', conn)

finally:
    print()

    conn.close()
