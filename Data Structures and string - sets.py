# set
 # set always have a unique value if you enter it will not intake.

s={1,2,3,4,5,6,"nitin",'king'}

print(type(s))
print(s)

# adding int to set s
s.add(10)

print(s)

# rmoving
s.remove(2)
print(s)

# another set s2
s2={1,2,3,4,56,}
# common value between s and s2
print(s & s2)