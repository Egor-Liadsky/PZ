def sumInt(num: int) -> int:
    leftNum = num // 10
    rightNum = num % 10
    if len(str(num)) == 3:
        centerNum = (num % 100)//10
        return num - (leftNum + rightNum + centerNum)
    return num - (leftNum + rightNum)


num = int(input())
count = sumInt(num)

# print(sumInt(num))

while True:
    print(count)
    count = sumInt(count)
    if count == 0:
        print(0)
        break
