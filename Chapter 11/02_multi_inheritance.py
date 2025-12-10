class Employee:
    company="ITC"
    name = "Horizon"
    def show(self):
        print(f"Tha name is {self.name} and the salary is {self.company}")

class Coder:
    lang = "Python"
    def printLanguages(self):
        print(f"The language is {self.lang}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    
    def language(self):
        print(f"The name is {self.company} and the language is {self.lang}")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.language()