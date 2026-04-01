print("Jay Shree Ram")

# name="Ram"
# age=5452
# print(name)
# print(age)
# print(f"{name} is {age} years old")

# name="Tony Spark"
# age=51
# is_genius=True
# print(f"{name} is {age} years old")
# print(f"Is {name} a genius? {is_genius}")

# name=input("Enter your name: ")
# age=input("Enter your age: ")
# print("Hello " + name)

# name=input("Tony please tell me  your name as superHero: ")
# print("Hello " + name)

# old_age = input("Enter your old age: ")
# new_age = int(old_age) + 2
# print("Your age after 2 years will be: ", new_age)
# print(float(new_age))
# print(bool(new_age))

# first=input("Enter first number: ")
# second=input("Enter second number: ")
# sum=int(first)+int(second)
# print("The sum of two numbers is: ", sum)

# first=input("Enter first number: ")
# second=input("Enter second number: ")
# sum=first+second
# print(sum)
# print("sum")

# name= "Tony Stark"
# print(name.lower())
# print(name.upper())
# print(name.replace("Tony", "Iron"))
# print(name.capitalize())
# print(name.find("Stark"))
# print(name.count("a"))
# print(name.index("S"))
# print(len(name))
# print(name.isalnum())
# print(name.isalpha())
# print(name.endswith("k"))
# print(name.split(" "))
# print(name.title())
# print(name)
# print("T" in name)
# print("m" in name)
# print("Tony" in name)
# print("tony" in name)

# print(5+2)
# print(5-2)
# print(5*2)
# print(5/2)
# print(5//2)
# print(5**2)
# print(5%2)
# print((5+2)*3)
# print(5+2*3)
# print(7%3+4*2-1)
# print(4**2/2+6*2- (4+6) )

# i=5
# print(i)
# i **= 2
# print(i)
# i %= 2
# print(i)
# i = i + 2
# print(i)
# i += 2
# print(i)
# i -= 2
# print(i)
# i *= 2
# print(i)
# i /= 2
# print(i)
# i //= 2
# print(i)

# result = 4 + 5 * 6 - 8
# print(result)

# print(3<=5)
# print(5<=3)
# print(5==5)
# print(3!=3)

# print(2>3 or 5>2)
# print(2>3 and 5>2)
# print(2<3 and 5>2)
# print(not 2<3 and 5>2)
# print(not 3<=5)

# age = 16
# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# print("Thank you")

# age=12
# if age>=18:
#     print("You are an adult.")
#     print("You can vote.")
# elif age<18 and age>3:
#     print("You are in school.")
# else:
#     print("You are a kid/child.")

# numbers= range(5)
# print(numbers)
# print(range(5))

# for num in numbers:
#     print(num)

# i=1
# while i<=5:
#     print(i)
#     i+=1

# i=1
# while i<=5:
#     print(i * "*")
#     i+=1

# i=5
# while i>=0:
#     print(i * "*")
#     i-=1

# for i in range(1,6):
#     print(i+1)

#list -> collection of items, []
# names = ["Tony", "Steve", "Bruce", "Natasha"]
# print(names)
# print(names[1])
# print(names[-1])
# print(names[0:2])
# names[1] = "Captain America"
# print(names)

# marks = [45, 78, 89, 90, 67]
# print(marks)

# items = [45, "Tony", 67.5, True]
# print(items)

# marks = [45, 78, 89, 90, 67]
# for score in marks:
#     print(score)
# marks.append(95)
# print(marks)
# marks.insert(0, 99)
# print(marks)
# marks.remove(89)
# print(marks)
# marks.pop()
# print(marks)
# marks.sort()
# print(marks)
# print(99 in marks)
# print(91 in marks)
# print(len(marks))

# marks = [45, 78, 89, 90, 67]
# i=0
# while i<len(marks):
#     print(marks[i])
#     i=i+1
# marks.clear()
# print(marks)  

# students = ["Ram", "Shyam", "Mohan", "Hari", "Gita"]
# for student in students:
#     if student == "Hari":
#         break;
#     print(student)

# for student in students:
#     if student == "Hari":
#         continue;
#     print(student)

#tuple -> collection of items which is immutable, ()

# marks = (45, 78, 90, 89, 90, 67)
# print(marks)
# print(marks[2])
# marks[2] = 95  # This will raise an error since tuples are immutable
# print(marks.count(90))
# print(marks.index(89))
# print(marks.index(90))

#set -> collection of unique items, {}, index does not exits, unordered

# marks = {45, 78, 90, 89, 90, 67}
# print(marks)

# for i in marks:
#     print(i)

#Dictionary -> collection of key-value pairs, {}
# student = {
#     "name": "Tony Stark",
#     "age": 51,
#     "is_genius": True,
#     "skills": ["Engineering", "Flying", "Shooting"]
# }

# print(student)
# print(student["name"])
# print(student["skills"][1])
# print(student["age"])
# student["age"] = 52
# print(student)

# marks = {
#     "Math": 95,
#     "Science": 87,
#     "English": 92
# }
# print(marks)
# print(marks["Science"])
# marks["physics"] = 90
# print(marks)
# marks["Math"] = 98
# print(marks)
# marks["Math"] = 99
# print(marks)

#Math

# import math
# print(math.sqrt(16))
# print(dir(math))

# from math import sqrt, pi
# print(sqrt(25))
# print(sqrt(9))
# print(pi)

# from math import *  # means import all functions from math module
# print(sqrt(25))
# print(sqrt(9))
# print(pi)

#
def add(a, b):
    print(a + b)

add_result = add(5, 3)
add(4,5)

#
def print_subtract(a, b=1):
    print(a - b)

print_subtract(4,5)
print_subtract(9,5)
print_subtract(3)
