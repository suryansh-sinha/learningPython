# x = 5
# y = 'string'

# print(type(x))  # Gives us output <class 'int'>
# print(type(y))  # Gives us output <class 'str'>

# Basically, x and y are instances of int and str classes respectively.

# Creating a new class.
class Dog(object):
    
    # This is the constructor function. We dont need to execute this, everytime an object is created, this will be called automatically.
    def __init__(self, name, age):
        # self is the object that has been created. So, tim.name = 'tim'. Basically this keyword from java.
        self.name = name
        self.age = age

    def speak(self):
        print('Hi! I am ', self.name, 'and I am', self.age, 'years old')

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight

# Creating new objects.
tim = Dog('Tim', 55)
fred = Dog('Fred', 3)
tim.speak()
fred.speak()
tim.change_age(12)
tim.speak()
tim.add_weight(59)
print(tim.weight)

print(tim.age, tim.name)