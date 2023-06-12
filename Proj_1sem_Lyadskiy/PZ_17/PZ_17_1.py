"""
Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
инкремента и декремента значения.
"""

class Counter:
    def __init__(self, value=0):
        self.value = value

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1


counter = Counter(5)

print(counter.value)

# Инкремент значения
counter.increment()
print(counter.value)

# Декремент значения
counter.decrement()
print(counter.value)