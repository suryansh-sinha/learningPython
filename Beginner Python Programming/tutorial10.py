# String methods in python.
# There are 60 plus methods for strings in python.
# strip(), len(), lower(), upper(), split()

text = input('Input something: ')
print(text)
print(text.strip())
print(len(text))
# strip function removes whitespaces (including \t and \n) from the start and end of the provided string.
# It can also take in parameters to remove those characters from the start or end of the string.

# .lower() turns everything to lower case.
# .upper() turns everything to upper case.

# split() creates a list of all the items in the list. It takes a delimiter by which the string is split.
# The delimiter is removed from the string and the string is split into parts as shown below. Where delimiter is '.'
# example -> "hello.tim.hi.bye" becomes ['hello', 'tim', 'hi', 'bye']
print(text.split('.'))