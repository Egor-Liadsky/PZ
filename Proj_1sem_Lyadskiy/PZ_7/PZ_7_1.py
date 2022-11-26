# Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
# вставить строку S0.

c = input("Введите символ: ")
s = input("Введите строку: ")
s_0 = input("Введите строку: ")
a = ""

number = 0

while number <= len(s):
    if c in s:
        a = s.replace(c, s_0)
    number += 1

print(a)
