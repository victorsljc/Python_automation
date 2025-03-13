"""
Magic Methods in Python

    Magic methods are special methods in Python that start and end with double underscores (e.g., __init__, __str__, __add__).

    They allow you to define how objects of a class behave with built-in Python operations
    (e.g., addition, comparison, string representation).

Common Magic Methods:

        __init__: Initializes an object (constructor).

        __str__: Defines the "informal" string representation of an object (used by print() and str()).

        __repr__: Defines the "official" string representation of an object (used by repr() and the interactive shell).

        __add__: Defines behavior for the + operator.

        __eq__: Defines behavior for the == operator

        __slots__ in Python
        Purpose:

            The __slots__ attribute is used to explicitly declare the attributes that a class can have.

            It restricts the creation of new attributes dynamically, saving memory and improving performance.

            How It Works:

            By default, Python uses a dictionary (__dict__) to store an object's attributes, which consumes extra memory.

            __slots__ replaces the __dict__ with a fixed-size array, reducing memory overhead.

        __call__ Method in Python
            Purpose:

            The __call__ method allows an instance of a class to be called like a function.

            When you define __call__ in a class, you can use the instance as if it were a function.

            How It Works:

            When you call an instance (e.g., instance()), Python internally calls the __call__ method of that instance.

            This makes the object callable.

"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)          # Output: Point(1, 2) (uses __str__)
print(p1 + p2)     # Output: Point(4, 6) (uses __add__)


class Person:
    __slots__ = ["name", "age"]  # Only 'name' and 'age' are allowed as attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name)  # Output: Alice
print(p.age)   # Output: 25

# Attempting to add a new attribute will raise an error
p.address = "123 Street"  # AttributeError: 'Person' object has no attribute 'address'

class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, x):
        return self.value + x

add_five = Adder(5)  # Create an instance
result = add_five(10)  # Call the instance like a function
print(result)  # Output: 15