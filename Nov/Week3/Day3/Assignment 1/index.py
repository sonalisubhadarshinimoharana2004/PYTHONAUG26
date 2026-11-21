#Question 1 – Book Details
#Task: Create a Book class with book name, author name and price. Use a constructor to initialize the values and a method to display book details.
class Book:
    def __init__(self, book_name, author_name, price):
        self.book_name = book_name
        self.author_name = author_name
        self.price = price

    def display_details(self):
        print("Book Name:", self.book_name)
        print("Author Name:", self.author_name)
        print("Price:", self.price)

b1 = Book("Python Programming", "Guido van Rossum", 500)
b1.display_details()

#Question 2 – Rectangle
#Task: Create a Rectangle class with length and width. Create methods to calculate area and perimeter.
# Area = length × width
# Perimeter = 2 × (length + width)
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area:", self.length * self.width)

    def perimeter(self):
        print("Perimeter:", 2 * (self.length + self.width))

r1 = Rectangle(10, 5)
r1.area()
r1.perimeter()

#Question 3 – Movie Ticket
#Task: Create a MovieTicket class with movie name and ticket price. Display movie details and calculate total price for multiple tickets.
class MovieTicket:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price

    def display_details(self):
        print("Movie Name:", self.movie_name)
        print("Ticket Price:", self.ticket_price)

    def total_price(self, quantity):
        total = self.ticket_price * quantity
        print("Total Price:", total)

m1 = MovieTicket("Avatar", 250)
m1.display_details()
m1.total_price(3)

#Question 4 – Electricity Bill
#Task: Create an ElectricityBill class with customer name and units consumed. Calculate the bill at ₹5 per unit.
class ElectricityBill:
    def __init__(self, customer_name, units):
        self.customer_name = customer_name
        self.units = units

    def calculate_bill(self):
        bill = self.units * 5
        print("Customer Name:", self.customer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill:", bill)

e1 = ElectricityBill("Sonali", 200)
e1.calculate_bill()

#Question 5 – Shopping Cart
#Task: Create a ShoppingCart class with product name, price and quantity. Display product details, calculate total price and apply a 10% discount if the total exceeds ₹5,000.
class ShoppingCart:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        print("Product Name:", self.product_name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def calculate_total(self):
        total = self.price * self.quantity

        if total > 5000:
            discount = total * 0.10
            final_price = total - discount
            print("Total Price:", total)
            print("Discount:", discount)
            print("Final Price:", final_price)
        else:
            print("Total Price:", total)
            print("No Discount")

c1 = ShoppingCart("Laptop", 6000, 1)
c1.display_details()
c1.calculate_total()