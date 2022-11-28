# Организовать словарь 10 русско- английских слов, обеспечивающий
# "перевод" русского слова на английского.

dict = {"hello": "привет",
        "bye": "пока",
        "spring": "весна",
        "world": "мир",
        "keyboard": "клавиатура",
        "mouse": "мышь",
        "package": "пакет",
        "phone": "телефон",
        "project": "проект",
        "main": "главный"
        }

word = input("Введите слово: ")

for key, value in dict.items():
    if word == value:
        print(key)
        break
