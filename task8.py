# todo: Даны переменные A, B, C. Написать код который меняет местами переменные таким образом
# чтобы значения в переменных были расположены по возрастанию
# Пример 1:
A = 10
B = 3
C = 7
# Итоговый результат должен быть:
# A = 3
# B = 7
# C = 10

# Пример 2:
A = 2
B = 10
C = 7
# Итоговый результат должен быть:
# A = 2
# B = 7
# C = 10

# Решение:
a = int(input('Введите значение числа А '))
b = int(input('Введите значение числа B '))
c = int(input('Введите значение числа C '))

if a > b > c:
    print('A =', c)
    print('B =', b)
    print('C =', a)
elif a > c > b:
    print('A =', b)
    print('B =', c)
    print('C =', a)
elif a < b < c:
    print('A =', a)
    print('B =', b)
    print('C =', c)
elif c > a > b:
    print('A =', b)
    print('B =', a)
    print('C =', c)
elif b > a > c:
    print('A =', c)
    print('B =', a)
    print('C =', b)
else:
    print('A =', a)
    print('B =', c)
    print('C =', b)
