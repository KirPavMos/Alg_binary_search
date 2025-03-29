#Создайте отсортированный список из 100 случайных чисел и
# выполните бинарный поиск для нескольких различных значений.
# Запишите результаты
# Сравните время выполнения бинарного поиска и линейного
# поиска на одинаковых списках.

import random
import time
import matplotlib.pyplot as plt

# Генерация отсортированного списка из 100 случайных чисел
random.seed(42)
sorted_list = sorted(random.randint(1, 1000) for _ in range(100))

# Реализация бинарного поиска
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Реализация линейного поиска
def linear_search(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

#  Тестирование поиска для нескольких значений
test_values = [sorted_list[0], sorted_list[-1], sorted_list[50], 9999]
print("Результаты поиска:")
for value in test_values:
    bin_idx = binary_search(sorted_list, value)
    lin_idx = linear_search(sorted_list, value)
    print(f"Значение {value}: бинарный поиск -> {bin_idx}, линейный поиск -> {lin_idx}")
