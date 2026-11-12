# Operators in python

# 1. Arithmetic Operators
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division

# 2. Comparison Operators
x = 10
y = 5
print(x == y)  # Equal
print(x != y)  # Not Equal
print(x > y)   # Greater Than
print(x < y)   # Less Than
print(x >= y)  # Greater Than or Equal To
print(x <= y)  # Less Than or Equal To

# 3. Logical Operators
p = True
q = False
print(p and q)  # Logical AND
print(p or q)   # Logical OR
print(not p)    # Logical NOT

# 4. Assignment Operators
r = 10
print(r)  # Assignment
r += 5  # Addition Assignment
print(r)

# Subtraction Assignment
r -= 3
print(r)

# Multiplication Assignment
r *= 2
print(r)

# Division Assignment
r /= 4
print(r)

# Modulus Assignment
r %= 3
print(r)

# Exponentiation Assignment
r **= 2
print(r)

# Floor Division Assignment
r //= 2
print(r)

# 5. Bitwise Operators
s = 10  # 1010 in binary
t = 6   # 0110 in binary
print(s & t)  # Bitwise AND
print(s | t)  # Bitwise OR
print(s ^ t)  # Bitwise XOR
print(~s)     # Bitwise NOT
print(s << 1) # Left Shift
print(s >> 1) # Right Shift

# 6. Membership Operators
list1 = [1, 2, 3, 4, 5]
print(3 in list1)    # in Operator
print(6 not in list1)  # not in Operator

# 7. Identity Operators
u = [1, 2, 3]
v = [1, 2, 3]
w = u
print(u is v)  # is Operator
print(u is w)  # is Operator
print(u is not v)  # is not Operator

# 8. Ternary Operator
age = 18
status = "Adult" if age >= 18 else "Not Adult"
print(status)


# 9. Walrus Operator (Python 3.8+)
# The walrus operator allows you to assign a value to a variable as part of an expression
if (n := len(list1)) > 3:
    print(f"List is long with {n} elements")
    
    # 10. Operator Precedence
# Operator precedence determines the order in which operations are performed in an expression.

# Example:
result = 10 + 5 * 2  # Multiplication has higher precedence than addition

print(result)  # Output: 20


# 2.Conditional Expressions(statement expressions)

# Conditional expressions allow you to evaluate a condition and return a value based on the result.
value = "Greater" if 10 > 5 else "Not Greater"
print(value)  # Output: Greater

# 1.if-statements
# The if statement allows you to execute a block of code only if a certain condition is true
age = 18
if age >= 18:
    print("You are an adult.")
    
    # 2.if-else statements
# The if-else statement allows you to execute one block of code if a condition is true
age = 17
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
    
    # 3.if-elif-else statements
# The if-elif-else statement allows you to check multiple conditions and execute different blocks of code based on which condition is true.
age = 20
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
    
    # 4.nested if statements
# Nested if statements allow you to place one if statement inside another if statement.
age = 25
if age >= 18:
    if age < 65:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
        
        
        
        # 2. Loops in python
        # The for loop allows you to iterate over a sequence (such as a list, tuple, or string).
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(fruit)

        # The while loop allows you to execute a block of code as long as a condition is true.
        count = 0
        while count < 5:
            print(count)
            count += 1
            
            # 3. break and continue statements
# The break statement allows you to exit a loop prematurely.
for i in range(10):
    if i == 5:
        break
    print(i)
    
    # The continue statement allows you to skip the rest of the code inside a loop for the current iteration and move on to the next iteration.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
    # 4. pass statement
# The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in situations where a statement is syntactically required but you do not want to execute any code.
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(i)
        
        # 5. else clause in loops
# The else clause in loops is executed when the loop completes normally (i.e., without encountering a break statement).
for i in range(5):
    print(i)
else:
    print("Loop completed without break.")
    
    # 6. Nested loops
# Nested loops are loops within loops. The inner loop is executed for each iteration of the outer loop.
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
        
        # 7. Loop control statements
# Loop control statements allow you to control the flow of a loop. The break and continue statements are examples of loop controlstatements, which have already been covered above.

