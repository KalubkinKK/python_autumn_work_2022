# todo 1: Для игры "Морской бой" файл sea_battle.py написать создание игрового поля nxn

# todo 2: В игровой матрице nxn найти кол-во всех 1

#  Задачи решить через генераторы списков (списковые включения)

from random import randint as rdi

game_field = []
i = 0


def matrix():
    global game_field
    n = int(input("Введите количество ячеек по горизонтали: "))
    m = int(input("Введите количество ячеек по вертикали: "))
    game_field = [[rdi(0, 1) for _ in range(n)] for _ in range(m)]


def matrix_sum():
    global game_field
    matrix()
    res = sum([x for game_field in game_field for x in game_field])
    print(game_field)
    print("Сумма всех единиц равна: ", res)


matrix_sum()
