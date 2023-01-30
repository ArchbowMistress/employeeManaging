class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def __repr__(self):
        return self._name + " has a salary of %.2f" % self._salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self._department = department

    def __repr__(self):
        return self._name + " has a salary of %.2f" % self._salary + " and manages the " + self._department + " department."

class Excecutive(Manager):
    def __int__(self, name, salary, department):
        super().__init__(name, salary, department)

    def __repr__(self):
        return self._name + " has a salary of %.2f" % self._salary + " and is the executive for the " + self._department + " department."

