# БД «ГАИ»
# Описание предметной области. БД создается для информационного обслуживания работников ГАИ.
# В БД находятся автомобили, зарегистрированные по данному адресу. Некоторые из них угнаны.
# Готовые запросы:
# 1. Выдавать информацию об автомобиле по его регистрационному знаку (марка, цвет, модель и т.д.);
# 2. Выдавать информацию об автовладельце по регистрационному знаку данного автомобиля.
# 3. Выдавать информацию об автомобиле (прошлые автовладельцы, аварии и т.д.) по номеру двигателя;
# 4. Выдавать список угнанных автомобилей;
# 5. Выдавать список автомобилей, попавших в аварию в данный период
# времени;
# 6. Выдавать список наиболее угоняемых автомобилей по марке.

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="course",
    user="postgres",
    password="1234567")

# Open a cursor to perform database operations
cur = conn.cursor()

# 1. Выдавать информацию об автомобиле по его регистрационному знаку (марка, цвет, модель и т.д.).
print('Вывод информации об автомобиле по регистрационному знаку.')
print()

# Execute a query
registration_number = input('Введите регистрационный номер: ')

SQL_GET_INFO_ABOUT_CAR_BY_REG_NUMBER = f"""SELECT *
                                           FROM auto
                                           WHERE reg_number = '{registration_number}'"""

cur.execute(SQL_GET_INFO_ABOUT_CAR_BY_REG_NUMBER)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 2. Выдавать информацию об автовладельце по регистрационному знаку данного автомобиля.
print('Вывод информации об автовладельце по регистрационному знаку автомобиля.')
print()

# Execute a query
registration_number = input('Введите регистрационный номер: ')

SQL_GET_INFO_ABOUT_DRIVER_BY_REG_NUMBER = f"""SELECT d.name, d.surname, d. bd, d. dt_buy, d. dt_sell
                                              FROM driver d, auto a
                                              WHERE a. reg_number = '{registration_number}'"""

cur.execute(SQL_GET_INFO_ABOUT_DRIVER_BY_REG_NUMBER)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 3. Выдавать информацию об автомобиле (прошлые автовладельцы, аварии и т.д.) по номеру двигателя.
print('Вывод информации об автомобиле по номеру двигателя.')
print()

# Execute a query
engine_number = input('Введите номер двигателя: ')

SQL_GET_INFO_ABOUT_AUTO_BY_ENG_NUMBER = f"""SELECT d.name, d.surname, d. bd, a. car_accident, a. accident_date
                                            FROM driver d, auto a
                                            WHERE a. eng_number = '{engine_number}'"""

cur.execute(SQL_GET_INFO_ABOUT_AUTO_BY_ENG_NUMBER)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 4. Выдавать список угнанных автомобилей.
print('Список угнанных автомобилей: ')
print()

SQL_GET_INFO_ABOUT_STILLED_CARS = f"""SELECT *
                                      FROM auto
                                      WHERE hijacking is true"""

cur.execute(SQL_GET_INFO_ABOUT_STILLED_CARS)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 5. Выдавать список автомобилей, попавших в аварию в данный период времени.
print('Вывод списка автомобилей, попавших в аварию в данный период времени.')
print()

accident_date_from = input('Введите дату с: ')
accident_date_by = input('Введите дату по: ')

SQL_GET_INFO_ABOUT_CARS_WHICH_HAD_ACCIDENT_IN_CHOSEN_TIME = f"""SELECT *
                                                                FROM auto
                                                                WHERE accident_date BETWEEN '{accident_date_from}' 
                                                                AND '{accident_date_by}'"""

cur.execute(SQL_GET_INFO_ABOUT_CARS_WHICH_HAD_ACCIDENT_IN_CHOSEN_TIME)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

# 5. Выдавать список наиболее угоняемых автомобилей по марке.
print('Вывод наиболее угоняемых автомобилей по марке.')
print()

car_brand = input('Введите марку автомобиля: ')

SQL_GET_INFO_ABOUT_MOST_STILLED_CARS_BY_BRAND = f"""SELECT model, count(car_accident)
                                                    FROM auto
                                                    WHERE brand = '{car_brand}'
                                                    GROUP BY model
                                                    ORDER BY count DESC"""

cur.execute(SQL_GET_INFO_ABOUT_MOST_STILLED_CARS_BY_BRAND)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

print()

conn.close()
