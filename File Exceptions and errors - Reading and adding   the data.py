# r+ --> write and read

file= open('my_file.txt','r+')
writing = file.write('Welcome jaadu ')
print(writing)
file.close()


file = open('my_file.txt','r+')
reading_file = file.read()
print(reading_file)
file.close()
