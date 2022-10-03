# #todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
# – id - номер по порядку (от 1 до 10);
# – текст из списка algoritm
#
# algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
# "EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]
#
# Каждое значение из списка должно находится на отдельной строке.

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
            "EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]
new_list = []
title = ('ID\t', 'algoritm\n')

fd = open('algoritm.csv', mode='tw', encoding='UTF-8')

for i in range(len(algoritm)):
    new_list.append(str(i + 1) + '   ' + algoritm[i] + '\n')

fd.writelines(title)
fd.writelines(new_list)
fd.close()
