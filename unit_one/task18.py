# todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
# и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.
#
# Пример вывода:
# Сумма 2   комбинация [(1,1)]
# Сумма 3   комбинация [(1,2),(2,1)]
# Сумма 4   комбинация [(1,3),(3,1),(2,2)]
# ........................................
# Выводы комбинаций оформить в список кортежей.
mass_num = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
summ_list = []
x = 0
y = 0


def points_count():
    result_list = list()
    for i in mass_num:
        some_list = list()
        for j in range(1, i + 1):
            first_dice = i - j
            second_dice = j
            if 0 < first_dice < 7 and 0 < second_dice < 7:
                pairs_tuple = (first_dice, second_dice)
                some_list.append(pairs_tuple)
                # print(f"x: {first_dice} y: {second_dice} || i: {i} j: {j}")
        result_list.append(some_list)
    return result_list


print(points_count())
output = points_count()
for i_sum in range(len(output)):
    print(f"Сумма {i_sum + 2}   комбинация {output[i_sum]}")
