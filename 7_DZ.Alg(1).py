import random
print("Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.")

#благодаря изменению кода, количество шагов изенится(уменьшится) в том случае, если перестановок будет меньше, чем длина списка. Сортировка будет прогонять список столько раз, сколько потребуется, не больше.


def sort(array, k):
    n = 1
    while n == True:
        n = False
        for i in range(len(array) - 1):
            if array[i] < array[i + 1]:
                if k == 1:
                    print("Меняем местами:", array[i], array[i + 1])
                array[i], array[i + 1] = array[i + 1], array[i]
                n = True
                if k == 1:
                    print(array)
    return array


SIZE = 10
MIN = -100
MAX = 99
array = [random.randint(MIN, MAX) for _ in range(SIZE)]
print("Исходный массив:\n", array)
k = int(input("\nВы хотите увидеть шаги?\nДа - 1 Нет - 2:"))
print("\nОтсортированный массив:\n", sort(array, k))
