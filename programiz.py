# 1. Python Program to Print Hello World!

print('Hello world!')


# 2. Python Program to Add Two Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2

print("The sum is", sum)


# 3. Python Program to Find the Square Root

num = float(input("Enter a number: "))

num_sqrt = num ** 0.5

print("The square root is", num_sqrt)


# 4. Python Program to Calculate the Area of a Triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print("The area of the triangle is", area)


# 5. Python Program to Solve Quadratic Equation

import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b ** 2) - (4 * a * c)

sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print("The solutions are", sol1, "and", sol2)


# 6. Python Program to Swap Two Variables

x = input("Enter first variable: ")
y = input("Enter second variable: ")

x, y = y, x

print("After swapping:")
print("x =", x)
print("y =", y)


# 7. Python Program to Generate a Random Number

import random

print(random.randint(0, 9))


# 8. Python Program to Convert Kilometers to Miles

kilometers = float(input("Enter value in kilometers: "))

conversion_factor = 0.621371

miles = kilometers * conversion_factor

print("%0.2f kilometers is equal to %0.2f miles" % (kilometers, miles))


# 9. Python Program to Convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 1.8) + 32

print("%0.2f Celsius is equal to %0.2f Fahrenheit" % (celsius, fahrenheit))


# 10. Python Program to Check if a Number is Positive, Negative or 0

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# 11. Python Program to Check if a Number is Odd or Even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


    # 12. Python Program to Check Leap Year

year = int(input("Enter a year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


# 13. Python Program to Find the Largest Among Three Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)


# 14. Python Program to Check Prime Number

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


# 15. Python Program to Print All Prime Numbers in an Interval

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# 16. Python Program to Find the Factorial of a Number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)


# 17. Python Program to Display the Multiplication Table

num = int(input("Display multiplication table of: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# 18. Python Program to Print the Fibonacci Sequence

nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


# 19. Python Program to Check Armstrong Number

num = int(input("Enter a number: "))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# 20. Python Program to Find Armstrong Number in an Interval

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)