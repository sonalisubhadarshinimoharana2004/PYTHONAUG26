# List
#1. Create a list of 10 numbers and print all elements using a for loop.
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for num in numbers:
    print(num)
    
#2. Print only even and odd numbers from a list
numbers = [10, 11, 20, 25, 30, 35, 40, 45]

print("Even Numbers:")

for num in numbers:
    if num % 2 == 0:
        print(num)

print("Odd Numbers:")

for num in numbers:
    if num % 2 != 0:
        print(num)
        
#3. Find the largest and smallest numbers in a list using a loop.
numbers = [10, 20, 30, 500, 300, 111]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest Number:", largest)
print("Smallest Number:", smallest) 

#4. Count how many times a particular number appears in a list.
numbers = [10, 20, 10, 30, 10, 40, 50]

target = 10
count = 0

for num in numbers:
    if num == target:
        count += 1

print("Number of occurrences:", count)  

 #5. Write a function to calculate the sum of all elements in a list without using sum()
def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total

numbers = [10, 20, 30, 40, 50]

result = calculate_sum(numbers)

print("Total Sum:", result)

#6. Find the second-largest number without using sort() or max()
numbers = [10, 20, 30, 500, 300, 111]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest) 

#7. Remove duplicate elements without using set() 
numbers = [10, 20, 10, 30, 20, 40, 50]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("List without duplicates:", unique)  

#8. Separate positive, negative and zero values into three different lists.
numbers = [10, -20, 0, 30, -40, 0, 50]

positive = []
negative = []
zero = []

for num in numbers:
    if num > 0:
        positive.append(num)

    elif num < 0:
        negative.append(num)

    else:
        zero.append(num)

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

#9. Find common elements between two lists without using intersection().
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common Elements:", common)

#10. Write a function to check whether a list is a palindrome. 
def check_palindrome(numbers):
    if numbers == numbers[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

numbers = [10, 20, 30, 20, 10]

result = check_palindrome(numbers)

print(result)

    
# Tuple

#1. Create a tuple of 10 numbers and print all elements using a for loop.
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

for num in numbers:
    print(num)

#2. Print all elements along with their index using enumerate().
numbers = (10, 20, 30, 40, 50)

for index, num in enumerate(numbers):
    print(index, num)

#3. Find the largest and smallest numbers in a tuple using a loop.
numbers = (10, 20, 30, 500, 300, 111)

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

#4. Count how many times a particular number appears using count().
numbers = (10, 20, 10, 30, 10, 40, 50)

target = 10

result = numbers.count(target)

print("Count:", result)

#5. Calculate the sum of all tuple elements without using sum().
numbers = (10, 20, 30, 40, 50)

total = 0

for num in numbers:
    total += num

print("Total Sum:", total)

#6. Find the second-largest number in a tuple without using sort() or max().
numbers = (10, 20, 30, 500, 300, 111)

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)

#7. Find all duplicate elements in a tuple.
numbers = (10, 20, 30, 10, 40, 20, 50)

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Duplicate Elements:", duplicates)

#8. Check whether a tuple is a palindrome without using slicing.
def check_palindrome(numbers):
    start = 0
    end = len(numbers) - 1

    while start < end:
        if numbers[start] != numbers[end]:
            return "Not Palindrome"

        start += 1
        end -= 1

    return "Palindrome"

numbers = (10, 20, 30, 20, 10)

print(check_palindrome(numbers))

#9. Find the common elements between two tuples using loops.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)

common = []

for num in tuple1:
    if num in tuple2 and num not in common:
        common.append(num)

print("Common Elements:", common)

#10. Separate even and odd numbers from a tuple into two different lists.
numbers = (10, 11, 20, 25, 30, 35, 40, 45)

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even Numbers:", even)
print("Odd Numbers:", odd)


#Set

#1. Create a set of 10 numbers and print all elements using a for loop.
numbers = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}

for num in numbers:
    print(num)
    
#2. Create two sets and find their union.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.union(set2)

print("Union:", result)

#3. Find the common elements between two sets using intersection().
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = set1.intersection(set2)

print("Common Elements:", result)

#4. Find the difference between two sets using difference().
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result = set1.difference(set2)

print("Difference:", result)

#5. Find the largest and smallest numbers in a set using a loop.
numbers = {10, 20, 30, 500, 300, 111}

