print("----------Simple Calculator-------------")

a=float(input("Enter the first number: "))
b=float(input("Enter the second nuber: "))
c=input("Enter the operator(+,/,*,-,%): ")

if c=="+":
    print("Result is: ",a+b)
elif c=="-":
    print("Result is: ",a-b)
elif c=="*":
    print("Result is: ",a*b)
elif c=="/":
    print("Result is: ",a/b)
elif c=="%":
    print("Result is: ",a%b)
else:
    print("Invalid Operator")