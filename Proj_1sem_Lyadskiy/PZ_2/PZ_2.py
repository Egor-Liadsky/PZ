try:
    second = int(input("Введите количество секунд: "))
    print((second % 3600) // 60)
except Exception as e:
    print(e)