largest = float('-inf')
smallest = float('inf')

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)

#6. Find common elements between two sets without using intersection().
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

common = set()

for num in set1:
    if num in set2:
        common.add(num)

print("Common Elements:", common)

#7. Find the union of two sets without using union().
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

result = set1.copy()

for num in set2:
    result.add(num)

print("Union:", result)

#8. Check whether two sets are equal without using the == operator.
set1 = {10, 20, 30, 40}
set2 = {40, 30, 20, 10}

if len(set1) == len(set2):
    if set1.issubset(set2):
        print("Both sets are equal")
    else:
        print("Both sets are not equal")
else:
    print("Both sets are not equal")

#9. Find the elements that are present in exactly one of three sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
set3 = {40, 60, 70, 80}

result = set()

for num in set1 | set2 | set3:
    count = 0

    if num in set1:
        count += 1

    if num in set2:
        count += 1

    if num in set3:
        count += 1

    if count == 1:
        result.add(num)

print("Elements present in exactly one set:", result)

#10. Find the common characters between two strings using sets.
str1 = "python"
str2 = "programming"

set1 = set(str1)
set2 = set(str2)

common = set1.intersection(set2)

print("Common Characters:", common)


#Dictionary

#1. Create a dictionary containing 5 students and their marks. Print all keys and values using a loop.
students = {
    "Sonali": 85,
    "Rahul": 70,
    "Priya": 90,
    "Amit": 65,
    "Sneha": 80
}

for name, marks in students.items():
    print(name, ":", marks)
    
#2. Add a new key called city to an existing dictionary.
student = {
    "name": "Sonali",
    "age": 22,
    "course": "MCA"
}

student["city"] = "Bhubaneswar"

print(student)

#3. Update the marks of a particular student.
students = {
    "Sonali": 85,
    "Rahul": 70,
    "Priya": 90
}

students["Rahul"] = 95

print(students)

#4. Find the total marks of all students without using sum().
students = {
    "Sonali": 85,
    "Rahul": 70,
    "Priya": 90,
    "Amit": 65,
    "Sneha": 80
}

total = 0

for marks in students.values():
    total += marks

print("Total Marks:", total)

#5. Count how many students passed and failed. Consider 40 as the passing mark.
students = {
    "Sonali": 85,
    "Rahul": 30,
    "Priya": 90,
    "Amit": 25,
    "Sneha": 80
}

passed = 0
failed = 0

for marks in students.values():
    if marks >= 40:
        passed += 1
    else:
        failed += 1

print("Passed Students:", passed)
print("Failed Students:", failed)

#6. Find the student with the highest and lowest marks without using max() or min().
students = {
    "Sonali": 85,
    "Rahul": 70,
    "Priya": 90,
    "Amit": 65,
    "Sneha": 80
}

highest = float('-inf')
lowest = float('inf')

topper = ""
lowest_student = ""

for name, marks in students.items():

    if marks > highest:
        highest = marks
        topper = name

    if marks < lowest:
        lowest = marks
        lowest_student = name

print("Highest Marks:", topper, highest)
print("Lowest Marks:", lowest_student, lowest)

#7. Find the second-highest marks from a student dictionary.
students = {
    "Sonali": 85,
    "Rahul": 70,
    "Priya": 90,
    "Amit": 65,
    "Sneha": 80
}

highest = float('-inf')
second_highest = float('-inf')

for marks in students.values():

    if marks > highest:
        second_highest = highest
        highest = marks

    elif marks > second_highest and marks != highest:
        second_highest = marks

print("Second Highest Marks:", second_highest)

#8. Create a new dictionary containing only students who scored more than 75.
students = {
    "Sonali": 85,
    "Rahul": 70,
    "Priya": 90,
    "Amit": 65,
    "Sneha": 80
}

result = {}

for name, marks in students.items():
    if marks > 75:
        result[name] = marks

print(result)

#9. Find the frequency of each character in a string and store it in a dictionary.
text = "python programming"

frequency = {}

for char in text:
    if char != " ":
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print(frequency)

#10. Merge two dictionaries without using the update() method.
dict1 = {
    "name": "Sonali",
    "age": 22
}

dict2 = {
    "city": "Bhubaneswar",
    "course": "MCA"
}

result = {}

for key, value in dict1.items():
    result[key] = value

for key, value in dict2.items():
    result[key] = value

print(result)