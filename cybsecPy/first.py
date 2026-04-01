# # taking two inputs at a time
# x,y = input("Enter two values: ").split()
# print("Number of boys: ", x)
# print("Number of girls: ", y)
 
# # taking three inputs at a time
# x, y, z = input("Enter three values: ").split()
# print("Total number of students: ", x)
# print("Number of boys is : ", y)
# print("Number of girls is : ", z)

# name = input("Enter your name: ")
# # print("Hello,", name, "! Welcome!")
# print(name)

# Taking input as string
# color = input("What color is rose?: ")
# print(color)

# Taking input as int
# Typecasting to int
# n = int(input("How many roses?: "))
# print(n)

# Taking input as float
# Typecasting to float
# price = float(input("Price of each rose?: "))
# print(price)

# a = "Hello World"
# b = 10
# c = 11.22
# d = ("Geeks", "for", "Geeks")
# e = ["Geeks", "for", "Geeks"]
# f = {"Geeks": 1, "for":2, "Geeks":3}


# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Eligible");
# else:
#     print("Not Eligible");

# password = ""
# while password != "python123":
#     password = input("Enter the password: ")

# print("Access granted!")



while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Invalid input! Please enter a number.")

print("Thank you! You entered:", age)