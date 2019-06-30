import sys
#Имя ОС Майкрософт Windows 10
#Версия 10.0.17134 Сборка 17134
#Тип Компьютер на базе x64
print(sys.version_info)#Версия Python 3.7.0.

def summa_rasmera(a,b,c):
    return (a+b+c)

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
#print(sys.getsizeof(c))
#print(sys.getsizeof(N))
#print(sys.getsizeof(Sum))#16
print("Размер:", summa_rasmera(sys.getsizeof(c),sys.getsizeof(N),sys.getsizeof(Sum)))

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
#print(sys.getsizeof(n))
#print(sys.getsizeof(item))
#print(sys.getsizeof(sum_))#16
print("Размер:",summa_rasmera(sys.getsizeof(n),sys.getsizeof(item),sys.getsizeof(sum_)))

print("\n*********************************")
print("3 вариант")
n2 = int(input("Сколько элементов сложить: "))
summa_ = 1 * (1-(-0.5)**n2) / (1-(-0.5))
print(summa_)
print(id(summa_))
#print(sys.getsizeof(n2))
#print(sys.getsizeof(summa_))#16
print("Размер:",summa_rasmera(0,sys.getsizeof(n2),sys.getsizeof(summa_)))

