# Topics Covered -
# instance attributes, class attributes
# instance methods, class methods
# 'dunder' methods (__str__ and __eq__). Can learn more about these in python docs.
# @staticmethod decorator for static methods.


# position, name, age, level, salary.
se1 = ["Software Engineer", "Max", 20, "Junior", 5000]
se2 = ["Software Engineer", "Lisa", 25, "Senior", 7000]

# Class
class SoftwareEngineer:

    # class attributes. This is an attribute that is global for the class.
    # all the objects of this class will be able to access this variable.
    alias = "Keyboard Magician"

    # the parameters defined in the constructor are the required values for creating an instance of this class.
    def __init__(self, name, age, level, salary):
        # now we define new variables for the class. These are called instance attributes.
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance method
    def code(self):
        print(f'{self.name} is writing code...')

    def code_in_language(self, language):
        print(f'{self.name} is writing code in {language}.')

    # d-under method. these are special functions which are already there but are not defined.
    # the str function decides what happens when you pass the object into the print function.
    def __str__(self):
        information = f'Name = {self.name}, Age = {self.age}, Level = {self.level}, Salary = {self.salary}'
        return information

    # here we compare two objects. this returns a boolean value.
    def __eq__(self, object):
        return self.name == object.name and self.age == object.age

    # class function. this function does not have self in the arguments and can only be called using the class name, not using instances.
    # in practice, we have to use decorator here, though it works without it too.
    @staticmethod
    # in this function, we cannot access the instance attributes. so, using self.age here would throw an error.
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000
        
# instance
se1 = SoftwareEngineer("Slash", 21, "Senior", 5000000)
print(SoftwareEngineer.alias)   # class attributes can be accessed without creating an instance.
print(se1.alias)    # we can also access class attributes from instances of the class.
print(se1.name, ",", se1.age)
se1.code()
se1.code_in_language('Python')
print(se1)  # this uses the __str__ function that we defined above.

print('\n')

se2 = SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(f'{se2.name}, {se2.level}')
se2.code()
se2.code_in_language('C++')
print(se2, '\n')

se3 = SoftwareEngineer("Slash", 21, "Senior", 5000000)
print(se1 == se3)
print('\n')

print(SoftwareEngineer.entry_salary(29))