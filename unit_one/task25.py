# #todo: Убрать повторяющиеся буквы и лишние символы
# Построить по ключевой фразе часть алфавита. Взять все буквы по одному разу. Не буквы убрать.
# Буквы должны идти в том порядке, в котором встретились во фразе в первый раз.
#
# Input             	            Output
#
# apple	                        aple
# 25.04.2022 Good morning !!	    godmrni

text = input('Введите строку: ')
output = ''

text = text.lower()

for letter in text:
    if letter.isalpha():
        if text.count(letter) < 2:
            output += ''.join(letter)
        else:
            if letter in output:
                continue
            else:
                output += ''.join(letter)
    else:
        continue

print(output)
