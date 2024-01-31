class Employee:
    name = "jocef"
    salary = 1


jocef = Employee()
jocef.name = "Jocefyneroot"
jocef.salary = 12
# print(jocef.name)
# print(jocef.salary)


# class
class Employee2:
    # constructor
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    # methods
    def getName(self):
        return self.name

    def getSalary(self):
        return self.salary


# object
emp1 = Employee2
("Jocefyneroot", 12)  #
print(emp1.name)
print(emp1.salary)
