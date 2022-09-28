# todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.

# Написать игру "Поле чудес"

# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
words = ["оператор", "конструкция", "объект"]
desc_ = ["Это слово обозначает наименьшую автономную часть языка программирования", "..", ".."]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.
#
# Пример вывода:
#
# "Это слово обозначает наименьшую автономную часть языка программирования"
#
# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒
#
# Введите букву: O
#
# O  ▒  ▒  ▒  ▒  ▒  O  ▒
#
#
# Введите букву: Я
#
# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:

import random

word_index = random.randint(0, 2)
the_word = words[word_index]
the_word_as_list = list(the_word)
the_hidden_word = list()
for _ in range(len(the_word)):
    the_hidden_word.append("▒")
word_description = desc_[word_index]
print(word_description)
common_letters_list = list()

for i in range(10):
    if "▒" not in the_hidden_word:
        print("Поздравляю! Вы выиграли!")
        break
    else:
        user_letter = input("Введите букву: ")
        print()

        if user_letter.lower() in the_word_as_list:
            for let in range(len(the_word_as_list)):
                if user_letter.lower() == the_word_as_list[let]:
                    common_letters_list.append(let)
        else:
            print(f"Нет такой буквы.\nУ вас осталось {10 - (i + 1)} попыток!")
            continue

        for change_let in common_letters_list:
            the_hidden_word[change_let] = user_letter.lower()

            common_letters_list = list()
        for show_word in the_hidden_word:
            print(show_word, end="\t")
        print("\n\n")
else:
    if "▒" not in the_hidden_word:
        print("Вы выиграли! Поздравляю!")
    else:
        print("Ваши попытки закончились! Может, повезет в другой раз!")
