# inheritance
class name:
    x=0
    name=""

    def __init__(self,z):
        self.name =z
        print("hi",z)

class football_fans(name):
    points =0
    def pts(self):
        print(self.name,"scores")

c=football_fans("nitin")
