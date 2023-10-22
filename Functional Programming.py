# functional programming

def add(i,j):
    return i+j;

def call(i,j):
    return add(i,j)


# calling function

print(add(1,3))

# calling function inside function

print(call(1,3))