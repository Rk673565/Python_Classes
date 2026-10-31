#  Assignment Operator

# 1. Assign 10 to variable a and print it

a = 10
print('value of a ', a)

# 2. Store name, age, and salary and print them
 
name = input("Enter name: ")
age = int(input("Enter age: "))
salary = float(input("Enter salary: "))

print("Name:", name)
print("Age:", age)
print("Salary:", salary)

# 3. Assign the same value to two variables
a = int(input("Enter an integer: "))
b = a

print("a =", a)
print("b =", b)

# 4. Swap two numbers using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)

# 5. Swap two numbers without using a temporary variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)

# 6. Increase a number by 5 using +=

number = int(input("Enter a number: "))

number += 5

print("Result:", number)

# 7. Decrease a number by 3 using -=

number = int(input("Enter a number: "))

number -= 3

print("Result:", number)

# 8. Multiply a number by 4 using *=

number = int(input("Enter a number: "))

number *= 4

print("Result:", number)

# 9. Divide a number by 2 using /=

number = float(input("Enter a number: "))

number /= 2

print("Result:", number)

# 10. Floor divide a number by 3 using //=

number = int(input("Enter a number: "))

number //= 3

print("Result:", number)

# 11. Update a number with remainder after division by 5 using %=

number = int(input("Enter a number: "))

number %= 5

print("Remainder:", number)

#  12. Raise a number to the power of 3 using **=

number = int(input("Enter a number: "))

number **= 3

print("Cube:", number)

# 13. Store student name, age, and marks

student_name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))

print("Student Name:", student_name)
print("Age:", age)
print("Marks:", marks)

#  14. Increase a number three times by 2 using +=

number = int(input("Enter a number: "))

number += 2
number += 2
number += 2

print("Result:", number)

#  15. Calculate total shopping amount using +=

price1 = float(input("Enter price 1: "))
price2 = float(input("Enter price 2: "))
price3 = float(input("Enter price 3: "))

total = 0

total += price1
total += price2
total += price3

print("Total Amount:", total)


#  16. Subtract an expense from bank balance using -=

balance = float(input("Enter balance: "))
expense = float(input("Enter expense: "))

balance -= expense

print("Remaining Balance:", balance)

#  17. Multiply product price by quantity using *=

price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

price *= quantity

print("Total Cost:", price)

#  18. Add bonus marks using +=

marks = int(input("Enter marks: "))
bonus = int(input("Enter bonus marks: "))

marks += bonus

print("Total Marks:", marks)

# 19. Reduce product price by 10% using assignment operator

price = float(input("Enter original price: "))

discount = price * 0.10
price -= discount

print("Discount:", discount)
print("Final Price:", price)

# 20. Apply +=, -=, *=, and //=

number = int(input("Enter a positive integer: "))

number += 5
print("After += 5:", number)

number -= 2
print("After -= 2:", number)

number *= 3
print("After *= 3:", number)

number //= 4
print("After //= 4:", number) 

#  Topic 2: Arithmetic Operators

# 1 Write a Python program to add two numbers.

a = int(input('enter any value:-  '))
b = int(input("enter any value:-  "))

results = a+b
print('sum = ',results)

# 2. Subtract One Number from Another

a = int(input('enter any value:-  '))
b = int(input("enter any value:-  "))

results = a-b

print('sub = ',results)

# 3 Multiply Two Numbers

a = int(input('enter any value:-  '))
b = int(input("enter any value:-  "))

results = a*b

print('product = ',results)

# 4. Divide One Number by Another

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

result = a / b
print("Quotient =", result)

# 5. Floor Division of Two Integers

a = input("Enter first number: ")
b = input("Enter second number: ")

result = a // b
print("division =", result)

# 6. Find Remainder

a = input("Enter first number: ")
b = input("Enter second number: ")

result = a % b
print("remainder =", result)

# 7. Square of a Number

number = int(input("Enter a number: "))

square = number ** 2

print("Square =", square)

# 8. Cube of a Number

number = int(input("Enter a number: "))

cube = number ** 3

print("Cube =", cube)


#  9. Average of Three Numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average =", average)

#  10. Area of a Rectangle

length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width

print("Area of Rectangle =", area)

#  11. Area of a Circle

radius = float(input("Enter radius: "))

area = 3.14 * radius ** 2

print("Area of Circle =", area)

#  12. Celsius to Fahrenheit Conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

#  13. Simple Interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))

interest = (principal * rate * time) / 100

print("Simple Interest =", interest)

#  14. Total Price of Products

quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total_price = quantity * unit_price

print("Total Price =", total_price)

# 15. Total Salary After Bonus

basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))

total_salary = basic_salary + bonus

print("Total Salary =", total_salary)

#  16. Convert Seconds into Minutes and Remaining Seconds

total_seconds = int(input("Enter total seconds: "))

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print("Minutes =", minutes)
print("Remaining Seconds =", remaining_seconds)

# 17. Convert Days into Weeks and Remaining Days

total_days = int(input("Enter total days: "))

weeks = total_days // 7
remaining_days = total_days % 7

print("Weeks =", weeks)
print("Remaining Days =", remaining_days)

#  18. Total and Average Marks of Five Subjects

mark1 = float(input("Enter mark1: "))
mark2 = float(input("Enter mark2: "))
mark3 = float(input("Enter mark3: "))
mark4 = float(input("Enter mark4: "))
mark5 = float(input("Enter mark5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

print("Total Marks =", total)
print("Average Marks =", average)

#  19. Quotient and Remainder

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

quotient = dividend // divisor
remainder = dividend % divisor

print("Quotient =", quotient)
print("Remainder =", remainder)

# 20. Evaluate (a + b) * c / d

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(input("Enter d: "))

result = (a + b) * c / d
print("Result =", result)








