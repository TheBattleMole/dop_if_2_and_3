from time import sleep

"""Найти срединное значение из трех чисел """
list_ = list(map(int, input("Введите 3 числа через пробел: ").split()))
if list_[1] < list_[0] < list_[2]:
    print(list_[0])
if list_[2] < list_[0] < list_[1]:
    print(list_[0])
if list_[2] < list_[1] < list_[0]:
    print(list_[1])
if list_[0] < list_[1] < list_[2]:
    print(list_[1])
if list_[1] < list_[2] < list_[0]:
    print(list_[2])
if list_[0] < list_[2] < list_[1]:
    print(list_[2])
"""-----------------------------------------------"""

"""Смешиваем цвета"""

a = "красный"
b = "синий"
c = "желтый"
first_ = input("Введите первый цвет: ")
second_ = input("Введите второй цвет: ")
if (first_.lower() == a and second_.lower() == b) or (first_.lower() == b and second_.lower() == a):
    print("Смешиваем.....")
    sleep(1)
    print("Получили - фиолетовый")
elif (first_.lower() == a and second_.lower() == c) or (first_.lower() == c and second_.lower() == a):
    print("Смешиваем.....")
    sleep(1)
    print("Получили - оранжевый")
elif  (first_.lower() == b and second_.lower() == c) or (first_.lower() == c and second_.lower() == b):
    print("Смешиваем.....")
    sleep(1)
    print("Получили - зеленый")
else:
    print("ОШИБКА: недопустимый для смешивания цвет")
"""----------------------------------------------------------------------------------------------------"""



