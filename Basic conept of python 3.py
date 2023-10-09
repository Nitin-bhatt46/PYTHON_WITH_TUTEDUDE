# celcius ---> farenheit

c = input("ceclis: ")
c = float(c)
f = (c*9/5)+32
print(f"Farenheit {f}")


# farenheit ---> celcius

f = input("farenheit: ")
f = float(f)
c = (f-32) * 5/9
print(f"celcius {c}")


# interest calculator
# eqautaion pnr/100
p = input("enter :")
n = input("no. of days:")
r = input("rate of interest: ")

p = int(p)
n = int(n)
r = int(r)
si=(p*n*r)/100
print(f"Simple interest is (si")


## in built function

print(max(1,2,3,4,5,6))
print(min(1,2,3,4,5))
print(abs(-2020))
print(pow(2,4))
# pow = power ( number , power)