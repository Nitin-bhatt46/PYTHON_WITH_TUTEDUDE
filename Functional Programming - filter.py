# filter
# it contain function, iterable,



def even(a):
    return a%2 ==0

numbers =[1,2,3,4,5]

ans = list(filter(even,numbers))
ans = set(filter(even,numbers))
ans = tuple(filter(even,numbers))

print(ans)

###


ans = list(filter(lambda a : a%2==0, range(11)))
print(ans)