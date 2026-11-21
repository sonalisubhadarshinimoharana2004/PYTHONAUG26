#1. Encapsulation – Product Management
#Goal: Create a Product class with a private price attribute and methods to update and display the price.
class Product:
    def __init__(self, price):
        self.__price = price

    def update_price(self, new_price):
        self.__price = new_price
        print("Price updated successfully")

    def display_price(self):
        print("Product Price:", self.__price)

p1 = Product(500)
p1.display_price()

p1.update_price(800)
p1.display_price()

#2. Single Inheritance – Library
#Goal: Create a Library parent class and a BookSection child class
class Library:
    def library_info(self):
        print("Welcome to the Central Library")

class BookSection(Library):
    def display_books(self):
        print("Python")
        print("Java")
        print("C++")

obj = BookSection()
obj.library_info()
obj.display_books()

#3. Multiple Inheritance – Smart Home
#Goal: Create two parent classes Light and Fan. A SmartHome class inherits from both
class Light:
    def turn_on_light(self):
        print("Light is ON")

class Fan:
    def turn_on_fan(self):
        print("Fan is ON")

class SmartHome(Light, Fan):
    def smart_control(self):
        print("Smart Home Control")

obj = SmartHome()
obj.turn_on_light()
obj.turn_on_fan()
obj.smart_control()

#4. Multilevel Inheritance – Education
#Goal: Create three classes Education, School, and OnlineSchool and call all inherited methods
class Education:
    def education_info(self):
        print("Education is important")

class School(Education):
    def school_info(self):
        print("School provides education")

class OnlineSchool(School):
    def online_info(self):
        print("Online classes are available")

obj = OnlineSchool()
obj.education_info()
obj.school_info()
obj.online_info()

#5. Hierarchical Inheritance – Vehicles
#Goal: Create one parent class Vehicle and three child classes Car, Bus, and Bike
class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a Car")

class Bus(Vehicle):
    def bus_info(self):
        print("This is a Bus")

class Bike(Vehicle):
    def bike_info(self):
        print("This is a Bike")

obj1 = Car()
obj1.vehicle_info()
obj1.car_info()

obj2 = Bus()
obj2.vehicle_info()
obj2.bus_info()

obj3 = Bike()
obj3.vehicle_info()
obj3.bike_info()

#6. Hybrid Inheritance – Smart Devices
#Goal: Create a parent class Device, two child classes Computer and Television, and a final class SmartDevice inheriting from both.
class Device:
    def device_info(self):
        print("This is a Smart Device")

class Computer(Device):
    def computer_info(self):
        print("This is a Computer")

class Television(Device):
    def television_info(self):
        print("This is a Television")

class SmartDevice(Computer, Television):
    def smart_info(self):
        print("Smart Device is ready")

obj = SmartDevice()
obj.device_info()
obj.computer_info()
obj.television_info()
obj.smart_info()

#7. Polymorphism – Notification System
#Goal: Create EmailNotification, SMSNotification, and PushNotification classes with the same method send() but different messages.
class EmailNotification:
    def send(self):
        print("Sending Email Notification")

class SMSNotification:
    def send(self):
        print("Sending SMS Notification")

class PushNotification:
    def send(self):
        print("Sending Push Notification")

obj1 = EmailNotification()
obj2 = SMSNotification()
obj3 = PushNotification()

obj1.send()
obj2.send()
obj3.send()

#8. Abstraction – Online Booking
#Goal: Create an abstract class Booking with an abstract method confirm_booking(). Implement it in HotelBooking and FlightBooking.
from abc import ABC, abstractmethod

class Booking(ABC):
    @abstractmethod
    def confirm_booking(self):
        pass

class HotelBooking(Booking):
    def confirm_booking(self):
        print("Hotel Booking Confirmed")

class FlightBooking(Booking):
    def confirm_booking(self):
        print("Flight Booking Confirmed")

obj1 = HotelBooking()
obj2 = FlightBooking()

obj1.confirm_booking()
obj2.confirm_booking()

#