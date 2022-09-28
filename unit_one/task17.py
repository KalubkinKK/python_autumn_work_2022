# todo: Создайте функцию compute_bill, считающую итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество единиц товара.
# Цены хранятся в словаре:
# prices = {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }

prices = {
    "banana": 400,
    "apple": 200,
    "orange": 150,
    "pear": 300
}

quantity = {
    "banana": 5,
    "apple": 3,
    "orange": 7,
    "pear": 14
}


def fruits_calc(quantity_dict, prices_dict):
    price_sum = 0
    for i_fruit in prices_dict.keys():
        price_sum += prices_dict[i_fruit] * quantity_dict[i_fruit]
    return price_sum


print(fruits_calc(quantity, prices))
