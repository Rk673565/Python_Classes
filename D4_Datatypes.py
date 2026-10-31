# print("1.data type of an integer, float, string, and Boolean")

# a = 10
# b = 10.5
# c = "Python"
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print("----------------------------------------------------------------------------")

# print("#2. user's name and age as input and display both")

# Name = input('enter your sweat name:- ')
# Age = input('how older you :- ')

# print('name is -',Name)
# print('My age is -',Age)
# print("----------------------------------------------------------------------------")


# print("# 3.two numbers as input and print their sum")

# x=int(input('enter one digit:- '))
# y=int(input('enter one digit:- '))
# print('sum of -',a+b)
# print("----------------------------------------------------------------------------")


# print("# 4 decimal number as input and convert it into an integer")

# dec=float(input('enter decimal number:- '))
# dec_int=int(dec)
# print('int value',dec)
# print("----------------------------------------------------------------------------")


# print("# 5 Create a variable x = 50 and print its value, data type, and ID")

# D = 50

# print("Value:", D)
# print("Data Type:", type(D))
# print("ID:", id(D))
# print("----------------------------------------------------------------------------")


# print("#6 input and display its data type before and after converting it to int")

# BF = input("Enter a number: ")

# print("Before conversion:", type(BF))

# AF = int(BF)

# print("After conversion:", type(AF))

# print("----------------------------------------------------------------------------")

# print("# 7 user's birth year as input and calculate approximate age")

# birth_year = int(input("Enter your birth year: "))

# age = 2026 - birth_year

# print("Approximate Age:", age)
# print("----------------------------------------------------------------------------")


# print("# 8 Take three numbers as input and print their average")

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# c = float(input("Enter third number: "))

# average = (a + b + c) / 3

# print("Average =", average)
# print("----------------------------------------------------------------------------")


# print("# 9 number as input and display its square and cube along with its data type")

# num = int(input("Enter a number: "))

# print("Square =", num ** 2)
# print("Cube =", num ** 3)
# print("Data Type =", type(num))

# print("----------------------------------------------------------------------------")

# print("# 10 Assign the same value to two variables and check whether their IDs are equal")

# a = 50
# b = 50

# print("ID of a:", id(a))
# print("ID of b:", id(b))

# print("Are IDs equal?", id(a) == id(b))

# print("----------------------------------------------------------------------------")

# print("# 11 user's name and marks in three subjects as input and print total and average marks")
# name = input("Enter your name: ")

# m1 = float(input("Enter marks in Subject 1: "))
# m2 = float(input("Enter marks in Subject 2: "))
# m3 = float(input("Enter marks in Subject 3: "))

# total = m1 + m2 + m3
# average = total / 3

# print("Name:", name)
# print("Total Marks:", total)
# print("Average Marks:", average)

# print("----------------------------------------------------------------------------")

# print("# 12  input from the user, convert it into a float, and display its value, type, and ID")

# x = input("Enter a value: ")

# x = float(x)

# print("Value:", x)
# print("Type:", type(x))
# print("ID:", id(x))

x = int(input("enter some value :-  "))
print(id(x))
y = int(input("enter value :-   "))
print(id(y))
print ( x == y)
print (x != y)

print ( x is y)
print (x is not y)
