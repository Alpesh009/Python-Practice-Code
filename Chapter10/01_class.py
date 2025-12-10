class employee():
    lang = "Python" # class attribute
    salary = 1200000 # class attribute

    def getInfo(self):
        print(f"The language is {self.lang} and salary is {self.salary}")

emp = employee()
# print(emp.lang, emp.salary)

# emp.getInfo()
employee.getInfo(emp)

