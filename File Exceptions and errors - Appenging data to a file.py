# 1

file = open('my_file.txt','a')
k = file.write("   While you watch")
print(k)
# output will be the num of char
file.close()

# in write mode whenever we add data it remove all the previous data

# 1

file = open('my_file.txt','r')
k = file.read()
print(k)
# output will be the num of char
file.close()