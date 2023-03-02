a = input("Enter value of A: ")
b = input("Enter value of B: ")

value = (str(input("Addition, Subraction, Multiplication, Divison: ")))

if value.upper() == str('ADDITION'):
 add = float(a) + float(b)
 print("Sum : " + str(add))

elif value.upper() == str('SUBRACTION'):
 sub = float(a) - float(b)
 print("Sum : " + str(sub))

elif value.upper() == str('MULTIPLICATION'):
 mult = float(a) * float(b)
 print("Sum : " + str(mult))

elif value.upper() == str('DIVISION'):
 div = float(a) / float(b)
 print("Sum : " + str(div))

else:
 print("Invalid Input")
 