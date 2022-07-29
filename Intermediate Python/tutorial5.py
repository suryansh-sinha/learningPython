# Lambda Function

def func(x):
    return x + 5

# Declaring above function using lambda.
# Just that whatever we want to return must be a single expression.
# We can use multiple parameters too instead of just one.
func2 = lambda x: x+5

func3 = lambda x,y: x+y

a = [1,2,3,4,5,6,7,8,9,10]
newList = list(map(lambda x:x+5, a))

print(newList)