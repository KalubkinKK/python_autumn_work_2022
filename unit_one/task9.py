# todo: Решить линейное уравнение A·x + B = 0, заданное своими коэффициентами A и B (коэффициент A не равен 0).
# Примечание: коэффициенты получаем через функцию input().

a = int(input('Введите значение переменной A '))
b = int(input('Введите значение переменной B '))
x = 0
if a != 0:
    x = -b / a
    print(x)
else:
    print('Переменная A не должна быть равно нулю!')
