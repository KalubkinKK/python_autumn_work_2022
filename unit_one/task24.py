# todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!

alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print('Input\t\t\t\t\t\t\t\t', 'Output')

num_sting_one = 8, 5, 12, 12, 15
num_sting_two = 8, 5, 12, 12, 15, ',', 0, 23, 15, 18, 12, 4

print(*num_sting_one, end='\t\t\t\t\t\t')

for i in num_sting_one:
    for j in range(len(alphabet)):
        if i == j:
            i = alphabet[j]
            print(i, end='')
print()
print(*num_sting_two, end='\t\t')

for i in num_sting_two:
    for j in range(len(alphabet)):
        if i == j:
            i = alphabet[j]
            print(i, end='')
        elif i == ',':
            print(i, end='')
            break
