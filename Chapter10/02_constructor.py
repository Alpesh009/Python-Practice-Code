class employee():
    lang = "Python" # class attribute
    salary = 1200000 # class attribute

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating object")
        
    def getInfo(self):
        print(f"Tha language is {self.lang} and salary is {self.salary}")

emp = employee("Alpesh", 1400000, "Javascript")
# emp.name = "Alpesh"
print(emp.name, emp.salary, emp.language)
# print(emp.lang, emp.salary)


