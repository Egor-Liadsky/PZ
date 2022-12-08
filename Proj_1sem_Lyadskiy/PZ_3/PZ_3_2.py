# Вариант 28
# Дано целое число в диапазоне 1-7. Вывести строку — название дня недели,
# соответствующее данному числу (1 — «понедельник», 2 — «втор


while True:
    try:
        num = int(input("Введите число: "))

        if num == 1:
            print("Понедельник")

        elif num == 2:
            print("Вторник")

        elif num == 3:
            print("Среда")

        elif num == 4:
            print("Четверг")

        elif num == 5:
            print("Пятница")

        elif num == 6:
            print("Суббота")

        elif num == 7:
            print("Воскресенье")

        else:
            print("Неверное число")

    except Exception as ex:
        print(ex)
