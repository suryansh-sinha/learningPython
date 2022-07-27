# Chained conditionals and nested statements

# and --> Both conditions must be true
# or --> One of the two conditions must be true
# not --> It reverses the boolean value of the variable

x = 2
y = 3

if x==y and x + y == 5:
    print("Ran")
else:
    print('Didn\'t run')


# Nested Example
if x == 2:
    if y == 3:
        print('Retard')
    else:
        print('Laal Singh Chadda')
else:
    print('Forrest Gump')