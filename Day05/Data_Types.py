# Types of Data in Python

# 1. Numeric Types : int, float, complex

x = 10   
y = -5

pi = 3.14
price = 99.99

c = 2 + 3j

# 2. Sequence Types : string, List, Tuple 

name = "Prasanth"
msg = 'Hello'

# String Operations : 

a = "Hello"
b = "World"

print(a + b)   # HelloWorld
print(a * 2)   # HelloHello

# Indexing

text = "Python"
print(text[0])   # P
print(text[-1])  # n

# Slicing

text = "Python"
print(text[0:3])  # Pyt 

# Useful Methods : 

text.lower()
text.upper()
text.strip()
text.replace("P", "J")

# List : Ordered, mutable, allows duplicates

nums = [1, 2, 3, 4]
names = ["A", "B", "C"]
nums.append(5)
nums.remove(2)
nums[0] = 10

# Tuple : Ordered, immutable

t = (1, 2, 3)

# 3. Set Types : set --> Unordered, Duplicates are not allowed, no indexing

s = {1, 2, 3, 3}
print(s)  # {1,2,3}
s.add(4)
s.remove(2)

# 4. Mapping Type : dictionary --> Key-value pair, Mutable 

student = {
    "name": "Prasanth",
    "age": 25
}
print(student["name"])
student["age"] = 26
student["city"] = "Vizag"

# 5. Boolean Type : bool --> True === 1 && False === 0

is_active = True
is_logged_in = False
if is_active:
    print("Active")

# 6. None Type : None --> Represents “no value”

x = None

# Type Conversion (Casting) --> Changing DataType 

x = "10"
y = int(x)

print(y + 5)  # 15

# Type Checking : Checks the data type

print(type(x))

student = {
    "name": "Prasanth",
    "marks": [90, 85, 88],
    "is_passed": True
}

print(student["marks"][0])  # 90

# Create variables for name, age, and city. Print the type of each variable.

name = "prasanth"
age = 25
city = "visakhapatnam"

print(type(name))
print(type(age))
print(type(city))

# Assign a float value and convert it to int.

num1 = 10.25
print(int(num1))

# Assign an int and convert it to string.

num2 = 2000
print(str(num2))
print(type(str(num2)))

# Check type of "123" and 123.

num3 = "123"
num4 = 123
print(type(num3))
print(type(num4))

# Create a string and print its length.

str1 = "Welcome to python tutorial"
print(len(str1))

# Access first and last character.

str2 = "Welcome to python tutorial"
print(str2[0])
print(str2[-1])

# Reverse a string.

str3 = "Welcome to python tutorial"

rev = ""
for char in str3 : 
    rev = char + rev
print(rev)

print(str3[::-1])

print("".join(reversed(str3)))


# Convert string to uppercase.

str4 = "learning python"
print(str4.upper())
print(str4.split())

# Replace a word in string.

str5 = "python learning"
print(str5.replace("learning", "course"))

text = "hello"
print(text.upper())

text = "HELLO"
print(text.lower())

text = "Welcome to Python"
print(text.split())

words = ['Welcome', 'to', 'Python']
print(" ".join(words))


text = "Python"
print(text.find("t"))

text = "Hello World"
print(text.replace("World", "Python"))

# .strip() – Remove spaces
text = "  hello  "
print(text.strip()) 

# .capitalize() – First letter uppercase

text = "python"
print(text.capitalize())

# .title() – Capitalize each word

text = "welcome to python"
print(text.title())

# .isdigit() – Check if number

text = "1234"
print(text.isdigit())

# Check if a substring exists.

text = "Welcome to Python"
print("Python" in text)

text = "Welcome to Python"
print(text.find("Python"))

text = "Welcome to Python"
print(text.index("Python"))

# Case-insensitive check

text = "Welcome to Python"
print("python".lower() in text.lower())

# Count occurrences of a character.

text = "Welcome to Python"
print(text.count("o"))

text = "welcome to python"
count = 0

for char in text:
    if char == 'o':
        count += 1

print(count)

# Count any character (user input)

text = "welcome to python"
ch = input("Enter character: ")
print(text.count(ch))

# Count all characters

from collections import Counter

text = "welcome"
print(Counter(text))


# Remove spaces from start and end.

text = "  hello  "
print(text.strip()) 

# Split a sentence into words.

sentence = "Welcome to Python programming"
words = sentence.split()

print(words)

# Join words into a sentence.

words = ['Welcome', 'to', 'Python', 'programming']

sentence = (" ".join(words))
print(sentence)

# Add two numbers.

num6 = 10
num7 = 20
num8 = num6 + num7
print(num8)

# Find square of a number.

number = int(input("Enter a Number: "))
square = number*number
print(square)

# Find cube of a number.

number = int(input("Enter a Number: "))
cube = number*number*number
cube1 = number ** 3
print(cube)
print(cube1)

# Check if number is even or odd.

number = int(input("Enter a Number: "))

if number % 2 == 0:
    print(True)
else:
    print(False)

# Find largest of two numbers.

number1 = int(input("Enter a Number: "))
number2 = int(input("Enter a Number: "))

print(max(number1, number2))

# Compare two numbers.

number1 = int(input("Enter a Number: "))
number2 = int(input("Enter a Number: "))

print(bool(number1 == number2))

# Check if a number is positive.

number1 = int(input("Enter a Number: "))

if number1 >= 0:
    print(True)
else: 
    print(False)

# Check if string is empty.

str1 = str(input("Enter a value: "))
if str1 == "":
    print(False)
else : 
    print(True)

# Use and, or operators.

str1 =  input("Enter a value: ")
if len(str1) > 3 and "a" in str1:
    print("Condition True")
else:
    print("Condition False")

# Negate a boolean value.

value = True
print(not value)

# Create a list of 5 numbers.

numbers = [1,2,3,4,5,6]
print(numbers)

# Add an element to list.

numbers = [1,2,3,4,5,6]
numbers.append(7)
print(numbers)

# Remove an element.

numbers = [1,2,3,4,5,6]
numbers.remove(3)
print(numbers)

# Find length of list.

numbers = [1,2,3,4,5,6]
print(len(numbers))

# Access last element.

numbers = [1,2,3,4,5,6]
print(numbers[-1])

# Reverse a list.

numbers = [1,2,3,4,5,6]
print(list(reversed(numbers)))

# Sort a list.

numbers = [1,2,5,6,3,4]

print(list(sorted(numbers)))

# Find max and min.

numbers = [1,2,5,6,3,4]
print(max(numbers))
print(min(numbers))

# Count occurrences of element.

numbers = [1,2,3,6,5,3,2,9,8,3,7]
print(numbers.count(3))

from collections import Counter

numbers = [1,2,3,6,5,3,2,9,8,3,7]
print(Counter(numbers))

# Check if element exists.

numbers = [1,2,5,6,3,4]
print(3 in numbers)

numbers = [1,2,5,6,3,4]

num = int(input("Enter number: "))

if num in numbers:
    print("Element exists")
else:
    print("Element does not exist")

# Merge two lists.

list1 = [10,20,30,40,50]
list2 = [60,70,80,90,100]

print(list1+list2)

# Copy a list.

list1 = [10,20,30,40,50]
new_list = numbers[:]
new_list = list1.copy()
print(new_list)

# Deep copy (for nested lists)

import copy
numbers = [[1, 2], [3, 4]]
new_list = copy.deepcopy(numbers)
print(new_list)

# Clear a list.

list1 = [10,20,30,40,50]
list1.clear()
print(list1)

# Insert element at index.

list1 = [10,20,30,40,50]

list1.insert(2, 25)   # insert 25 at index 2

print(list1)




