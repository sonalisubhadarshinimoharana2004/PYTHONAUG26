# 1.Operators in python

# 1.Add two numbers using arithmetic operators.
a = 5
b = 10
c = a + b
print(c)


#2. Calculate the remainder of two numbers using modulus operator.
x = 15
y = 4
z = x % y
print(z)


#3.calculate the square of a number
num = 5
square = num ** 2
print(square)

#4.compare two numbers using comparison operators.
m = 10
n = 15
print(m > n)  # Greater than
print(m < n)  # Less than
print(m == n)  # Equal to
print(m != n)  # Not equal to

#5.check whether a number is between 10 and 50 using logical operators.
number = 30
print(10 < number < 50)  # Using chained comparison operators




# 2. Conditional Statements in Python

#1.wap to check whether a number is positive or negative.
num = 10
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    
# 2. wap to check whether a number is even or odd.
num = 7
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
    
    #3. Check voting eligibility.
age = 20
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
    #4.find the largest of two numbers.
num1 = 10
num2 = 20
if num1 > num2:
    print("The largest number is:", num1)
else:
    print("The largest number is:", num2)
    
    #5.calculate grades based on marks.
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")
    
    #6.check whether a number is positive, negative or zero.
num = -5
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
    #7.simple calculator using if-elif-else statements.
num1 = 10
num2 = 20
operation = "+"

if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    result = num1 / num2
    print("Result:", result)
    
    
    
    # 3. Loops in Python
    
    #1. Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
    
    #2. Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    
    
    #3. Print even numbers from 2 to 20 using a for loop.
for i in range(2, 21, 2):
    print(i)
    
    
    #4. Print odd numbers from 1 to 20 using a for loop.
for i in range(1, 21, 2):
    print(i)
    
    #5. print the multiplication table of any number using a for loop.
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
    
    
    #6. print numbers from 5 to 25 with a step of 5 using a for loop.
for i in range(5, 26, 5):
    print(i)
    
    
    #7. print numbers in reverse order from 5 to 1 using a for loop.
for i in range(5, 0, -1):
    print(i)
    
    
    #8. calculate the sum of numbers from 1 to 10 using a for loop.
total = 0
for i in range(1, 11):
    total += i
print("The sum of numbers from 1 to 10 is:", total)


    #9. print the following number patterns
1
2
3
4
5

for i in range(1, 6):
    print(i)
    
    #10. print the following number patterns 
for i in range(1, 6):
    print("*" * i)

   