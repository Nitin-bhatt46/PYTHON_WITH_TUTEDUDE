
# Exception handiling

try:

    a=2
    b =0
    print(a/b)
except ZeroDivisionError:
    print("there is an error")
finally:
    print("continue with the follwoing code")