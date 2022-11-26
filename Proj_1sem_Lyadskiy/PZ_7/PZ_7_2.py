# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и последним пробелом исходной строки. Если
# строка содержит только один пробел, то вывести пустую строку

strings = input("Введите строку: ")
b = 0
s = ""
list = []
a = strings.index(" ")
if strings.count(" ") == 1:
    print("")
else:
    n = strings.count(" ")
    while b < len(strings):
        if strings[b] == " ":
            list.append(b)
        b += 1

print(strings[a + 1:list[-1]])
