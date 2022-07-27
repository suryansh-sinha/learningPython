# Functions
def addTwo(x):
    return x + 2

def subTwo(x):
    return x - 2

# Variable in function prototype is called parameter.
def printString(string):
    print(string)

def acc(mass, force):
    a = force / mass
    return a

def doSomething():
    print('Hey!')

# Value given to parameter in function call is called argument.
print(addTwo(6))
print(subTwo(6))
printString('Autism')
print(acc(2, 5))
doSomething()