"""
В матрице элементы последней строки заменить на 0.
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def replace_last_row(matrix):
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    matrix[rows_count - 1] = [0] * cols_count
    return matrix


print(replace_last_row(matrix))
