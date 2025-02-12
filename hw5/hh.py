# 1 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
string1 = "www.my_site.com#about"
print(string1.replace("#", "/"))

# 2 Напишите программу, которая добавляет ‘ing’ к словам


def adding_ing_function(a):
    return a + 'ing'


print(adding_ing_function('random'))
print(adding_ing_function('run'))

# 3 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
string3 = 'Ivanou Ivan'
sep = string3.split()
# print(type(sep), sep)
sep.reverse()
new_string = ' '.join(sep)
print(new_string)

# другой вариант
# string31 = "Ivanou Ivan"
# swapped_string31 = ' '.join(string31.split()[::-1])
# print(swapped_string31)

# 4 Напишите программу которая удаляет пробел в начале, в конце строки
string4 = ' test task 4 '
print(string4.strip())

# 5 Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
# Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению.
# "pARiS" >> "Paris"

string5 = 'pARiS'
print(string5.capitalize())

# 6 Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
string6 = "Robin Singh"
lst = string6.split()
print(lst)
# 7 "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
string7 = "I love arrays they are my favorite"
lstt = string7.split()
print(lstt)
# 8 Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
arr8 = ["Ivan", "Ivanou"]
string8 = "Minsk"
string81 = "Belarus"
print("Привет, " + arr8[0] + " " + arr8[1] + "! Добро пожаловать в " + string8 + " " + string81)
# 9 Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
arr9 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
arr9_string = " ".join(arr9)
print(arr9_string)
# 10 Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
arr10 = ["lemon", "apple", "pear", "watermelon",
         "plum", "orange", "tangerine", "mango", "peach", "coconut"]
arr10.insert(2, "papaya")
del arr10[6]
print(arr10)
