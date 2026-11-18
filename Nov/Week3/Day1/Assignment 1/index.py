#Function
#1.Create a function to check whether a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_even_odd(10)
print(result)

#2. Create a function to find the largest of three numbers
def largest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

result = largest_number(10, 50, 30)
print("Largest Number:", result)

#3. Create a function to calculate factorial
def factorial(num):
    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

result = factorial(5)
print("Factorial:", result)

#4.Create a function to check whether a number is prime
def check_prime(num):
    if num <= 1:
        return "Not Prime"

    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"

    return "Prime Number"

result = check_prime(7)
print(result)

#5.Create a function to reverse a string.
def reverse_string(text):
    return text[::-1]

result = reverse_string("Python")
print("Reversed String:", result)

#6.Create a function to calculate the sum of all elements in a list
def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)
print("Total Sum:", result)

#7.Create a calculator using separate functions for addition, subtraction, multiplication, and division
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("Addition:", addition(10, 5))
print("Subtraction:", subtraction(10, 5))
print("Multiplication:", multiplication(10, 5))
print("Division:", division(10, 5))

#8.Create a function using *args to calculate the sum of multiple numbers.
def calculate_sum(*args):
    total = 0

    for num in args:
        total += num

    return total

result = calculate_sum(10, 20, 30, 40, 50)

print("Total Sum:", result)

#9. Create a function using **kwargs to display student details
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(
    name="Sonali",
    age=22,
    course="MCA",
    city="Bhubaneswar"
)

#10.Create a recursive function to calculate the Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")