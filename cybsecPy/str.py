# name="warner"
# friend="Michael"
# anotherFriend="David"
# apple= '''He said,
# Hi Harry
# hey I am good
# "I want to eat an apple
# '''
# print("Hello, "+ name)
# print(apple)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# print("Lets use a for loop\n")
# for character in apple:
#     print(character)

# string slicing
# print("String Slicing:")  

# names="Harry,Shubham"
# print(len(names))
# a=len(names)
# print(float(a))
# print(int(a))
# a=int(len(names))
# print(float(a))

# fruit="Mango"
# mangoLen=len(fruit)
# print(mangoLen)
# print(fruit[0:4])
# print(fruit[1:4]) #including 1 but not 4
# print(fruit[:])  #means 0:5
# print(fruit[:5]) #means 0:5
# print(fruit[0:-3]) #0:-3 means 0:len(fruit)-3
# print(fruit[-3:-1]) #means len(fruit)-3 : len(fruit)-1 i.e 2:4

# operation on string
print("--------STRING OPERATION----------")
# strings are immutable in python
# upper ya lower function us string ko upper ya lower me convert nahi karta 
#but new string upper ya lower letter ka bana deta hai.

a="Harry"
print(len(a))
print(a.upper())
print(a.lower())

b="!!!!Mohan!!!!"
print(b.rstrip("!"))
print(a.replace("Mohan","John"))