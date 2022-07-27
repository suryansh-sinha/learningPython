x = 2
name = 'Tim'

print("What is your name? ")
name = input()
# print(f"Hi {name}")
print("Hello, ", name) # The comma just separates the values.

# Exponents is ** and Integer Division is // and % is modulus.
print("Pick a number: ")
num1 = input()
print("Pick another number: ")
num2 = input()
print(type(num2))
# The input function always reads a string from the user. To treat it as integer, we have to first convert it to int.
# Else, we're basically adding 2 strings together here.
sum = num1 + num2

# This is called typecasting.
sum = int(num1) + int(num2)
print(sum)