from idlelib.rpc import MethodProxy


# example of class

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed} km/h.")

my_car = Car("Tesla", 100)
my_car.drive()  # Tesla is driving at 100 km/h

# inheritance example
# Let a class reuse another class's attributes and methods.

class Vehicle:
    def move(self):
        print("Vehicle is moving.")

class Bike(Vehicle):
    def ring_bell(self):
        print("Ring ring!")

bike = Bike()
bike.move()        # Inherited method
bike.ring_bell()   # Child's own method

# Encapsulation
# Wrap data and restrict direct access to internal state.

class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acct = BankAccount()
acct.deposit(100)
print(acct.get_balance())  # 100

# Polymorphism
# Same method, different behavior depending on the class.

class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())  # Meow
animal_sound(Dog())  # Woof


# There are 5 main types of methods in Python OOP:

# ...........................Instance Method..............
# These operate on instance variables and require an instance of the class.
# Use cases :- To access or modify object-specific data.
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):  # Instance method
        print(f"Hello, my name is {self.name}")

# ......................CLASS METHODS.............................
# They operate on the class itself, not on instances.
# Use case: Access/modify class-level data and Alternative constructors.

class Person:
    species = "Human"

    @classmethod
    def get_species(cls):
        return cls.species

    @classmethod
    def from_string(cls, string):
        name = string.split("-")[0]
        return cls(name)

# ..........................STATIC METHODS...................................
# They don’t access class or instance data.
# Use Case :- Utility/helper methods that belong to a class but don’t need class/object data.

class Math:
    @staticmethod
    def add(x, y):
        return x + y

# .................Constructor method........................
# Used to initialize new objects.
# __init__() is automatically called when a new object is created.
# Sets up the object’s initial state.

class Car:
    def __init__(self, brand):
        self.brand = brand

# ..................Destructor Method.....................
# Called when an object is deleted.
# Usecase :- Not used commonly but Python has automatic garbage collection.

class Demo:
    def __del__(self):
        print("Destructor called")

# ....................🧠 Special (Magic/Dunder) Methods..................
# These start and end with double underscores: __init__, __str__, __len__, etc.
# Usecase :- Customize built-in operations (like print(obj), len(obj), etc.)

class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

a=Book('python')
print(a)

# .............................Complete example ...............................
class BankAccount:
    # Class variable (shared across all accounts)
    bank_name = "Python Bank"
    total_accounts = 0

    # Constructor (initializes each object)
    def __init__(self, owner, balance=0):
        self.owner = owner                # instance variable
        self.__balance = balance          # private variable
        BankAccount.total_accounts += 1   # updating class variable
        print(f"Account created for {self.owner}")

    # Instance method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")

    # Instance method
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    # Instance method (getter)
    def get_balance(self):
        return self.__balance

    # Class method (accessing class-level data)
    @classmethod
    def get_bank_info(cls):
        return f"{cls.bank_name} has {cls.total_accounts} active accounts."

    # Static method (utility function)
    @staticmethod
    def validate_account_number(acc_no):
        return str(acc_no).isdigit() and len(str(acc_no)) == 10

    # Special method (called when object is printed)
    def __str__(self):
        return f"{self.owner}'s account | Balance: ₹{self.__balance}"

    # Destructor (called when object is deleted)
    def __del__(self):
        print(f"Account for {self.owner} is closed.")
        BankAccount.total_accounts -= 1


# -------------------------------
# 🎯 Using the class in action

# Creating accounts
acc1 = BankAccount("Kavya", 1000)
acc2 = BankAccount("Raj", 500)

# Using instance methods
acc1.deposit(300)
acc1.withdraw(200)

# Printing account info
print(acc1)

# Class method usage
print(BankAccount.get_bank_info())

# Static method usage
print("Is valid account number?", BankAccount.validate_account_number("1234567890"))

# Deleting an account (calls __del__)
del acc2

# Final bank info
print(BankAccount.get_bank_info())

# ...........output............
            # Account created for Kavya
            # Account created for Raj
            # 300 deposited. New balance: 1300
            # 200 withdrawn. New balance: 1100
            # Kavya's account | Balance: ₹1100
            # Python Bank has 2 active accounts.
            # Is valid account number? True
            # Account for Raj is closed.
            # Python Bank has 1 active accounts.




