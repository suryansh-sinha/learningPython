file = open('file2.txt', 'w')   # 'w' clears the entire file and then starts writing to the file.
# If the file doesn't exist, it creates the file and then starts working with it.

file.write('Retarded')
file.write('\nI am learning to write to files in python.')

file.close()