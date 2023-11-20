class A :
    def  state_1(self):
        print("state 1")
    def  state_2(self):
        print("state 2")
    def  state_3(self):
        print("state 3")

class B(A):
    def  state_4(self):
        print("state 4")
    def  state_5(self):
        print("state 5")

class C(B):
    def  state_6(self):
        print("state 6")
    def  state_7(self):
        print("state 7")

c=C()
c.state_1()
c.state_4()
c.state_6()