# ==========================================
# Topic: If Else Statement
# ==========================================

"""
What is If Else?
----------------
Used to make decisions in a program.

Syntax:

if condition:
    statement

elif condition:
    statement

else:
    statement
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")