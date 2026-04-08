# Variable : A variable is a name used to store a value in memory.

name = "Prasanth"
age = 25

# Dynamic Typing (Important) : Python automatically decides the type.

x = 10      # integer
x = "hello" # now string

# Variable Naming Rules

# 1. Must start with a letter or underscore

name = "prasanth"
_user = "kumar"

# Invalid Names: 

# 1name = "wrong"      # cannot start with number
user-name = "wrong"  # hyphen not allowed
# class = "wrong"      # keyword not allowed

# Reserved Keywords (Cannot Use) - if, else, while, for, class, def, return, True, False

# Example : class = "abc"  # error

user_name = "Prasanth"
total_amount = 500
is_active = True

# 7. Multiple Variable Assignment

# Assign multiple values: a, b, c = 1, 2, 3

# Same value: x = y = z = 100

# 8. Changing Variable Values 

x = 10
x = 20

# Using Variables

a = 10
b = 5
c = a + b

print(c)  # 15

bill_amount = 1000
tip_percent = 10

tip = bill_amount * tip_percent / 100
total = bill_amount + tip

print(total)

name = "YourName"
age = 25
city = "YourCity"

p = 1000
t = 2
r = 5

si = (p * t * r) / 100
print(si)

a = 10
b = 20

a, b = b, a
print(a, b)