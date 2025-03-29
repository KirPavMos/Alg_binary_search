# Реализуйте алгоритм бинарного поиска на языке Python. Функция
# должна принимать отсортированный список и элемент для поиска,
# и возвращать индекс элемента или -1, если элемент не найден
# Проанализируйте временную и пространственную сложность
# алгоритма бинарного поиска.

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Пример 1: Элемент найден
numbers = [1, 3, 5, 7, 9]
print(binary_search(numbers, 5))

# Пример 2: Элемент не найден
print(binary_search(numbers, 4))