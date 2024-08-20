class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


class Programmer(Employee):
    company = "ITC Infotech"

    def __init__(self, name, salary, language,company):
        super().__init__(name, salary)
        self.language = language
        self.company = company

    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language and name of company is {self.company}")


# Creating instances of Employee and Programmer
a = Employee("Rayyan", 50000)
b = Programmer("Harry", 60000, "Python","xyz")

# Calling methods
b.showLanguage()

# Printing the company names
print(a.company, b.company)
