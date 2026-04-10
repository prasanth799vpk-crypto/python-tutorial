# Function name should not be same as the varaiable name, file name and package (or) module name.


def summation() :
    n1 = eval(input("Enter the n1 value :"))
    n2 = eval(input("Enter the n2 value :"))
    add = n1+n2
    print(n1)

summation()

# Take three values and find the average

def Average() :
    val1 = eval(input("Enter the val1 value :"))
    val2 = eval(input("Enter the val2 value :"))
    val3 = eval(input("Enter the val3 value :"))
    sum_of_avg = (val1+val2+val3)/3
    print(sum_of_avg)

Average()

# Function without arguements :

def Average() :   
    try :
        val1 = eval(input("Enter the val1 value :"))   
        val2 = eval(input("Enter the val2 value :"))
        val3 = eval(input("Enter the val3 value :"))
        sum_of_avg = (val1+val2+val3)/3
        print(sum_of_avg)
    except  Exception as e : print(e)
Average()

# Function with arguements :

def Average(val1,val2,val3) :   
    try :
        # val1 = eval(input("Enter the val1 value :"))   
        # val2 = eval(input("Enter the val2 value :"))
        # val3 = eval(input("Enter the val3 value :"))
        sum_of_avg = (val1+val2+val3)/3
        print(sum_of_avg)
    except  Exception as e : print(e)
Average(10,30,60)

def Tax_Calculation (salary, tax_percentage) :
    tax_amount = salary * tax_percentage/100
    print('tax_amount' , tax_amount)

Tax_Calculation(50000,10)

def Tax_Calculation (salary, tax_percentage=10) :   # tax_percentage=10 --> default arguement
    tax_amount = salary * tax_percentage/100 
    print('tax_amount' , tax_amount)

Tax_Calculation(50000,20)  # tax_percentage is overrides 


def Tax_Calculation (salary, tax_percentage=10) :   # tax_percentage=10 --> default arguement
    tax_percentage = 30  # tax_percentage is overrides 
    tax_amount = salary * tax_percentage/100 
    print('tax_amount' , tax_amount)

Tax_Calculation(50000) 

# Note : Default arguements are passed as last arguemnet because it will consider that otherwise it throughs an error 

# Addition(n1,n2,n3=100)  # works
# Addition(n1,n2=100,n3) # Fails
# Addition(n1=100,n2,n3) # Fails
# Addition(n1,n2=100,n3=100) # works
# Addition(n1=100,n2=100,n3) # Fails
# Addition(n1=100,n2,n3=100) # Fails
# Addition(n1=100,n2=100,n3=100) # works

# Global Variables vs Local Variables

# Global Variables are the variables which are outside the function

    # It can be used inside the function and outside of the function as well

n1 = 100
n2 = 100
n3 = 300

def Addition1() : 
    sum = n1+n2+n3
    print(sum)

Addition1()

# Local Variables are the variables which are inside the function

    # It can be used inside the function and it cannot be used as outside of the function 

def Addition2() : 
    n1 = 100
    n2 = 100
    n3 = 300
    sum = n1+n2+n3
    print(sum)
    
Addition2()

# Global + Local varibles access

n3 = 500
def Addition3() :
    n1 = 500
    n2 = 200
    sum = n1+n2+n3
    print(sum)
Addition3()

n4 = 500
def Addition3(n4,n5,n6) :
    sum = n4+n5+n6
    print(sum)
Addition3(600,300,400)

n3 = 300
def Addition4(n1,n2,n3=200):
    n3 = 500
    print("n1:", n1)
    print("n2:", n2)
    print("n3:", n3)
    summ = (n1+n2+n3)
    print(f"the sum of {n1}, {n2} and {n3} is {summ}")

Addition4(100,200,600)

# step1 : n3 = 300
# step2 : define the function n3 = 200
# step3 : call the function n3 = 600
# step : run the function n3 = 500 (inside the function lines)

n3 = 300
def Addition4(n1,n2,n3=200):
    n3 = 500 # <-- this value is taken
    print("n1:", n1)
    print("n2:", n2)
    print("n3:", n3)
    summ = (n1+n2+n3)  # 800 --> 100+200+500
    n3=800 # no use 
    print(f"the sum of {n1}, {n2} and {n3} is {summ}") # but n3 is consider as 800 in the {n3} and not value in the sum --> n3 == 500
n3 = 700
Addition4(100,200,600)

# 300 === 200 === 600 ==- 700 === 500 === (sum) === 800(no use)

num1 = 100
num2 = 200
num3 = 600

def Addition2():
    summ = num1+num2+num3
    print("the sum of addition is :", summ)
Addition2()

num1 = 100
num2 = 200
num3 = 600

def Addition2():
    global sum
    summ = num1+num2+num3
    print("the sum of addition is :", summ)
Addition2()

num1 = 100
num2 = 200
num3 = 600
summ = 0
def Addition2():
    global sum # <-- this is a global variable here
    summ = num1+num2+num3
    print("the sum of addition is :", summ)
    summ = summ*500  #4500
    
Addition2() 

num1 = 100
num2 = 200
num3 = 600
summ = 0 # <-- this is a global variable here
def Addition2():
    # global sum
    summ = num1+num2+num3
    print("the sum of addition is :", summ)
    summ = summ*500  #0
    
Addition2() 


# function with if, else statements and function arguements and default parameters 

def even_odd1():
    number = eval(input("Enter the number :"))
    if number%2 == 0 : 
        print(f'{number} is even number')
    else : 
        print(f'{number} is odd number')

even_odd1()

def even_odd1(number):
    # number = eval(input("Enter the number :"))
    if number%2 == 0 : 
        print(f'{number} is even number')
    else : 
        print(f'{number} is odd number')
        
even_odd1(25)


def even_odd1(number=7):
    # number = eval(input("Enter the number :"))
    if number%2 == 0 : 
        print(f'{number} is even number')
    else : 
        print(f'{number} is odd number')
        
even_odd1(20)

summ = 0
def add(a) :
    summ = a
    print(summ)
add(100)


summ = 0
def add(a) : 
    global summ, sub
    summ = a
    sub = summ-50
    print(summ, sub)
add(100)


summ = 0
def add(a):
    global summ
    summ = a

add(100)
print(summ)

print(vishal)  # error : vishal is not defined
vishal = "vizag"

def greet():
    print(vishal)
    vishal="vizag" #error : UnboundLocalError


vishal = "mumbai"
def greet() : 
    print(vishal)
    vishal = "pune"
greet()


vishal = "mumbai"
def greet() : 
    print(vishal)
greet()


v = 10
def kaushik():
    v= 100
    print(v)
kaushik()

v = 10
def kaushik():
    print(v)
kaushik()























