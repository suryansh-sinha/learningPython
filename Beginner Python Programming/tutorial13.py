# Reading and writing from a file.
file = open('file.txt', 'r')    # 'r' means read mode.
f = file.readlines()

print(f)    # We see that it also reads the \n at the end of every line.

newList = []
# Removing the \n from the end of each line.
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1])   # -1 means the last character of the line (which is \n) so we are just excluding the last character.
    else:
        newList.append(line)

print(newList)

newList2 = []
# There is an easier method to read lines from a file.
for line in f:
    newList2.append(line.strip())

file.close()    # Required to save any changes made to the file.