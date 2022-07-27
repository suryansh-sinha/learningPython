# Iteration by items.

fruits = ['apples', 'pears', 'strawberries', 3, 8, 90]

# Here fruit is a variable that stores the item at current iterator in the list.
for fruit in fruits:
    print(fruit)

print()

# len() function gives us the number of items in the list.
for x in range(len(fruits)):
    if fruits[x] == 'pears':
        print(fruits[x])
    else:
        print('Not Pears')