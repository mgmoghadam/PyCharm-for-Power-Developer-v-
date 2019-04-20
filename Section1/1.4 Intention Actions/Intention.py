import math


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def divide(self):
        return self.a / self.b

    def subtract(self):
        return self.a - self.b

    def root(a):
        return math.sqrt()


def greetings(name):
    print('Hello ' + name + '!')


def goodbye():
    print('Goodbye!')


myCalculator = Calculator(15, 6)
print(myCalculator.subtract())
