# todo: Найти сумму элементов матрицы
# Написать функцию msum(matrix)  которая подсчитывает сумму всех элементов матрицы:
# Задачу решить с помощью генераторов.

# >>> matrix = [[1, 2, 3], [4, 5, 6]]
# >>> msum(matrix)
# 21


def msum(matrix):
    counter = [sum(num) for num in matrix]
    counter = sum(counter)
    print(counter)


msum([[1, 2, 3], [4, 5, 6]])
