# todo: Дан массив размера N. Найти минимальное растояние между одинаковыми значениями в массиве и вывести их индексы.

"Пример:"
mass = [1, 2, 17, 54, 30, 89, 2, 1, 6, 2]
# mass = [1, 1, 4, 6, 7, 6, 4, 3, 7, 4, 15, 1, 3, 1]
"Для числа 1 минимальное растояние в массиве по индексам: 0 и 7"
"Для числа 2 минимальное растояние в массиве по индексам: 6 и 9"
"Для числа 17 нет минимального растояния т.к элемент в массиве один."

flags_list = list()
# Этот список нужен для того (флаговый список), чтобы не повторялись выводы для чисел по три раза, то есть
# Чтобы не было три одинаковых вывода для 2, мол,
# минимальное расстояние 6 9... минимальное расстояние 6 9... минимальное расстояние 6 9... и т.д.

for i in range(len(mass)):  # ЦИКЛ ДЛЯ СРАВНЕНИЯ КАЖДОГО ЧИСЛА ИЗ СПИСКА СО ВСЕМИ ДРУГИМИ ЧИСЛАМИ
    min_len = len(mass)
    # Чтобы найти минимальное значение, мы переприсваеваем переменной min_len значение,
    # в сравнении с которым min_len больше
    # Что-то вроде: я 10, если я больше 5, то я тоже стану 5 (так думает переменная min_len)
    common_num_indexes = list()
    two_closest_indexes = [0, 0]
    check_num = mass[i]
    common_num_indexes.append(i)

    if check_num not in flags_list:
        flags_list.append(check_num)
        for j in range(len(mass)):
            # print(f"i - {i}, j - {j}")
            if check_num == mass[j] and i != j:
                common_num_indexes.append(j)

        if len(common_num_indexes) < 2:
            print(f"Для числа {check_num} нет минимального растояния т.к элемент в массиве один.")
        else:
            for j in range(len(common_num_indexes)):
                if j + 1 != len(common_num_indexes) and min_len > common_num_indexes[j+1] - common_num_indexes[j]:
                    print(common_num_indexes[j+1] - common_num_indexes[j])
                    min_len = common_num_indexes[j+1] - common_num_indexes[j]
                    two_closest_indexes[0] = common_num_indexes[j]
                    two_closest_indexes[1] = common_num_indexes[j+1]
            print(
                f"Для числа {check_num} минимальное растояние в массиве по индексам: "
                f"{two_closest_indexes[0]} и {two_closest_indexes[1]}")
