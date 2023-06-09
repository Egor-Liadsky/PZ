"""
В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
"""


def double_column_elements(matrix, n):
    return [[row[i] * 2 if i == n else row[i] for i in range(len(row))] for row in matrix]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = int(input("Введите N:  "))
result = double_column_elements(matrix, n)
for row in result:
    print(row)
