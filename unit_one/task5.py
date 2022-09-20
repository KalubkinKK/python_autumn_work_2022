# todo: Написать программу, которая считывает два числа и выводит их сумму, разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком, результат возведения в степень.

num_one = int(input('Введите первое число '))
num_two = int(input('Введите второе число '))

nums_sum = num_one + num_two
print('Сумма чисел равна: ', nums_sum)

nums_diff = num_one - num_two
print('Разность чисел равна: ', nums_diff)

nums_div = num_one / num_two
print('Частное чисел равно: ', nums_div)

nums_mult = num_one * num_two
print('Произведение чисел равно: ', nums_mult)

nums_int_div = num_one // num_two
print('Реультат целочисленного деления чисел равен: ', nums_int_div)

nums_div_marg = num_one % num_two
print('Реультат деления чисел с остатком равно: ', nums_div_marg)

nums_raising = num_one ** num_two
print('Реультат возведения первого числа в степень второго равен: ', nums_raising)
