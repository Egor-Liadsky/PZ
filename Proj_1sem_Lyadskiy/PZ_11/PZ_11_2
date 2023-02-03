"""
Из предложенного текстового файла (text18-28.txt) вывести на экран его содержимое,
количество символов в тексте. Сформировать новый файл, в который поместить текст в
стихотворной форме предварительно вставив после строки N (N – задается пользователем)
произвольную фразу.
"""

# чтение файла
file = open("text18-28.txt", "r")
text = file.read()
print("Содержимое файла:")
print(text)
print("Количество символов в тексте:", len(text))
file.close()

# формирование нового файла
line_number = int(input("Введите номер строки, после которой требуется вставить фразу: "))
phrase = input("Введите фразу: ")

lines = text.split("\n")
lines.insert(line_number, phrase)
new_text = "\n".join(lines)

file = open("new_text.txt", "w")
file.write(new_text)
file.close()
