import random
print("7.В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться. ")
SIZE = 10
MIN = 0
MAX = 100
array =[ random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)
min = 100
min2 = 100
I = int()
for i in range(SIZE):
    if (array[i]<=min):
        min = array[i]
        I = i
for i in range(SIZE):
    if ((I!=i) & (array[i]<=min2)):
        min2=array[i]
print(min, min2)