"""
Comprehensive Python Basics Practice
Covers: variables, operations, strings, control flow, functions, data structures, file I/O, and classes
"""

# ============================================================================
# 1. HELLO WORLD
# ============================================================================
print("Hello, World!")
print()


# ============================================================================
# 2. VARIABLES AND BASIC OPERATIONS
# ============================================================================
print("--- Variables and Operations ---")

# Variables and data types
name = "Python"
age = 30
height = 5.9
is_fun = True

print(f"Name: {name}, Age: {age}, Height: {height}, Fun: {is_fun}")

# Arithmetic operations
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor Division: {a // b}")
print(f"Modulo: {a % b}")
print(f"Exponent: {a ** b}")
print()


# ============================================================================
# 3. STRING MANIPULATION
# ============================================================================
print("--- String Manipulation ---")

text = "Python Programming"
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Length: {len(text)}")
print(f"First 6 chars: {text[:6]}")
print(f"Replace 'Python' with 'Java': {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# String concatenation
greeting = "Hello" + " " + "World"
print(f"Concatenation: {greeting}")
print()


# ============================================================================
# 4. CONTROL FLOW - IF/ELSE
# ============================================================================
print("--- If/Else Statements ---")

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
print()


# ============================================================================
# 5. LOOPS - FOR AND WHILE
# ============================================================================
print("--- Loops ---")

# For loop
print("For loop (1-5):")
for i in range(1, 6):
    print(f"  {i}")

# For loop with list
print("For loop with list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# While loop
print("While loop (countdown 5-1):")
count = 5
while count > 0:
    print(f"  {count}")
    count -= 1
print()


# ============================================================================
# 6. FUNCTIONS
# ============================================================================
print("--- Functions ---")

def greet(name):
    """Function that greets a person"""
    return f"Hello, {name}!"

def add(x, y):
    """Function that adds two numbers"""
    return x + y

def multiply(x, y=2):
    """Function with default parameter"""
    return x * y

print(greet("Alice"))
print(f"Add 10 + 5: {add(10, 5)}")
print(f"Multiply 10 * default: {multiply(10)}")
print(f"Multiply 10 * 3: {multiply(10, 3)}")
print()


# ============================================================================
# 7. DATA STRUCTURES - LISTS
# ============================================================================
print("--- Lists ---")

numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")
numbers.append(6)
print(f"After append(6): {numbers}")
numbers.extend([7, 8])
print(f"After extend([7, 8]): {numbers}")
print(f"Length: {len(numbers)}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")
print(f"Slice [1:4]: {numbers[1:4]}")
numbers.pop()
print(f"After pop(): {numbers}")
print()


# ============================================================================
# 8. DATA STRUCTURES - DICTIONARIES
# ============================================================================
print("--- Dictionaries ---")

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}
print(f"Dictionary: {person}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
person["age"] = 31
print(f"After updating age: {person}")
person["email"] = "john@example.com"
print(f"After adding email: {person}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print()


# ============================================================================
# 9. DATA STRUCTURES - TUPLES AND SETS
# ============================================================================
print("--- Tuples and Sets ---")

# Tuples (immutable)
coordinates = (10, 20, 30)
print(f"Tuple: {coordinates}")
print(f"First element: {coordinates[0]}")

# Sets (unique elements)
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print(f"Set (duplicates removed): {unique_numbers}")
unique_numbers.add(6)
print(f"After add(6): {unique_numbers}")
print()


# ============================================================================
# 10. LIST COMPREHENSION
# ============================================================================
print("--- List Comprehension ---")

squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {even_numbers}")
print()


# ============================================================================
# 11. FILE OPERATIONS
# ============================================================================
print("--- File Operations ---")

# Write to file
filename = "sample.txt"
with open(filename, "w") as file:
    file.write("Line 1: Hello\n")
    file.write("Line 2: Python\n")
    file.write("Line 3: Practice\n")
print(f"Written to {filename}")

# Read from file
with open(filename, "r") as file:
    content = file.read()
print(f"Read from {filename}:")
print(content)

# Append to file
with open(filename, "a") as file:
    file.write("Line 4: Appended\n")
print(f"Appended to {filename}")

# Read line by line
print("Reading line by line:")
with open(filename, "r") as file:
    for line in file:
        print(f"  {line.strip()}")
print()


# ============================================================================
# 12. EXCEPTION HANDLING
# ============================================================================
print("--- Exception Handling ---")

try:
    result = 10 / 2
    print(f"10 / 2 = {result}")
    result = 10 / 0  # This will raise an error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This runs regardless of success or error")
print()


# ============================================================================
# 13. CLASSES AND OBJECT-ORIENTED PROGRAMMING
# ============================================================================
print("--- Classes and OOP ---")

class Animal:
    """Base class for animals"""
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    """Dog class inheriting from Animal"""
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed
    
    def bark(self):
        return f"{self.name} barks: Woof! Woof!"

# Create instances
dog = Dog("Rex", "Golden Retriever")
print(dog.describe())
print(dog.bark())
print(f"Breed: {dog.breed}")
print()


# ============================================================================
# 14. LAMBDA AND MAP/FILTER
# ============================================================================
print("--- Lambda, Map, and Filter ---")

numbers = [1, 2, 3, 4, 5]

# Lambda function
square = lambda x: x ** 2
print(f"Square of 3: {square(3)}")

# Map
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
print()


# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 70)
print("Python Basics Practice Complete!")
print("Topics covered:")
print("  1. Hello World")
print("  2. Variables and Operations")
print("  3. String Manipulation")
print("  4. Control Flow (If/Else)")
print("  5. Loops (For and While)")
print("  6. Functions")
print("  7. Lists")
print("  8. Dictionaries")
print("  9. Tuples and Sets")
print(" 10. List Comprehension")
print(" 11. File Operations")
print(" 12. Exception Handling")
print(" 13. Classes and OOP")
print(" 14. Lambda, Map, and Filter")
print("=" * 70)