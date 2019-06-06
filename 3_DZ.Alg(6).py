import random
print("6.В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.")
SIZE = 10
MIN = 0
MAX = 100
array =[ random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)
Imin = int()
Imax = int()
min = array[0]
max = array[0]
summa = 0
for i in range(SIZE):
    if array[i]<= min:
        min = array[i]
        Imin = i
    if array[i]>= max:
        max = array[i]
        Imax = i
print("Минимальный элемент:%d место:%d" % (min, Imin))
print("Максимальный элеvент:%d место:%d" % (max, Imax))
if Imin<Imax:
    for i in range(Imin+1, Imax):
        summa += array[i]
else:
    for i in range(Imax+1, Imin):
        summa += array[i]
print (summa)