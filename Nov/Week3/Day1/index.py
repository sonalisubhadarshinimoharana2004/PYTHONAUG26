# non premitive data types
#List
fruits = ['apple','orange','fruit1','fruit2','fruit3']

for i,fruit in enumerate(fruits):
    print(i+1,"->",fruit)
    
 #Tuple
fruits = ['apple','orange','fruit1','fruit2','fruit3']

for i,fruit in enumerate(fruits):
    print(i+1,"->",fruit)
    
 #Dict
student = {
     "name":"Sonali",
     "age":21,
     "city":"BBSR"
 }  
 
  
for key in student:
    print(key)
    
    
    
    
#Function in python:

#A function is a block of reusable code that performs a specific task.
#We use functions to:
# Reuse code.
# Reduce code repetition.
# Make programs easier to understand.
# Make code organized.

#Example:
#Simple function:
def greet():
    print("Hello, Welcome to Python!")

greet()

#Argument:

#Arguments are the actual values passed to a function when calling it.
#Arguments provide data to a function so that it can perform a task.

#Example:
def add(a, b):
    print(a + b)

add(10, 20)

#Types of Arguments:

# Python has five commonly discussed argument categories:

#1. Positional Arguments
#Values are passed according to their position.
#Example:
def student(name, age):
    print(name)
    print(age)

student("Sonali", 22)

#2. Keyword Arguments:
#Values are passed using parameter names
#Example:
def student(name, age):
    print(name)
    print(age)

student(age=22, name="Sonali")

#3. Default Arguments:
#A default argument has a predefined value
#Example:
def greet(name="Sonali"):
    print("Hello", name)

greet()
greet("Rahul")

#4. Variable-Length Arguments (*args):
#*args allows a function to accept multiple positional arguments.
#Example:
def add(*numbers):
    print(numbers)

add(10, 20, 30, 40)

#5. Keyword Variable-Length Arguments (**kwargs): 
# **kwargs allows a function to accept multiple keyword arguments
#Example:
def student(**details):
    print(details)

student(name="Sonali", age=22, course="MCA")


#Return Statement:

#The return statement is used to send a value back from a function to the place where the function was called.
#It also stops the execution of that function.
#Example:
def add(a, b):
    return a + b

result = add(10, 20)

print(result)


# Return vs Print:
#print():
#display output on the screen
#used to show information
#doednot return the displayed value	

# return:
#sends a value back
#used to reused a result
#return a value to the caller

#1. write a function  with a arg, that return number is even or odd
#Example:
def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_even_odd(10)
print(result)

# (or)

def EvenOdd(number):
    if number %2 ==0:
        return "Number is Even"
    else:
        return "Number is Odd"
res = EvenOdd(100)
print (res)

#2. write a function that take a list of numbers and return the largest number
#Example:
numbers = [10,20,30,500,300,111]
def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [10, 20, 30, 500, 300, 111]

result = find_largest(numbers)

print("Largest number is:", result)

#3.write a function that takes a list of numbera and return largest and  smallest numbers
numbers = [10,20,500,300,111,30,10]
#Example:
def find_smallest(numbers):
    find_smallest = numbers[0]

    for num in numbers:
        if num < find_smallest:
            find_smallest = num

    return find_smallest


numbers = [10, 20, 500, 300,111,30,10]

result = find_smallest(numbers)

print("Smallest number is:", result)

#4. write a function that take a argument as age and return Voting Eligibility
#not eigible
#Eligible
#Just 18
#Example:
def voting_eligibility(age):
    if age < 18:
        return "Not Eligible"
    elif age == 18:
        return "Just 18"
    else:
        return "Eligible"


age = int(input("Enter your age: "))

result = voting_eligibility(age)

print(result)

#5. write a function that takes mark and show grade
#Mark     Grade
#90 - 100 ->A
#80 - 89  ->B
#78 - 79  ->C
#60 - 69  ->D
#50 - 59  ->E
#less the 50 -> Fail

#Example:
def get_grade(mark):
    if mark < 0 or mark > 100:
        return "Invalid mark"
    elif mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:  # Change 70 to 78 if you strictly want 78-79
        return "C"
    elif mark >= 60:
        return "D"
    elif mark >= 50:
        return "E"
    else:
        return "Fail"

# Example usage:
print(get_grade(95))  # Output: A
print(get_grade(78))  # Output: C
print(get_grade(42))  # Output: Fail



#6. write the function that takes a number list and show the  numbers are even or odd 
numbers = [10,11,530,320,111,30,10]
#Example:
def check_even_odd(numbers):
    for num in numbers:
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")


numbers = [10, 11, 530, 320, 111, 30, 10]

check_even_odd(numbers)

#7. write a function  that takes a number list and show how many even and odds are there
numbers = [10,11,530,320,111,30,10]
#Example:
def count_even_odd(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Total Even Numbers:", even)
    print("Total Odd Numbers:", odd)


numbers = [10, 11, 530, 320, 111, 30, 10]

count_even_odd(numbers)

8.
