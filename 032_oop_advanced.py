from lib.helpers import check_that_these_are_equal

# Let's explore more advanced OOP concepts!

# == Private Variables ==

# In Python, we use a naming convention to indicate that a variable should be
# treated as "private" (not accessed directly from outside the class).
# We prefix the name with an underscore.

class Person:
    def __init__(self, name, age):
        self.name = name          # Public attribute
        self._age = age           # Private attribute (by convention)
            
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age >= 0:  # Validation!
            self._age = age
        else:
            print("Age cannot be negative!")

person = Person("Alice", 25)

# We can still access _age directly (Python doesn't enforce privacy)
print(f"Direct access: {person._age}")

# But we should use the getter/setter methods instead:
print(f"Using getter: {person.get_age()}")
person.set_age(26)
print(f"After setter: {person.get_age()}")

# == Getters and Setters with @property ==

# Python has a cleaner way to create getters and setters using @property:

class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# Now we can use it like a regular attribute:
temp = Temperature()
temp.celsius = 25
print(f"25°C = {temp.fahrenheit}°F")

temp.fahrenheit = 86
print(f"86°F = {temp.celsius}°C")

# == Composition ==

# Composition is when one class contains instances of other classes.
# It's a "has-a" relationship (a Car has an Engine).

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self._is_running = False
    
    def start(self):
        self._is_running = True
        return "Engine started!"
    
    def stop(self):
        self._is_running = False
        return "Engine stopped!"
    
    def is_running(self):
        return self._is_running

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition!
        self._speed = 0
    
    def start(self):
        return self.engine.start()
    
    def accelerate(self):
        if self.engine.is_running():
            self._speed += 10
            return f"Speed is now {self._speed} mph"
        else:
            return "Start the engine first!"
    
    def get_info(self):
        return f"{self.make} {self.model} with {self.engine.horsepower}hp engine"

# Using composition:
my_car = Car("Toyota", "Camry", 200)
print(my_car.get_info())
print(my_car.start())
print(my_car.accelerate())

# @TASK: Create a Library system using composition

# 1. Create a Book class with:
#    - title and author attributes
#    - an _is_checked_out private attribute (starts as False)
#    - check_out() and return_book() methods
#    - is_available() method

class Book:
    # Your code here
    pass

# 2. Create a Library class that:
#    - Contains a list of Book objects
#    - Has an add_book(book) method
#    - Has a find_available_books() method that returns a list of available books
#    - Has a check_out_book(title) method

class Library:
    # Your code here
    pass

# Test your classes:
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library.add_book(book1)
library.add_book(book2)

check_that_these_are_equal(
    len(library.find_available_books()),
    2
)

library.check_out_book("1984")

check_that_these_are_equal(
    len(library.find_available_books()),
    1
)

check_that_these_are_equal(
    library.find_available_books()[0].title,
    "To Kill a Mockingbird"
)

# == Summary ==

# We've learned about:
# - Private variables (prefix with _ or __)
# - Getters and setters (using methods or @property)
# - Composition (objects containing other objects)

# These concepts help us write more robust and maintainable code by:
# - Controlling access to internal data
# - Validating data before it's set
# - Building complex objects from simpler ones

# Congratulations! If you've got this far. 