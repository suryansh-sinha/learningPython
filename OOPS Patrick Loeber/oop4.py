# Topics Covered -
# Encapsulation

class SoftwareEngineer:

    def __init__(self):
        self._salary = None

    # getter. For getter, we give the function the name of the property we want. Then we use the @property decorator.
    @property
    def salary(self):
        return self._salary

    # setter function
    @salary.setter
    def set_salary(self, value):
        self._salary = value

    # deleter function
    @salary.deleter
    def salary(self):
        del self._salary

se = SoftwareEngineer()

# Setting the salary for se with base as 6000.
se.set_salary(6000)
print(se.salary)    # we can now access this property as a simple variable.
del se.salary
print(se.salary)