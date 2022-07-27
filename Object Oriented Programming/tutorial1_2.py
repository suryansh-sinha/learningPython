# Inheritance and shit.
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi! I am', self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print("Bark!")

# class Cat inherits Dog. Means it has all the same functions that are in the Dog class.
# Here, Dog is the parent class of the Cat class.
class Cat(Dog):
    # Creating the constructor for this class.
    def __init__(self, name, age, color):
        # Calling the constructor of the Dog class to initialize those variables.
        super().__init__(name, age)
        # Initializing the color variable because that wasn't in the previous class.
        self.color = color

    # Whatever function with same name we write here, it overwrites the parent function.
    # This is called function overriding.
    def talk(self):
        print("Meow")

# Creating a cat object. 
tim = Cat('tim', 5, 'blue')
tim.speak()
tim.talk()