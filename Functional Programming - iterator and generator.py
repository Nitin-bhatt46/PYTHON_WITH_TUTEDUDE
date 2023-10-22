# iterator
list = list(range(1,6))
# printing with index

print(list[1])

# printing using for loop

for i in list:
    print(i)

# using iterator
# this is how a iteration work inside loop or in indexing.

itertion =iter(list)
print(itertion.__next__())
print(itertion.__next__())
print(itertion.__next__())
print(itertion.__next__())
print(itertion.__next__())



# generator

def fn():

    yield 1 # it represent the last step of the function.

values =fn()
print(values.__next__())


def square():
    n=1
    while n<=5:
        square = n**2
        yield square
        n=n+1


values = square()
for i in values:
    print(i)