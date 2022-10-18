try:
    num = int(input("Введите число: "))
    count = 0
    res = 0
    if num > 0:
        while count <= num:
            sum = (num + count) ** 2
            res += sum
            count += 1
            print(sum)
        print(res)

except Exception as ex:
    print(ex)
