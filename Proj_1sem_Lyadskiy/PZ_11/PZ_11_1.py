"""
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов;
Среднее арифметическое элементов первого и второго файлов;
Количество нечетных элементов первого и второго файлов;
Элементы общие для двух файлов;
Количество элементов, общих для двух файлов.
"""


# создаем два текстовых файла с последовательностями целых чисел
def create_files():
    with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
        f1.write("1 2 -3 4 -5")
        f2.write("2 3 -4 5 -6")


# рассчитываем среднее, количество нечетных элементов, общие элементы и их количество
def calculate_statistics():
    with open("file1.txt") as f1, open("file2.txt") as f2:
        elements1 = [int(x) for x in f1.read().split()]
        elements2 = [int(x) for x in f2.read().split()]
        avg = (sum(elements1) + sum(elements2)) / (len(elements1) + len(elements2))
        odd_count1 = len([x for x in elements1 if x % 2 != 0])
        odd_count2 = len([x for x in elements2 if x % 2 != 0])
        common = set(elements1).intersection(set(elements2))
        common_count = len(common)

    # записываем результаты в новый текстовый файл
    with open("result.txt", "w") as f:
        f.write(f"Элементы первого файла: {elements1}\n")
        f.write(f"Элементы второго файла: {elements2}\n")
        f.write(f"Среднее арифметическое элементов двух файлов: {avg}\n")
        f.write(f"Количество нечетных элементов в первом файле: {odd_count1}\n")
        f.write(f"Количество нечетных элементов во втором файле: {odd_count2}\n")
        f.write(f"Общие элементы: {common}\n")
        f.write(f"Количество общих элементов: {common_count}")


if __name__ == "__main__":
    create_files()
    calculate_statistics()
