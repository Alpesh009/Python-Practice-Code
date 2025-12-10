class Employee:
    company="ITC"
    def show(self):
        print(f"Tha name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    def language(self):
        print(f"The name is {self.name} and the language is {self.language}")

a = Employee()
b = Programmer()

print(a.company, b.company)
