"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in nums]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(nums):
    b = 0
    for i in nums:
        if nums % i == 0:
            b = b + 1
    if (b <= 0):
        return True
    else:
        return False


def filter_numbers(nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [num for num in nums if num % 2]
    if filter_type == EVEN:
        return [num for num in nums if num % 2 == 0]
    if filter_type == PRIME:
        return is_prime(nums)
