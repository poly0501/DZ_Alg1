import random
print("9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.")
SIZE1 = 5
SIZE2 = 4
MIN = 0
MAX = 100
Min = int()
M1 = 0
Matr = [[random.randint(MIN, MAX) for _ in range(SIZE1)] for _ in range(SIZE2)]
for line in Matr:
    print(line)
print("Минималный элемент в каждой строке:")
for i in range(SIZE1):
    Min = Matr[0][i]
    for j in range(SIZE2-1):
        if Matr[j+1][i] <= Min:
            Min = Matr[j+1][i]
    print(f"{Min:4>}", end="   ")
    if Min > M1:
        M1=Min
        Min = 0
print("\n\nМаксимальный:", M1)