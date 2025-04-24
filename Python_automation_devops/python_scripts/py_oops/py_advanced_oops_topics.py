"""
🔥 Complete OOP Topics in Python
    ✅ 1. Class & Object (Basics)
            Blueprint (class) and instance (object)

    ✅ 2. Constructor & Destructor
            __init__() for initializing
            __del__() for cleanup

    ✅ 3. Instance, Class & Static Methods
            Explained earlier
            Uses: object-specific, shared data, utility functions

    ✅ 4. Inheritance
            Single
            Multiple
            Multilevel
            Hierarchical
            Hybrid

            class A: pass
            class B(A): pass  # Single
            class C(A, B): pass  # Multiple
    ✅ 5. Polymorphism
            Method Overriding
            Duck Typing
            Operator Overloading (__add__, __lt__, etc.)

    ✅ 6. Encapsulation
            Public (self.x), Protected (self._x), Private (self.__x)
            Use getters/setters with @property

            @property
            def balance(self):
                return self.__balance
    ✅ 7. Abstraction
            Hiding implementation, only showing interface.
            Done using abc module.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    ✅ 8. Magic Methods (Dunder Methods)
            __init__, __str__, __repr__, __len__, __getitem__, etc.

            Enable Python's syntactic sugar and operator overloading.

def __add__(self, other):
    return self.value + other.value
    ✅ 9. Composition
            Has-A relationship (object inside another object)

class Engine: pass

class Car:
    def __init__(self):
        self.engine = Engine()
    ✅ 10. Aggregation
            Weaker form of composition (object exists independently)

    ✅ 11. Inner/Nested Classes
            Define class inside another class.

class Outer:
    class Inner:
        pass
    ✅ 12. Class Variables vs Instance Variables
            self.x = per object
            ClassName.x = shared across all objects

    ✅ 13. Type Annotations & Data Classes (Python 3.7+)

from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    ✅ 14. Mixins
            Small reusable classes for adding features.

class LoggingMixin:
    def log(self, msg):
        print(f"Log: {msg}")
    ✅ 15. Metaclasses (Advanced)
            Class of a class. Controls class creation.
            Mostly for framework or library design.

"""
# 🧠 Python OOP Advanced Topics – With Examples
# .......................INHERITANCE...........................:
class Animal:
    def sound(self): print("Some sound")

class Dog(Animal):
    def sound(self): print("Bark")

Dog().sound()  # Bark


# ....................Multiple Inheritance .............................
class A: pass
class B: pass
class C(A, B): pass


# .....................Polymorphism........................................

class Bird:
    def speak(self): print("Chirp")

class Duck:
    def speak(self): print("Quack")

def talk(obj):
    obj.speak()

talk(Bird())  # Chirp
talk(Duck())  # Quack


# ..........................Encapsulation..............................
class Box:
    def __init__(self):
        self._protected = "semi-private"
        self.__private = "hidden"

    def reveal(self):
        return self.__private

b = Box()
print(b._protected)
print(b.reveal())

# ....................Abstraction(abc module).................................
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * 5 * 5

# ...............................Magic Methods...................................
class Product:
    def __init__(self, price):
        self.price = price

    def __str__(self):
        return f"₹{self.price}"

    def __add__(self, other):
        return self.price + other.price

a = Product(50)
b = Product(70)
print(a + b)  # 120

# ...................Composition.........................................
class Engine:
    def start(self): print("Engine running")

class Car:
    def __init__(self):
        self.engine = Engine()

    def drive(self):
        self.engine.start()

Car().drive()


# ...................Inner class............................
class Outer:
    class Inner:
        def greet(self): print("Hello from Inner")

Outer.Inner().greet()

# .........................class vs instance ..........................
class Example:
    count = 0         # class var

    def __init__(self):
        self.id = Example.count
        Example.count += 1

e1 = Example()
e2 = Example()
print(e1.id, e2.id)  # 0 1

# .................static and class methods ...................................
class Tool:
    version = "1.0"

    @staticmethod
    def greet(): print("Welcome!")

    @classmethod
    def get_version(cls): return cls.version

# ..........................Mixins........................................
class LoggerMixin:
    def log(self): print(f"Logging from {self.__class__.__name__}")

class App(LoggerMixin):
    def run(self): self.log()

App().run()

# .........................data classes......................................
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

u = User("Kavya", 22)
print(u)

# ....................Meta classes ................
class Meta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating {name}")
        return super().__new__(cls, name, bases, dct)

class Custom(metaclass=Meta):
    pass
