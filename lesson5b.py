# function with parameters 
# example 1 
def greeting (name) :
    print("Good Morning", name)

# call the fuction 
greeting ("Smith")

# example 2 
def adddition (num1, num2) :
    answer =num1+num2
    print ("The sum is", answer)

# call the fuction 
adddition (60,40)

# NB: A funtion is a re-usable block of code that performs a specific task 
# 1. 
adddition (900, 700)

# 2. 
adddition (1500,400)

# 3. 
adddition (-160, -40)


# Assignment 
# 1. subtraction 
def subtraction (num1, num2) :
    answer = num1 - num2
    print("The subtract", answer)

# call the fuction 
subtraction (70, 40)

# 2. Division 
def division (num1, num2) :
    answer = num1 / num2 
    print("The division is", answer)

# call the fuction 
division  (121, 11)

# 3. Multiplication 
def multiplication (num1, num2) :
    answer =num1 * num2 
    print("The answer is", answer)

# call the fuction 
multiplication (45, 10)


# 4. simple interst 
def function (p, r, v) :
    answer =(p*r*v)/100
    print("The simple interest is", answer)

# call the fuction 
function (24000,16,3)

# 5. Area of Triangle 
def area (num0, num1, num2) :
    answer = num0*num1*num2
    print ("The area is", answer)

# call the fuction 
area (1/2, 4, 8)

# 6. BMI 
def BMI (num1, num2) :
    answer =num1 / (num2**2)
    print ("The BMI is", answer)

# call the function 
BMI (80, 5)