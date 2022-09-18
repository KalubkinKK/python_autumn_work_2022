#Преобразуйте переменную age и foo в число 
age = "23"
foo = "23abc"
age = int(age)
print(type(age))
foo = '23'
foo = int(foo)
print(type(foo))
#Преобразуйте переменную age в Boolean
age = '123abc' #Необходимо поставить кавычки, либо изменить тип данных на str (в данном случае поставил кавычки)
age = bool(age)
print(type(age))
#Преобразуйте переменную flag в Boolean
flag = 1
flag = bool(flag)
print(type(flag))
#Преобразуйте значение  в Boolean
str_one = "Privet"
str_two = ""
str_one = bool(str_one)
str_two = bool(str_two)
print(type(str_one))
print(type(str_two))

#Преобразуйте значение 0 и 1  в Boolean
num1 = 0
num2 = 1
num1 = bool(num1)
num2 = bool(num2)
print (type(num1))
print (type(num2))

# Задание из презентации (Преобразуйте False в строку.)
print(type('False'))