# OOP
# Class and Object

# class Employee:
#     name = "Soumya"
#     emp_id = 1
#     salary = 50000
#     dept = "IT"

# emp1 = Employee()
# emp2 = Employee()

# print(emp1.name)
# print(emp1.emp_id)
# print(emp1.salary)
# print(emp1.dept)

# print(emp1.name)



# class Mobile:
#     def __init__(self):
#         self.price = 15000
        
#     def Ringing(self):
#         print("Mobile is ringing...")


# mobile1 = Mobile()

# print(mobile1.price)

# mobile1.Ringing()


# class Employee:
#     name = "Soumya"
#     salary = 50000

#     def _init_(self):
#         self.address = "BBSR"
#         print("Constructer1")


# emp1 = Employee()
# print(emp1.name)
# print(emp1.address)


 
class Employee:                                  #class
    def __init__(self,name,address,salary):     #Constructer
        self.name = name
        self.salary = salary
        self.address = address

    def EmployeeDetails(self):                    #Method
        print("Employee Name",self.name)
        print("Employee Salary",self.salary)
        print("Employee address",self.address)

e1 = Employee(name="Sonali",salary=50000,address="BBSR")
e2 = Employee(name="Soumya",salary=60000,address="KATAK")

# print(e1.EmployeeDetails())
e1.EmployeeDetails()
print(e2.address)


# # CONSTRUCTOR
# class Employee:
#     name = "sonali"
#     salary = 6000

#     def __init__(self):
#         self.address = "BBSR"
#         print("constructor 1")
# emp1= Employee()


# Make a class where i can create multiple object (employee) with name is change but salary will the fix also there will a method that return the name of employee and his/her salart

# {
#     name = "Rahul",
#     salary = 45000
# },
# {
#     name = "Rohit",
#     salary = 45000
# },
# {
#     name = "Raj",
#     salary = 45000
# },
# {
#     name = "Ram",
#     salary = 45000
# },
# {
#     name = "Soumya",
#     salary = 45000
# },

# Output --- My name is ___ salary is 45000



class Employee:

    def __init__(self, name):
        self.name = name
        self.salary = 45000

    def display(self):
        return f"Hii {self.name}, your salary is {self.salary}"


emp1 = Employee("sonali")
emp2 = Employee("Priya")
emp3 = Employee("Ashu")

print(emp1.display())
print(emp2.display())
print(emp3.display())

   

# Calculator with multiple methods like add,sub,mu,div also use constructor

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def multi(self):
        return self.num1 * self.num2
    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Cannot divide by zero"
c1 = Calculator(20, 10)
print("Addition:", c1.add())
print("Subtraction:", c1.sub())
print("Multiplication:", c1.multi())
print("Division:", c1.div())



# Make a class for bank passbook from where a pass holder
#  user can deposit 
# user can withdraw amount
# user can view there balance


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Available Balance:", self.balance)
user1 = BankAccount("Sonali", 10000)

user1.deposit(2000)
user1.withdraw(1000)
user1.check_balance()