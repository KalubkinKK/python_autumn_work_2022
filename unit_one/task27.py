from random import randint as rdi

game_field = []
LIVE = 1
access = [10, 20, 30]
import sys


def init():
    matrix()


def decor_access(func_menu):
    id = int(input('Введите ID: '))

    def wrapper():
        global access
        if id not in access:
            sys.exit('Нет доступа')
        else:
            func_menu()

    return wrapper


@decor_access
def menu():
    out = f"1. Новая игра\n2. Продолжить игру\n3. Сохранить игру\n4.Загрузить игру"
    print(out)
    num = int(input("Раздел: "))
    if num == 1:
        init()
        game()
    else:
        sys.exit(0)


def get_row(number_of_count=5):
    row = []
    func = lambda: rdi(0, 1)
    for i in range(number_of_count):
        row.append(func)
    result = []
    for l in row:
        result.append(l())
    return result


def matrix(amount_row=5):
    global game_field
    for i in range(amount_row):
        game_field.append(get_row())
    return game_field


def get_position():
    long = input("Введите координату x:")
    lot = input("Введите координату y:")
    return (int(long), int(lot))


def minus_live():
    global LIVE
    LIVE -= 1


def game():
    global game_field

    while LIVE:
        i, j = get_position()
        if game_field[i][j] == 1:
            game_field[i][j] = -1
            print("Попал")
        else:
            minus_live()
    else:
        print("Ваша песенка спета!")


menu()
