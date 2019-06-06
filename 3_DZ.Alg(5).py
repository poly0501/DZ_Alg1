import random
print("5.В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.")
SIZE = 10
MIN = -100
MAX = 100
array =[ random.randint(MIN, MAX) for _ in range(SIZE)]
print(array)
c = 0
M = int()
for i in range(SIZE):
    if ((array[i] < 0) &(array[i] >= MIN)):
        MIN = array[i]
        c = 1
        M = i
if c==1:
    print(MIN)
    print("Место", M)
else:
    print("Отрицательных чисел нет")
