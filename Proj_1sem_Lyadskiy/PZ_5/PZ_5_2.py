def addLeftDigit(D: int, K: int):
    if (D <= 0 or D > 9 or K <= 0):
        print("Неверное значение параметров")
    else:
        n = K
        while ( n != 0):
            n /= 10
            D *= 10
        K += D


K = int(input("Введите число: "))
D1 = int(input("Введите число: "))
D2 = int(input("Введите число: "))
addLeftDigit(D1, K)
print(K)
addLeftDigit(D2, K)
print(K)
