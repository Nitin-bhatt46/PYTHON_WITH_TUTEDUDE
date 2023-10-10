# factorial

# 0! = 1
# 1! = 1
# 2! = 2
# 3! = 6
# 4! = 24
# 5! = 120

def fact(n):
    if n<2:
        return 1;
    else:
        return n * fact(n-1)

result = fact(5)
print(result)