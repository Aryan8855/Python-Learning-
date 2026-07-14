# ==========================================
# Topic: Operators in Python
# ==========================================

"""
What are Operators?
-------------------
Operators are special symbols used to perform operations on variables and values.

Types of Operators:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
"""

# ==========================================
# 1. Arithmetic Operators
# ==========================================

"""
Arithmetic Operators are used to perform mathematical operations.

Syntax:
result = operand1 operator operand2
"""

a = 10
b = 3

print("===== Arithmetic Operators =====")
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Modulus (%):", a % b)
print("Floor Division (//):", a // b)
print("Exponent (**):", a ** b)


# ==========================================
# 2. Assignment Operators
# ==========================================

"""
Assignment Operators are used to assign values to variables.

Operators:
=
+=
-=
*=
/=
//=
%=
**=
"""

print("\n===== Assignment Operators =====")

x = 10
print("Initial Value:", x)

x += 5
print("After += :", x)

x -= 2
print("After -= :", x)

x *= 3
print("After *= :", x)

x /= 2
print("After /= :", x)

x //= 2
print("After //= :", x)

x %= 3
print("After %= :", x)

x **= 2
print("After **= :", x)


# ==========================================
# 3. Comparison Operators
# ==========================================

"""
Comparison Operators compare two values.

Operators:
==
!=
>
<
>=
<=
"""

print("\n===== Comparison Operators =====")

a = 10
b = 5

print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


# ==========================================
# 4. Logical Operators
# ==========================================

"""
Logical Operators combine multiple conditions.

Operators:
and
or
not
"""

print("\n===== Logical Operators =====")

age = 20
has_id = True

print("AND :", age >= 18 and has_id)
print("OR :", age >= 18 or False)
print("NOT :", not has_id)


# ==========================================
# 5. Identity Operators
# ==========================================

"""
Identity Operators compare whether two variables refer
to the same object.

Operators:
is
is not
"""

print("\n===== Identity Operators =====")

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)


# ==========================================
# 6. Membership Operators
# ==========================================

"""
Membership Operators check whether a value exists in a sequence.

Operators:
in
not in
"""

print("\n===== Membership Operators =====")

fruits = ["Apple", "Banana", "Mango"]

print("'Apple' in fruits :", "Apple" in fruits)
print("'Orange' in fruits :", "Orange" in fruits)
print("'Orange' not in fruits :", "Orange" not in fruits)


# ==========================================
# 7. Bitwise Operators
# ==========================================

"""
Bitwise Operators perform operations on binary numbers.

Operators:
&
|
^
~
<<
>>
"""

print("\n===== Bitwise Operators =====")

a = 5      # 0101
b = 3      # 0011

print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)