# map( function, iterable)

numbers = list(range(1,11))

def square(a):
    return a**2


ans = map(square,numbers)
# it will show the addres

# in this we will use data type to save it
ans =list(map(square,numbers))

print(ans)

# if both filter and map can do same thing :- map take all the number and sent it back , filter take one by one and return a new list.