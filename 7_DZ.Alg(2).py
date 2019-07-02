import random
print("Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.")


def connect(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Создаваём переменные для длины списков
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        # Мы проверяем, какое значение с начала каждого списка меньше
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Если элемент в начале левого списка меньше, добавляем его в отсортированный список
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если элемент в начале правого списка меньше, добавляем его в отсортированный список
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если мы достигли конца левого списка, добавляем элементы из правого списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если мы достигли конца правого списка, добавляем элементы из левого списка
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def connect_sort(nums):
    # Если список представляет собой один элемент, возвращаем его
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    # Сортируем и объединяем каждую половину
    left_list = connect_sort(nums[:mid])
    right_list = connect_sort(nums[mid:])

    return connect(left_list, right_list)


SIZE = 5
MIN = 0
MAX = 49
a = [0] * SIZE
for i in range(SIZE):
   a[i] = float(random.randint(MIN, MAX))
print("Исходный список\n", a)
a = connect_sort(a)
print("Отсортированный список:\n", a)
