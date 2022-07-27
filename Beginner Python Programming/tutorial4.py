# Decisions
# if condition == True:
#     do this

age = input('Input your age: ')

if int(age) >= 16:
    print("Hey! You're older than 16")
else:
    print("You're younger than 16.")


height = int(input())
if height < 1:
    print('You cannot ride')
elif height > 2:
    print('You cannot ride')
elif height == 5:
    print('Wow! You are abnormally tall. Khali moment.')
else:
    print('You can ride.')