class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


e1 = Employee("Rohan Das", 430)
e1.showDetails()
e2 = Programmer("Harry", 444)
e2.showDetails()
e2.showLanguage()