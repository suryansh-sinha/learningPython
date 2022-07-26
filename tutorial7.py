# While Loops

# while condition == True:
#     do this
# break keyword is used to end the loop right there and go outside

loop = True
while loop:
    name = input('Insert something: ')
    if name == 'stop':
        loop = False
        break