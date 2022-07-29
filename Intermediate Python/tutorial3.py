# Map Function

# Problem: I want to apply the function to every value in the list and have that stored in a new list.

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

newList = []
for x in li:
    newlist.append(func(x))
print(newList)
print()

print(list(map(func, li)))
print()
# Map function applies the function func to every element in the list

# We can also use list comprehension to do the same.
print([func(x) for x in li])
