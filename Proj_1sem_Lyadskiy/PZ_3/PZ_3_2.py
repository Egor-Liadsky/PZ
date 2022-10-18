
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
