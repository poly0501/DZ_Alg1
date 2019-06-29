import sys
#Имя ОС Майкрософт Windows 10
#Версия 10.0.17134 Сборка 17134
#Тип Компьютер на базе x64
print(sys.version_info)#Версия Python 3.7.0.
print("4)Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится с клавиатуры.")
print("1 вариант")
print("Введите количество элементов")
N = int(input("N= "))
c = 1
Sum = 1
print("Все элементы:")
print(c)
for i in range(N-1):
    c = c * (-0.5)
    Sum += c
    print(c)
print("\nОтвет:")
print(Sum)
print(id(Sum))
print(sys.getsizeof(Sum))#16

print("\n*********************************")
print("2 вариант")
n = int(input("Сколько элементов сложить: "))
item = 1
sum_ = 0
for _ in range(n):
    sum_ += item
    item/= -2
print(sum_)
print(id(sum_))
print(sys.getsizeof(sum_))#16

print("\n*********************************")
print("3 вариант")
n2 = int(input("Сколько элементов сложить: "))
summa_ = 1 * (1-(-0.5)**n2) / (1-(-0.5))
print(summa_)
print(id(summa_))
print(sys.getsizeof(summa_))#16
