"""
Организовать и вывести последовательность из 20 целых чисел,
выбрать уникальные элементы и посчитать их количество.
Если элементы больше 5, увеличить их в 2 раза.
"""

import random

# Организация последовательности из 20 целых чисел
numbers = [random.randint(-100, 100) for i in range(20)]

# Выбор неповторяющихся элементов и нахождение их количества
unique_numbers = set(numbers)
unique_number_count = len(unique_numbers)

# Увеличение элементов больше 5 в два раза
double_numbers = [number * 2 if number > 5 else number for number in numbers]

# Вывод результатов
print("Последовательность целых чисел:", numbers)
print("Неповторяющиеся элементы:", unique_numbers)
print("Количество неповторяющихся элементов:", unique_number_count)
print("Увеличенные в два раза элементы:", double_numbers)
