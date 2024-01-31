# class
class Employee:
    # constructor
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    # methods
    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary


# Inheritance
class Programmer(Employee):
    def __init__(self, name, salary, language) -> None:
        super().__init__(name, salary)
        self.language = language

    def getLanguage(self):
        return self.language

    def getName(self): 
        print("Name: ", self.name)


jocefyne = Programmer("Jocefyne", 12, "Python")
print(jocefyne.getLanguage())
# print(jocefyne.getName())
jocefyne.getName()
