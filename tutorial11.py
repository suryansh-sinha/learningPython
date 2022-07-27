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
fruits[1:1] = 'gorilla'
print(fruits)