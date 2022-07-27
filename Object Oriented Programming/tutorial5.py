class Dog:
    # This is a class variable. You can use these without creating an object for the class.
    # for example, you can write this - print(Dog.dogs) and it will return a list with 2 dog objects that we have added to the list.
    # You can also access these using object.
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # @classmethod or @staticmethod --> These are known as decorators.
    # They're used to indicate special type of functions.    
    
    @classmethod
    # You can call this on the name of the class. dog.num_dogs() will work. We don't need an object to execute this function.
    # You can still call this on objects too though.
    # cls stands for class
    def num_dogs(cls):
        return len(cls.dogs)

    # These methods are the ones who don't require class attributes. They also work without creating objects.
    # We can't access class variables in this because self and cls dont work here.
    @staticmethod
    def bark(n):
        """barks n times""" # This is a multiline comment
        for _ in range(n):
            print("Bark!")

tim = Dog('Tim')
jim = Dog('Jim')