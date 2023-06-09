"""
Составить генератор (yield), который переведет символы строки из верхнего
регистра в нижний.
"""


def to_lower_case(string):
    for char in string:
        yield char.lower()


string = "HELLO, WORLD!"
result = [char for char in to_lower_case(string)]
print("".join(result))
