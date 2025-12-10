class Employee:
    a = 1
    @classmethod
    def show(self):
        print(f"The a attribute value is {self.a}")

e = Employee()
e.a = 34

e.show()