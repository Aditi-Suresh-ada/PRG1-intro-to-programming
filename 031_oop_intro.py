from lib.helpers import check_that_these_are_equal

# Welcome to Object-Oriented Programming (OOP)!

# So far, we've been working with functions and data separately. But sometimes
# it makes sense to bundle them together. That's where classes come in.

# Think of a class as a blueprint for creating objects. An object is a bundle
# of data (called attributes) and functions (called methods) that work together.

# Let's start with a simple example - a Dog class:

class Dog:
    # This special method is called when we create a new Dog
    # It's called the "constructor" or "initialiser"
    def __init__(self, name, age):
        self.name = name  # self.name is an attribute
        self.age = age    # self.age is another attribute
    
    # This is a method - a function that belongs to the class
    def bark(self):
        return f"{self.name} says Woof!"
    
    def describe(self):
        return f"{self.name} is {self.age} years old"

# Now let's create some Dog objects (also called "instances"):

my_dog = Dog("Buddy", 3)
your_dog = Dog("Luna", 5)

# We can access attributes using dot notation:
print(f"My dog's name is {my_dog.name}")
print(f"Your dog is {your_dog.age} years old")

# We can call methods on objects:
print(my_dog.bark())
print(your_dog.describe())

# == The 'self' parameter ==

# Notice that every method has 'self' as its first parameter? That's how
# methods know which object they're working with. Python passes it automatically:

# When we call my_dog.bark(), Python actually calls Dog.bark(my_dog)

# @TASK: Add a birthday method to the Dog class above that:
# - Increases the dog's age by 1
# - Returns a string like "Happy birthday Buddy! Now 4 years old!"

# Test your method here:
# original_age = my_dog.age
# birthday_message = my_dog.birthday()
# print(birthday_message)
# print(f"Age changed from {original_age} to {my_dog.age}")

# == Creating your own class ==

print("\n--- Your Turn ---")

# @TASK: Create a BankAccount class with:
# - An __init__ method that takes an initial balance
# - A balance attribute
# - A deposit method that adds money to the balance
# - A withdraw method that removes money (if there's enough)
# - A get_balance method that returns the current balance

class BankAccount:
    # Your code here
    pass

# Test your BankAccount class:
account = BankAccount(100)

check_that_these_are_equal(
    account.get_balance(),
    100
)

account.deposit(50)
check_that_these_are_equal(
    account.get_balance(),
    150
)

account.withdraw(30)
check_that_these_are_equal(
    account.get_balance(),
    120
)

# This should not change the balance (insufficient funds)
account.withdraw(200)
check_that_these_are_equal(
    account.get_balance(),
    120
)

# == Why use classes? ==

# Classes help us:
# 1. Organise related data and functions together
# 2. Create multiple instances with their own data
# 3. Model real-world objects in our code
# 4. Write cleaner, more maintainable programs

# When you're ready, move on to 032_oop_advanced.py