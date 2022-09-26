#todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы. 

# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
flags_list = list()

for i in range(len(mass)):
    min_len = len(mass)

    common_num_indexes = list()
    two_closest_indexes = [0, 0]
    check_num = mass[i]
    common_num_indexes.append(i)

    if check_num not in flags_list:
        flags_list.append(check_num)
        for j in range(len(mass)):
            if check_num == mass[j] and i != j:
                common_num_indexes.append(j)

        if len(common_num_indexes) < 2:
            print(f"Для числа {check_num} нет минимального растояния, т.к элемент в массиве один.")
        else:
            for j in range(len(common_num_indexes)):
                if j != len(common_num_indexes) - 1 and min_len > common_num_indexes[j+1] - common_num_indexes[j]:
                    min_len = common_num_indexes[j+1] - common_num_indexes[j]
                    two_closest_indexes[0] = common_num_indexes[j]
                    two_closest_indexes[1] = common_num_indexes[j+1]
            print(
                f"Для числа {check_num} минимальное растояние в массиве по индексам: "
                f"{two_closest_indexes[0]} и {two_closest_indexes[1]}"
            )