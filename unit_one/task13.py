# todo: Дан целочисленный массив размера N из 10 элементов.
# Преобразовать массив, увеличить каждый его элемент на единицу.

mass = [2, 6, 7, 8, 4, 2, 5, 7, 8, 4]
for i in range(len(mass)):
    mass[i] += 1
print(mass)