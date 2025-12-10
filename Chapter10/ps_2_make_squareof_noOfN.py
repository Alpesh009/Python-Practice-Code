class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"Tha square is {self.n*self.n}")

a = Calculator(6)
a.square()