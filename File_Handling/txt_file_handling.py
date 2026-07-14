# ==========================================
# Topic: Text File Handling
# ==========================================

"""
Text File Handling is used to create, read, write and append data in text files.

Common Modes

"r"  -> Read
"w"  -> Write (Creates file if it doesn't exist)
"a"  -> Append
"x"  -> Create new file

Syntax:

open("file_name.txt", "mode")
"""

# ==========================================
# 1. Create a Text File
# ==========================================

file = open("student.txt", "w")
file.write("Hello Aryan\n")
file.close()

print("File Created Successfully")


# ==========================================
# 2. Read a Text File
# ==========================================

file = open("student.txt", "r")
content = file.read()
print(content)
file.close()


# ==========================================
# 3. Write into a Text File
# ==========================================

file = open("student.txt", "w")
file.write("Python is Awesome!")
file.close()

print("Data Written Successfully")


# ==========================================
# 4. Append into a Text File
# ==========================================

file = open("student.txt", "a")
file.write("\nLearning File Handling")
file.close()

print("Data Appended Successfully")