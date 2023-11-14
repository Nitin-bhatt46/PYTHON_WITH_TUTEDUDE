# list function.

list1=[1,2,3,4,5,6]

# it add value at the last of the list
list1.append(25)
print(list1)

# it also add the value at the last of the list but it need to iterable.
list1.extend("12")

print(list1)
# it add the value at any place og the list with the help of indexing

list1.insert(1,50)

print(list1)


# how to remove ( just enter the value.
list1.remove(25)
print(list1)

# in this del function we need indexng

del list1[1]
print(list1)


# it create a filled list into a blank list

list1.clear()