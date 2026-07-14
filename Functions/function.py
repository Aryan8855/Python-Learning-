# ==========================================
# Topic: Functions
# ==========================================

"""
What is a Function?
-------------------
A function is a reusable block of code that performs a specific task.

Syntax:

def function_name(parameters):
    statements
    return value
"""

# Example 1
def greet():
    print("Welcome to Python")

greet()


# Example 2
def add(a, b):
    print("Sum =", a + b)

add(10, 20)


# Example 3
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication =", result)