import random
print("3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.")
SIZE = 10
MIN = 0
MAX = 100
array =[ random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)
Imin = int()
Imax = int()
min = array[0]
max = array[0]
for i in range(SIZE):
    if array[i]<= min:
        min = array[i]
        Imin = i
    if array[i]>= max:
        max = array[i]
        Imax = i
print("Минимальный элемент:%d место:%d" %(min,Imin))
print("Максимальный элеvент:%d место:%d" %(max,Imax))
array[Imin]=max
array[Imax]=min
print(array)