# Concatation Zahlen werden als strings betrachtet 
num1 = input("enter first num : ")
num2 = input("enter sec. num : ")
res = num1+num2
print(res)


# in Zahlen umwandeln => float oder int 
num3 = input("enter thired num : ")
op = input("enter the operator ")
num4 = input("enter fourth num : ")

if op == "+":
    print(int(num3)+int(num4))
elif op == "-":
    print(int(num3)-int(num4))
elif op == "/":
    print(int(num3)/int(num4))
elif op == "*":
    print(int(num3)*int(num4))
else:
    print("wrong operator")