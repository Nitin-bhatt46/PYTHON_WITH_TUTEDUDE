
# method 1

file1=open("my_file.txt",'r')
reading_file =file1.read()
print(reading_file)
file1.close()


# methos 2
with open ('my_file.txt','r') as file1:
    reading_file =file1.read()
    print(reading_file)