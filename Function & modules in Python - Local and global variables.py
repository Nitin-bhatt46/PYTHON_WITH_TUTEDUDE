n = 1  # global variable
def fn():
    global n # inside function we create gobal variable.
    n = 5  # local variable
    print('in',n)

fn()

print('out',n)
