# Static and Class Methods

class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # You can call it on any instance of a class. You don't need an object of the class.
    # You can call it on the class. Basically --> Person.getPopulation()
    # cls doesnt need to be particularly that, it just represents the class.
    # We can also add more parameters after adding cls.
    @classmethod
    def getPopulation(cls):
        return cls.population

    # Static methods don't need any parameter to run.
    # It cant use parameters defined within the class.
    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = Person('Tim', 18)
print(Person.getPopulation())