a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("Enter required operation (+, -, *, /,%): ")
op=input()
if op=='+':
    print("The sum is: ", a+b)
elif op=='-':
    print("The difference is: ", a-b)
elif op=='*':
    print("The product is: ", a*b)
elif op=='/':
    print("The quotient is: ", a/b)
elif op=='%':
    print("The remainder is: ", a%b)
else:
    print("Invalid operation")