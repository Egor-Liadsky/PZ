# Дан список A размером N. Найти максимальный элемент из его элементов с нечетными номерами: A1, A3, A5, ... .

import random

list = []
listOdd = []

num = int(input())
count = 0

while count < num:
    list.append(random.randint(0, 100))
    count += 1

print(list)
for i in list:
    if i % 2 == 0:
        listOdd.append(i)

print(max(listOdd))
