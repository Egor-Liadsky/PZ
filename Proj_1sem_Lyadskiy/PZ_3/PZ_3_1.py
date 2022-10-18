while True:
    try:
        x = int(input("Введите x: "))
        y = int(input("Введите y: "))

        if x > 0 and y > 0:
            print("Первая четверть")

        elif x < 0 and y < 0:
            print("Третья четверть")

        else:
            print("Координаты не лежат на первой или третьей четверти")
    except Exception as ex:
        print(ex)
