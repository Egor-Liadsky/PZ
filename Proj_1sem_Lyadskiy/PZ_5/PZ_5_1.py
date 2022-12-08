"""
Вариант 28
Составить функцию решения задачи: из заданного числа вычли сумму его цифр. Из
результата вновь вычли сумму его цифр и т. д. Через сколько таких действий
получится нуль?
"""


def take_sum_numeric(number):
    sum = 0
    iter_num = 0
    while abs(iter_num) != len(number):
        sum += int(number[iter_num])
        iter_num -= 1
    return sum


input_number = int(input('Введите число: '))

acum_step = 0
while input_number > 0:
    input_number = input_number - take_sum_numeric(str(input_number))
    acum_step += 1

print(f"Нуль получится через {acum_step}  действий")
