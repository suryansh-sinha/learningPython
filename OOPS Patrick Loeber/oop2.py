# Topics Covered -
# Inheritance
# Extends
# Overriding
# Polymorphism

# Extends - When you use the methods of the parent class and then add some new methods in the child class.
# Overriding - Creating a method in the child class with the same name as the parent class but with different operation.
# Polymorphism - ability of a message to be displayed in more than one form


# we can inherit from this or extend this class or override this class.
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # class method defined here.
    def work(self):
        print(f'{self.name} is working...')

class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary) # passing the name and age into the original init function of the parent class
        self.level = level

    # method overriding
    def work(self):
        print(f'{self.name} is coding...')

    def debug(self):
        print(f'{self.name} is debugging...')

class Designer(Employee):

    # method overriding
    def work(self):
        print(f'{self.name} is designing...')
    
    def draw(self):
        print(f'{self.name} is drawing...')

se = SoftwareEngineer("Max", 21, 52000000, 'Junior')
print(se.level)
se.work()
se.debug()

print('\n')

d = Designer("Randy", 26, 5000)
print(d.name, d.age)
d.work()
d.draw()

print('\n')

# Polymorphism example -
employees = [se, d,
             Designer('Lisa', 20, 30000)]

# this outputs different messages for different instances.
def workinprogress():
    for employee in employees:
        employee.work()

workinprogress()