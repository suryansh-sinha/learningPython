# Topics Covered -
# Inheritance

# we can inherit from this or extend this class or override this class.
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print(f'{self.name} is working ...')

class SoftwareEngineer(Employee):
    pass

class Designer(Employee):
    pass

se = SoftwareEngineer("Max", 21)
print(se.name, se.age)
se.work()

d = SoftwareEngineer("Randy", 26)
print(d.name, d.age)
d.work()