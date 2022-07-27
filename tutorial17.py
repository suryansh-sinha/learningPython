# Functions with optional parameters

# To set an optional parameter, you just have to give it a default value in the function parameter itself.
def func(x=3, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')

func()
print()
func('tim', '1')
print()
func('autist')

# If you have more than 1 optional parameters, you cannot change the 2nd optional parameter's value without changing the first one's.
