# Documentation
## What/Why Programming 
First, let's understand what programming is and why we use it. Programming is a way to give instructions to a computer. We create computer programs by writing code that automates tasks. You can think of programming languages as a way to communicate with computers, much like we use languages like Hindi or English to communicate with each other. Just as you understand the language I'm speaking in, computers have their own languages that they understand. Some of these languages include Python, C++, Java, JavaScript, Go, and more. We use these languages because computers don't understand human languages like Hindi or English. So, we learn the computer's language to be more efficient and get our work done faster and more effectively.
## What/Why Python ?
### What is Python?
Python is a versatile and user-friendly programming language known for its simplicity and readability. It is a high-level, general-purpose language that can be used for a wide range of applications.
### Why Python?
1. **Simplicity:** Python's clean and concise syntax makes it easy to read and write code, reducing the chance of errors and saving time.
2. **Versatility:** Python can be used for web development, data analysis, machine learning, scientific computing, and more.
3. **Community:** It has a large and active developer community, providing extensive libraries and packages for various tasks.
4. **Cross-Platform:** Python is compatible with different operating systems, ensuring code can run on multiple platforms.
5. **Educational Value:** Python is widely used for teaching programming and computer science due to its simplicity and readability.
6. **Business Applications:** Python is a preferred choice for building prototypes, automation scripts, and large-scale applications in the business world.

