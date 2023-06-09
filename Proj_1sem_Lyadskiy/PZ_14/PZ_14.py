"""
В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и
ДД/ММ/ГГГГ. Посчитать количество дат в каждом формате. Поместить в новый
текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
"""

import re

# Открываем файл с датами для чтения
with open("dates.txt", "r") as f:
    text = f.read()

# Находим все даты в формате ДД.ММ.ГГГГ и ДД/ММ/ГГГГ
dates_dot = re.findall(r"\b\d{2}\.\d{2}\.\d{4}\b", text)
dates_slash = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)

# Подсчитываем количество дат в каждом формате
count_dot = len(dates_dot)
count_slash = len(dates_slash)

# Открываем файл для записи дат февраля
with open("february_dates.txt", "w") as f:
    # Находим все даты февраля в формате ДД.ММ.ГГГГ
    february_dates_dot = re.findall(r"\b\d{2}\.02\.\d{4}\b", text)
    # Записываем все даты февраля в формате ДД/ММ/ГГГГ
    for date in february_dates_dot:
        date_slash = re.sub(r"\.", "/", date)
        f.write(date_slash + "\n")

# Выводим количество дат в каждом формате
print("Количество дат в формате ДД.ММ.ГГГГ:", count_dot)
print("Количество дат в формате ДД/ММ/ГГГГ:", count_slash)

