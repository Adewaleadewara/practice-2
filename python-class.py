# === Common Command Line Statements ===
## Windows

# - cd - Change Directory
# ----- cd <Name of the directory/folder>
# ----- cd .. - Going a Step backward
# ----- cd / - Going to root directory

# - dir - Listing Directory
# -mkdir - Make Directory
# ----- mkdir <Name the folder>

## == MacOS == (On Mac not Windows)
# - cd - Change Directory
# ------ cd <Name of directory/folder>
# ------ cd .. - Going a step backward
# ------ cd ~ - Going to root directory

# ls - List Directory
# ls -a - List all

# - mkdir - Make Directory
# ------ mkdir <Name the folder>


# =============================== PYTHON ==============================


# Basic Synthax
# print(2/2)


# # ============== Variables ==============
# # Variables is a container that stores data values
# number1 = 2
# number2 = 4
# print(number1 / number2)

# x =3
# print(x)

# # ============== Do's and Don't in naming a variable ==============
# # Do not start a variable name with a number
# # Do not start with a symbol except in special cases which involve the use of underscore(_)
# # Readability i.e always write meaningful variable names
# x = 23 # Not Adviced
# y = 54 # Not Adviced
# # Do not add spaces when naming your variable

# # ============ Naming Styles ============
# # PascalCase - Use to define classes
# TotalAmount = 10
# TotalAverageOfStuents = 10000


# # camelCase - Use to define variables and functions
# totalAmount = 120
# totalAverageOfStudents = 13000


# # snake_case - Used for mostly variables
# dollar_amount = 15

# To comment on multiple lines of codes at a time use ctrl or cmd + /
# ====== Input & Output Operations ======
firstName = input('What is your first name: ')
middleName = input('Your other name: ')
lastName = input('Your surname: ')
profession = input('What do you do for a living? ')
location = input('Where you stay currently? ')
# For a input and output response you concatenate
#Concatenation is the process of joining two or more strings to form a single string.

print('Hello! ' + firstName, middleName, lastName)
print('Profession: ' + profession)
print('Where are you presently? ' + location)