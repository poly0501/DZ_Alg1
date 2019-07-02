import random
print(" Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.")


def new_sort(x, y):
    if (x - y) > 0:
        return(1)
    if(x-y) < 0:
        return (0)


def _mediana_(array, m):
    t = array[(2*m+1)//2]
    return(t)


MIN = 0
MAX = 50
n = 1
m = int(input('Введите m = '))
array = [random.randint(MIN, MAX) for _ in range(2*m+1)]
print("Длина списка:", 2*m+1)
print("Исходный список\n", array)
while n == True:
    n = False
    for i in range(2*m):
        if new_sort(array[i], array[i+1]):
            array[i], array[i + 1] = array[i + 1], array[i]
            n = True
print("Отсортированный список:\n", array)
print("\nМедиана нашего списка:", _mediana_(array, m))

