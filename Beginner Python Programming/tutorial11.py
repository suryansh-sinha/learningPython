# Slice operator.

fruits = ['apples', 'pear', 'strawberries']
text = 'Hello I hate python'

# text[start:stop:step] stop is exclusive.
print(text[0:5])
# To start at a pos and go to end, we do this -
print(text[3:])
# We can also just print iteratively.
print(text[::3])

# To insert an item in a list without using append -
# To insert between 0 and 1, do this -
fruits[1:1] = ['gorilla']
print('Fruits 1: ', fruits)

# Clone or copy a list -
fruits2 = fruits[:]
print('Fruits 2: ', fruits2)

# To delete items, just put in a blank list.
fruits[0:4] = []
print(fruits)
# Can also use the del statement to do the same.
# del fruits[0:4]
