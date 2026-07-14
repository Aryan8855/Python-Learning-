# ==========================================
# Topic: Loops
# ==========================================

"""
Loops are used to repeat a block of code.

1. for loop
2. while loop

For Loop Syntax:

for variable in sequence:
    statement

While Loop Syntax:

while condition:
    statement
"""

print("For Loop")

for i in range(1, 6):
    print(i)

print()

print("While Loop")

count = 1

while count <= 5:
    print(count)
    count += 1