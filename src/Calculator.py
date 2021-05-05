def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a

def multiplication(a, b):
    a = int(a)
    b = int(b)
    return (a) * (b)

def division(a, b):
    a = float(a)
    b = float(b)
    return round((b/ a), 9)

def square(a):
    a = float(a)
    return a**2

def squareroot(a):
    a = float(a)
    return round((a**.5), 4)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqrd(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = squareroot(a)
        return self.result