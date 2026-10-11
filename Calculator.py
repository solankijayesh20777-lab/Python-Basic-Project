a = int(input("Enter 1st Number -> "))
b = int(input("Enter 2nd B=Number -> "))
op = input("Enter Oprators-> ")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
elif op == "%":
    print(a%b)
elif op == "**":
    print(a**b)
else:
    print("Invalid Oprators")
