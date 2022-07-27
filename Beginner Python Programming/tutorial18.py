# Try and Except. Error Handling.
text = input('Username: ')
try:
    number = int(text)
    print(number)
except:
    print("Invalid Username!")
# Now, if we enter text in username instead of a number, the program throws an error saying it can't convert text to numbers!
# To handle that error, we use try and catch.