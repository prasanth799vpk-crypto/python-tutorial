# Conditional Statements : IF, IF-ELSE, IF-ELIF-ELSE 

if 100>10 : 
    print("Hello")
    print("hey")
    print("wrong")

# when condition is True

print(1)
print(2)
if 100 > 10 :
    print("hello")
    print("haii")
print("hey")

# When Condition is False 

print(1)
print(2)
if 100 < 10 :
    print("hello")
    print("haii")
print("hey")  

# if statement

num = 10

if num > 5:
    print("Number is greater than 5")
    
# if-else statement

num = 3

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
# if-elif-else statement

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    
# Example

num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Nested if statement
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
        
# Nested if-else

num = 7

if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Not positive")
    
# Nested if-elif-else

marks = 85

if marks >= 50:
    if marks >= 90:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Fail")

# example: 

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")