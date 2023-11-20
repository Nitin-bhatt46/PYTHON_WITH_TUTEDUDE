# constructor

class const_dest:
    x=0


    def __init__(self,color,type):
        self.color = color
        self.type = type
        print('constructor')


# destrutor always come at the last no matter where ever you call it , it will only emerge when code is finish.

    def __del__(self):
        print("destructor")

cd=const_dest('black','suv')
cd
print(cd.color)
print(cd.type)