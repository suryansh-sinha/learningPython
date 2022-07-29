# Filter Function

def add7(x):
    return x + 7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list(filter(isOdd, a))  # If function returns true, it is added to the list. Else it's not.

c = list(map(add7, b))

# Combining the map and filter functions in single line.
# Same as the above list.
d = list(map(add7, filter(isOdd, a)))