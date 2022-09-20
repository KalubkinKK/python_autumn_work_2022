# todo: Данные две переменные:
# Нужно обменять значения переменных местами. В итого age должен равнятся 25 а  temperature – 36.6:
age = 36.6
temperature = 25

# 1 способ решения (через введение новой дополнительной переменной, допустим "reverse"):
age = 36.6
temperature = 25
reverse = age
age = temperature
temperature = reverse
print('age =', age)
print('temperature =', temperature)

# 2 способ решения (сразу переприсвоить переменные):
age = 36.6
temperature = 25
age, temperature = temperature, age
print('age =', age)
print('temperature =', temperature)

# 3 способ решения (арифметика)
age = 36.6
temperature = 25
age = age + temperature
temperature
print('age =', age)
print('temperature =', temperature)
