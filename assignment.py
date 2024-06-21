"""
1.
Python is a high-level programming language (It is easily readable by humans).

 It is popular among users because it is versatile(can be used for web design, data analysis, etc),
 is easy to learn, has a large and active community, has plenty of libraries and has cross-platform 
 compatibility.

It is particularly useful for Exploratory Data Analysis (EDA):
Utilize Python's visualization libraries (e.g., Matplotlib, Seaborn) to understand data patterns and 
correlations.

2.(Windows)
Downloading Python;
-Visit python.org
-Locate the downloads tab
-The website will automatically detect you are on windows and suggest the latest available version 
for download
-Click on it and it will download

Installing Python
-Run the installer and locate the downloaded folder
-Add Python to PATH: Ensure that you check the box that says "Add Python to PATH" at the bottom of the 
first installation screen.
-Click on "Customize installation" to proceed.
-Select Optional Features
-Click next
-Click "Install" to begin the installation.
-Wait for the installation to complete and click "Close" once it's done.

Verifying the Installation
-Open Command Prompt:
-Press Win + R, type cmd, and press Enter.
-Verify Python Installation:
Type python --version and press Enter. You should see the Python version number.
Type pip --version and press Enter. This verifies that pip was installed correctly.

To Set up a Virtual Environment
-Navigate to Your Project Directory:
Use the cd command to navigate to the directory where you want to create your virtual environment.
-Create a Virtual Environment:
Run the following command to create a virtual environment:
python -m venv venv
-This will create a directory named venv (you can choose a different name) in your project directory.
-To activate the virtual environment, run
.\venv\Scripts\activate
You should see (venv) at the beginning of the command prompt line, indicating that the virtual environment is active.


""" 
#3
print("Hello, World!")

"""
'print' is a function used to output text to the console
"Hello, World" is a string enclosed inside quotation marks
() used to enclose the arguments that are passed to the print function


4.Data Types
They specify the type of data that can be stored inside a variable, they include:
 x) Numeric - holds numeric data values
 x) String - holds sequence of characters
 x) Sequence - holds a collection on items
 x) Mapping - holds data in key-value pair form
 x) Boolean - holds either true or false
 x) Set - holds collection of unique items

"""
# Numeric Types
integer_var = 10          # int
float_var = 10.5          # float
complex_var = 3 + 4j      # complex

# String
string_var = "Hello, World!"  # str

# Sequence Types
list_var = [1, 2, 3, 4, 5]          # list
tuple_var = (1, 2, 3, 4, 5)         # tuple

# Mapping Type
dict_var = {"name": "Alice", "age": 25}  # dict

# Boolean
boolean_var = True  # bool

# Set Types
set_var = {1, 2, 3, 4, 5}            # set
frozenset_var = frozenset([1, 2, 3, 4, 5])  # frozenset

# Printing the variables
print("Integer:", integer_var)
print("Float:", float_var)
print("Complex:", complex_var)
print("String:", string_var)
print("List:", list_var)
print("Tuple:", tuple_var)
print("Dictionary:", dict_var)
print("Boolean:", boolean_var)
print("Set:", set_var)
print("Frozenset:", frozenset_var)

# Demonstrating operations on some types
print("Sum of integers in list:", sum(list_var))
print("Uppercase string:", string_var.upper())
print("Keys in dictionary:", dict_var.keys())
print("Add element to set:", set_var.add(6))
print("Set after adding an element:", set_var)

5.
#Conditional statements allow you to execute code blocks based on certain conditions. 
# The most common conditional statement is the if-else statement.

age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

#Loops are used to execute a block of code repeatedly. The most common loops in Python are for and while.

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

6.
#Functions are reusable blocks of code that perform a specific task. They help in organizing code, making it more readable and maintainable.
def add(a, b):
    return a + b

# Calling the function
result = add(3, 5)
print("The sum is:", result)

7.
"""
Lists are an Ordered collections of items.
Items are accessed by their index.
Their Syntax: list_name = [item1, item2, item3].

Dictionaries are an Unordered collections of key-value pairs.
Items are accessed by their key.
Their Syntax: dict_name = {'key1': 'value1', 'key2': 'value2'}.
"""
# Creating a list
numbers = [1, 2, 3, 4, 5]

# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Basic operations on the list
numbers.append(6)
print("List after appending:", numbers)
print("Second element in the list:", numbers[1])

# Basic operations on the dictionary
person["age"] = 26
print("Dictionary after updating age:", person)
print("Person's name:", person["name"])


8.
#Exception Handling
"""
Exception handling is used to handle runtime errors gracefully
 without crashing the program. It uses try, except, and finally blocks.
 """
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
finally:
    print("Execution complete.")

9.
#Modules
"""
Modules are files containing Python code that can be imported into other scripts. 
They allow for code reusability and better organization.
"""

import math

# Using functions from the math module
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)


#Packages
"""Packages are directories containing multiple modules. They help in organizing related modules together.
"""

10.
#File I/O
#Reading from a file - Script to Read from a File
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

#Writing to a File - Script to Write to a File
lines = ["Hello, World!", "Welcome to Python programming.", "File I/O operations are simple."]

with open("output.txt", "w") as file:
    for line in lines:
        file.write(line + "\n")