## Comments 
Comments in Python are used to explain the code and provide additional information. They are not executed by the interpreter and are solely for the benefit of programmers to understand the code. Comments are ignored by the Python interpreter.
### Single-Line Comments
Single-line comments are created using the `#` symbol. Anything following `#` on the same line is considered a comment.
```python
# This is a single-line comment.
print("Hello, World")  # This is also a comment after code.
```
### Multi-Line Comments
Python doesn't have a specific syntax for multi-line comments. However, you can use triple-quotes (`'''` or `"""`) to create multi-line strings, and these strings are often used for multi-line comments.
```python
'''
This is a
multi-line comment.
'''
```
### Purpose of Comments
1. **Documentation**: Comments help document the code, explaining its purpose, how it works, and any relevant information for other programmers.
2. **Debugging**: Comments can be used to temporarily disable a piece of code for debugging purposes without removing it.
3. **Clarity**: They make the code more readable by providing context and explanations for complex or non-obvious sections of code.
4. **Future Reference**: Comments serve as a reference for the programmer who may revisit the code later, helping them understand their own code.
Remember to use comments sparingly, as overly commented code can become cluttered and harder to read. Use them where necessary to make your code more understandable to you and other developers.

### Variables and Data Types
In Python, variables are used to store and manipulate data. Python supports various data types to represent different kinds of information. Here's a brief overview of variables and common data types:

### Variables
Variables are containers for storing data values. They can hold different types of data, and you can change the data they store during the program's execution. To declare a variable, use the following syntax:
```python
variable_name = value
```
#### Example
```python
name = "Jocefyneroot"  # Here, "name" is a variable containing a string value "Jocefyneroot".
age = 30       # "age" is a variable containing an integer value 30.
```
### Common Data Types
Python has several built-in data types, but here are some of the most commonly used ones:
#### 1. Integer (`int`)
Used for whole numbers (positive and negative) without a decimal point.
```python
age = 25
```
#### 2. Float (`float`)
Used for numbers with a decimal point or in exponential form.
```python
height = 5.7
```
#### 3. String (`str`)
Used to represent text data.
```python
name = "Alice"
```
#### 4. Boolean (`bool`)
Represents either `True` or `False`.
```python
is_student = True
```
#### 5. List
A collection of values that can be of different data types, enclosed in square brackets `[]`.
```python
fruits = ["apple", "banana", "cherry"]
```
#### 6. Tuple
Similar to a list but immutable, enclosed in parentheses `()`.
```python
coordinates = (3, 4)
```
#### 7. Dictionary
Stores data in key-value pairs, enclosed in curly braces `{}`.
```python
person = {"name": "Jocefyneroot", "age": 28}
```
These data types are the building blocks of Python programming, allowing you to work with a wide range of information efficiently. You can also create custom data types using classes.
Remember to choose the appropriate data type based on the kind of information you need to work with. Python's dynamic typing system allows variables to change their data type dynamically during runtime.

## Operators
Operators in Python are special symbols or keywords used to perform operations on variables and values. Python supports a variety of operators for different tasks. Here are some of the most commonly used operators:
### Arithmetic Operators
Arithmetic operators are used for mathematical calculations.
- **Addition (`+`)**: Adds two values.
- **Subtraction (`-`)**: Subtracts the right-hand operand from the left-hand operand.
- **Multiplication (`*`)**: Multiplies two values.
- **Division (`/`)**: Divides the left-hand operand by the right-hand operand.
- **Modulus (`%`)**: Returns the remainder when the left-hand operand is divided by the right-hand operand.
- **Exponentiation (`**`)**: Raises the left-hand operand to the power of the right-hand operand.
- **Floor Division (`//`)**: Returns the integer part of the division result, discarding the remainder.
### Comparison Operators
Comparison operators are used to compare two values and return a Boolean result.
- **Equal to (`==`)**: Checks if two values are equal.
- **Not Equal to (`!=`)**: Checks if two values are not equal.
- **Greater than (`>`)**: Checks if the left-hand value is greater than the right-hand value.
- **Less than (`<`)**: Checks if the left-hand value is less than the right-hand value.
- **Greater than or Equal to (`>=`)**: Checks if the left-hand value is greater than or equal to the right-hand value.
- **Less than or Equal to (`<=`)**: Checks if the left-hand value is less than or equal to the right-hand value.
### Logical Operators
Logical operators are used to combine and manipulate Boolean values.
- **And (`and`)**: Returns `True` if both operands are `True`.
- **Or (`or`)**: Returns `True` if at least one operand is `True`.
- **Not (`not`)**: Returns the opposite of the operand's Boolean value.
### Assignment Operators
Assignment operators are used to assign values to variables.
- **Assignment (`=`)**: Assigns the value of the right-hand operand to the left-hand variable.
- **Add and Assign (`+=`)**: Adds the right-hand value to the left-hand variable and assigns the result.
- **Subtract and Assign (`-=`)**: Subtracts the right-hand value from the left-hand variable and assigns the result.
- **Multiply and Assign (`*=`)**: Multiplies the left-hand variable by the right-hand value and assigns the result.
- **Divide and Assign (`/=`)**: Divides the left-hand variable by the right-hand value and assigns the result.
### Membership Operators
Membership operators are used to test if a value is present in a sequence (e.g., a string, list, or tuple).
- **In (`in`)**: Returns `True` if a value is found in the sequence.
- **Not In (`not in`)**: Returns `True` if a value is not found in the sequence.
These operators are essential for performing various operations in Python, and they are used extensively in programming. Understanding how to use them is crucial for effective coding.

## Conditional Expressions
Conditional expressions in Python are used to make decisions and control the flow of a program based on specified conditions. They often involve the use of `if`, `elif` (else if), and `else` statements. Here's an overview of conditional expressions in Python:
### `if` Statement
The `if` statement is used to test a condition. If the condition is true, the code block indented under the `if` statement is executed.
```python
age = 25
if age < 18:
    print("You are a minor.")
```
### `elif` (Else If) Statement
The `elif` statement is used to test additional conditions after the initial `if` statement. It is executed if the preceding `if` or `elif` conditions are false and the current condition is true.
```python
score = 85
if score >= 90:
    print("Excellent!")
elif score >= 70:
    print("Good job.")
```
### `else` Statement
The `else` statement is used to define a block of code that will be executed if the `if` and `elif` conditions are false.
```python
num = 10
if num > 0:
    print("Positive number.")
else:
    print("Non-positive number.")
```
### Nested `if` Statements
You can nest `if` statements within other `if` statements to handle complex conditions.
```python
x = 10
y = 5
if x > 0:
    if y > 0:
        print("Both x and y are positive.")
```
### Ternary Operator
Python also allows the use of a ternary operator for concise conditional expressions:
```python
result = "Pass" if score >= 50 else "Fail"
```
Conditional expressions are crucial for making decisions in your code and executing different actions based on specific conditions. They are used extensively for creating logic and branching in your programs.

## Loops
Loops in Python are used to repeatedly execute a block of code. Python provides two primary loop structures: `for` and `while` loops. Here's an overview of these loops:
### `for` Loop
The `for` loop is used for iterating over a sequence (such as a list, tuple, or string) or other iterable objects. It executes a block of code for each item in the sequence.
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
### `while` Loop
The `while` loop is used to repeatedly execute a block of code as long as a condition is true. It is suitable when you don't know the number of iterations in advance.
```python
count = 0
while count < 5:
    print("Count:", count)
    count += 1
```
### Loop Control Statements
Python also provides loop control statements to modify the execution of loops:
- `break`: Terminates the loop prematurely.
- `continue`: Skips the current iteration and proceeds to the next one.
- `pass`: Used as a placeholder when no action is required in the loop.
### `for` Loop with `range()`
The `range()` function is commonly used with `for` loops to generate a sequence of numbers. It is helpful for iterating a specific number of times.
```python
for i in range(5):
    print(i)
```
### Nested Loops
Python allows nesting loops inside each other. This can be useful for handling multidimensional data or for complex iterative operations.
```python
for x in range(3):
    for y in range(3):
        print(x, y)
```
Loops are essential for automating repetitive tasks and processing data. They provide the means to iterate through sequences and perform actions multiple times, making them a fundamental part of Python programming.

## Functions
Functions in Python are blocks of code that can be named and reused. They allow you to organize your code into smaller, manageable parts. Here's an overview of functions in Python:
### Defining a Function
You can define a function using the `def` keyword followed by the function name and a set of parentheses. The code block to be executed is indented under the function definition.
```python
def greet(name):
    print("Hello, " + name)
```
### Calling a Function
To execute a function, you simply call it by its name and provide any required arguments in the parentheses.
```python
greet("Alice")
```
### Function Parameters
Functions can accept parameters (input values) that allow you to pass data to the function.
```python
def add(x, y):
    return x + y
```
### Return Statement
Functions can use the `return` statement to send a value back as the result of the function's execution.
```python
result = add(5, 3)  # result will be 8
```
### Default Parameters
You can set default values for function parameters, making some arguments optional.
```python
def say_hello(name="Guest"):
    print("Hello, " + name)
```
### DocStrings
Adding docstrings (comments enclosed in triple-quotes) to your functions is good practice. They provide documentation for your function's purpose and usage.
```python
def calculate_area(length, width):
    """
    Calculates the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The calculated area.
    """
    return length * width
```
### Scope
Variables defined inside a function have local scope and are only accessible within that function. Variables defined outside of any function have global scope.
### Lambda Functions
Lambda functions, or anonymous functions, are small, one-line functions defined using the `lambda` keyword.
```python
multiply = lambda x, y: x * y
```
```using
multiplyDemo = multiply(4, 3)
print(multiplyDemo) # 12
```
Functions are fundamental to structuring your code in a modular and reusable way. They make your code more organized, easier to read, and promote code reusability.

## Error Handling

Error handling in Python allows you to deal with unexpected situations and prevent your program from crashing. Python provides mechanisms for handling exceptions and errors gracefully. Here's an overview of error handling in Python:
### `try` and `except`
The `try` and `except` blocks are used to catch and handle exceptions. Code that may raise an exception is placed inside the `try` block, and if an exception occurs, it's handled in the `except` block.
```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the exception
    print("Division by zero is not allowed.")
```
### Multiple `except` Blocks
You can have multiple `except` blocks to handle different types of exceptions. This allows you to provide specific handling for each exception.
```python
try:
    num = int("abc")
except ValueError:
    print("Invalid value provided.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```
### `else` and `finally`
- The `else` block can be used after all `except` blocks. It runs if no exceptions occur in the `try` block.
```python
try:
    num = 10 / 2
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print("No exceptions occurred.")
```
- The `finally` block is used to execute code regardless of whether an exception occurred or not. It's often used for cleanup operations.
```python
try:
    file = open("example.txt", "r")
    # Perform some operations on the file
except FileNotFoundError:
    print("File not found.")
finally:
    file.close()  # Always close the file, whether there's an exception or not.
```
### Raising Exceptions
You can raise exceptions manually using the `raise` statement. This is useful when you want to trigger an error in your code under specific conditions.
```python
if x < 0:
    raise ValueError("x should be a positive number")
```

### Custom Exceptions
You can create custom exceptions by defining new exception classes. This allows you to handle application-specific errors gracefully.
```python
class CustomError(Exception):
    pass

try:
    # Some code that may raise a custom exception
    if something_wrong:
        raise CustomError("Something went wrong.")
except CustomError as e:
    print("Custom error:", e)
```
Error handling is essential for writing robust and reliable programs. It allows you to anticipate and manage issues that might arise during the execution of your code.

## File I/O (Input/Output)
File Input/Output (I/O) in Python allows you to work with files, read data from them, and write data to them. Here's an overview of file I/O in Python:
### Opening a File
You can open a file for reading (`'r'`), writing (`'w'`), or appending (`'a'`). You can also open it in binary mode by adding `'b'` to the mode (e.g., `'rb'`, `'wb'`, `'ab'`). To open a file, use the `open()` function.
```python
# Opening a file for reading
file = open("example.txt", "r")

# Opening a file for writing
file = open("output.txt", "w")
```
### Reading from a File
You can read the contents of a file using methods like `read()`, `readline()`, or by iterating over the file object.
```python
# Read the entire file
content = file.read()
# Read a single line
line = file.readline()
# Iterate over the file line by line
for line in file:
    print(line)
```
### Writing to a File
To write data to a file, open the file in write (`'w'`) or append (`'a'`) mode and use the `write()` method.
```python
# Open the file in write mode
file = open("output.txt", "w")

# Write data to the file
file.write("Hello, World!")
```
### Closing a File
Always close a file using the `close()` method when you're done with it. This releases system resources and ensures data is written to the file.
```python
file.close()
```
### Using `with` Statement
A better practice is to use the `with` statement, which automatically closes the file when the block is exited. It's the recommended way to handle files.
```python
with open("example.txt", "r") as file:
    content = file.read()
# File is automatically closed when exiting the block
```
### Error Handling
File I/O operations can raise exceptions (e.g., `FileNotFoundError`, `PermissionError`). Always include error handling to manage potential issues when working with files.
### File Modes
- `'r'`: Read (default) - Open for reading.
- `'w'`: Write - Open for writing, creates a new file or truncates an existing file.
- `'a'`: Append - Open for writing, creates a new file or appends to an existing file.
- `'b'`: Binary - Open in binary mode for reading or writing.
- `'x'`: Exclusive Creation - Open for exclusive creation, failing if the file already exists.
File I/O is a fundamental concept in programming, enabling you to work with data stored in files, and it's crucial for tasks like reading configuration files, logging, and data persistence.

## Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a programming paradigm that organizes and models data and code into objects. In Python, OOP is a fundamental concept that allows you to create reusable and maintainable code. Here's an overview of OOP in Python:

### Class

- A class is a blueprint or a template for creating objects. It defines the structure and behavior of objects.
- Classes in Python are defined using the `class` keyword.

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is started.")
```

### Object

- An object is an instance of a class, created from the class blueprint.
- Objects can have attributes (variables) and methods (functions).

```python
my_car = Car("Toyota", "Camry")
my_car.start_engine()
```

### Constructor

- The `__init__` method is a special method called a constructor. It initializes the object's attributes when an object is created.

### Inheritance

- Inheritance is a mechanism that allows you to create a new class by inheriting properties and methods from an existing class.
- The new class is called a derived or subclass, and the existing class is the base or superclass.

```python
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.brand} {self.model}.")
```

### Encapsulation

- Encapsulation is the concept of hiding the internal details of an object from the outside world.
- In Python, it's achieved by using private attributes (variables) and methods.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
```

### Polymorphism

- Polymorphism allows objects of different classes to be treated as objects of a common base class.
- It enables flexibility and dynamic behavior in code.
```python
def describe_vehicle(vehicle):
    print(f"This vehicle is a {vehicle.brand} {vehicle.model}.")

car = Car("Nissan", "Altima")
electric_car = ElectricCar("Tesla", "Model S", 75)

describe_vehicle(car)
describe_vehicle(electric_car)
```
OOP promotes code reusability, modularity, and maintainability by modeling data and behaviors as objects and classes. It's a powerful paradigm used in many Python libraries and frameworks.
