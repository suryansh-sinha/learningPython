# Local vs Global Variables
var = 9
loop = True

def func(x):
    # Local Variable. This is defined inside the function so, it is the local variable of this function.
    loop = 7
    if x == 5:
        return loop

def otherFunc():
    global loop # Declaring a global variable loop inside the function.
    loop = 7

func(2) # Calling function with local variable that changes value of loop to 7.
print(loop) # We see that the value of the global variable remains unchanged.
otherFunc() # Calling new function where we change the value of global variable loop.
print(loop) # Printing the changed value of loop variable.