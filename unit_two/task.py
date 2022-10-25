# todo:Прочитать главу 6 (стр. 119) книги SQL Полное Руководство.
# Написать на модели данный ПО "Авторизации" запросы:
# 1. Простой запрос
# 2. Вычисляемый столбец
# 3. Выборка всех столбцов
# 4. Повторяющиеся строки (DISTINCT)
# 5. Отбор строк (WHERE) с оператором сравнения
# 6. Выборка одной строки
# 7. Проверка на принадлежность диапазону (BETWEEN)
# 8. Проверка наличия во множестве (IN)
# 9. Проверка на соответствие шаблону (LIKE)
# 10. Проверка на равенство NULL (is NULL)
# 11. Сопоставление условия отбора (AND, OR и NOT)
# 12. Сортировка результатов запроса (ORDER ВУ)
# 13. Объединение результов нескольких запросов (UNION)

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="auth",
    user="postgres",
    password="1234567")

cur = conn.cursor()

# 1. Простой запрос
print('1. Простой запрос')
SQL_SIMPLE_REQUEST = f"""SELECT login, password
                         FROM account"""

cur.execute(SQL_SIMPLE_REQUEST)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 2. Вычисляемый столбец
print('2. Вычисляемый столбец')
SQL_CALCULATED_COLUMN = f"""SELECT surname, salary, (salary * 1.1)
                            FROM profile"""

cur.execute(SQL_CALCULATED_COLUMN)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 3. Выборка всех столбцов
print('3. Выборка всех столбцов')
SQL_SELECTING_ALL_COLUMNS = f"""SELECT *
                            FROM profile"""

cur.execute(SQL_SELECTING_ALL_COLUMNS)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 4. Повторяющиеся строки (DISTINCT)
print('4. Повторяющиеся строки (DISTINCT)')
SQL_DISTINCT_STRINGS = f"""SELECT DISTINCT limit_of_participants
                           FROM groups"""

cur.execute(SQL_DISTINCT_STRINGS)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 5. Отбор строк (WHERE) с оператором сравнения
print('5. Отбор строк (WHERE) с оператором сравнения')

SQL_ROW_SELECTION = f"""SELECT surname
                        FROM profile
                        WHERE salary > 60000"""

cur.execute(SQL_ROW_SELECTION)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 6. Выборка одной строки
print('6. Выборка одной строки')

SQL_ONE_ROW_SELECTION = f"""SELECT surname, salary
                            FROM profile
                            WHERE id = 2"""

cur.execute(SQL_ONE_ROW_SELECTION)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 7. Проверка на принадлежность диапазону (BETWEEN)
print('7. Проверка на принадлежность диапазону (BETWEEN)')

SQL_RANGE_CHECK = f"""SELECT surname, salary
                      FROM profile
                      WHERE salary between 60000 and 70000"""

cur.execute(SQL_RANGE_CHECK)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 8. Проверка наличия во множестве (IN)
print('8. Проверка наличия во множестве (IN)')

SQL_CHECKING_FOR_PRESENCE_IN_A_SET = f"""SELECT id, surname, name, salary
                                         FROM profile
                                         WHERE id in (2,3,4,7,8)"""

cur.execute(SQL_CHECKING_FOR_PRESENCE_IN_A_SET)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 9. Проверка на соответствие шаблону (LIKE)
print('9. Проверка на соответствие шаблону (LIKE)')

SQL_CHECKING_FOR_PATTERN_MATCHING = f"""SELECT id, surname, name, salary
                                        FROM profile
                                        WHERE surname LIKE 'Бат%'"""

cur.execute(SQL_CHECKING_FOR_PATTERN_MATCHING)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 10. Проверка на равенство NULL (is NULL)
print('10. Проверка на равенство NULL (is NULL)')

SQL_CHECKING_NULL_MEANING = f"""SELECT id_profile, login, password
                                FROM account
                                WHERE is_blocked is NULL"""

cur.execute(SQL_CHECKING_NULL_MEANING)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 11. Сопоставление условия отбора (AND, OR и NOT)
print('11. Сопоставление условия отбора (AND, OR и NOT)')

SQL_SELECTION_CONDITION_MEANING = f"""SELECT id, surname, name, salary
                                      FROM profile
                                      WHERE id in (1,2,3,4,5,8,9)
                                      AND salary = 60000
                                      OR salary = 80000"""

cur.execute(SQL_SELECTION_CONDITION_MEANING)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 12. Сортировка результатов запроса (ORDER ВУ)
print('12. Сортировка результатов запроса (ORDER ВУ)')

SQL_SORTING_QUERY_RESULTS = f"""SELECT id, surname, name, salary
                                FROM profile
                                ORDER BY name, salary"""

cur.execute(SQL_SORTING_QUERY_RESULTS)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 13. Объединение результатов нескольких запросов (UNION)
print('13. Объединение результатов нескольких запросов (UNION)')

SQL_COMBINING_RESULTS_FROM_MULTIPLE_QUERIES = f"""SELECT id, surname
                                                  FROM profile
                                                  WHERE salary > 70000
                                                  UNION
                                                  SELECT id_profile, login
                                                  FROM account
                                                  WHERE id_profile in (5,6,7,8,2,3)"""

cur.execute(SQL_COMBINING_RESULTS_FROM_MULTIPLE_QUERIES)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

conn.close()



