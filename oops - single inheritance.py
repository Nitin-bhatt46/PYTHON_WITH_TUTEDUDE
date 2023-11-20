# type of inheritance

# single
# multi
# multiple


class A :
    def  state_1(self):
        print("state1")
    def  state_2(self):
        print("state2")
    def  state_3(self):
        print("state3")

class B(A):
    def  state_4(self):
        print("state4")
    def  state_5(self):
        print("state5")

b=B()
b.state_1()
b.state_2()