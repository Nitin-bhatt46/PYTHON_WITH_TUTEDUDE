
marks = int(input("enter your marks out of 100"))
if marks > 85:
    print("you are pass and grade is A")
elif marks > 75:
    print("you are pass and grade is B")
elif marks > 45:
    print("you are pass and grade is C")
elif marks > 33:
    print("you are pass and grade is D")
else:
    print("you are fail")




# calculator

operand_1 = int(input("enter the operand_1: "))
operand_2 = int(input("enter the operand_2: "))
operator = input("enter the operator (+,-<*,/)")

if operator == '+':
    print(operand_1 + operand_2)
elif operator == '-':
    print(operand_1 - operand_2)
elif operator == '*':
    print(operand_1 * operand_2)
elif operator == '/':
    print(operand_1 / operand_2)
else:
    print("invalid option")