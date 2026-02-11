# python modules 
# A module is a python file that contains code 
# its re-usable and can be used in other files 
#  example 1 
# add two numbers 

#  method 1 
import lesson6a

# addition 
lesson6a.addition(45, 55)

# subtraction 
lesson6a.subtraction(32,12)

# division 
lesson6a.division(24,6)

# multiplication 
lesson6a.multiplication(32,4)



# method 2
from lesson6a import addition, subtraction, multiplication, division
addition(40, 90)
subtraction(600,150)
multiplication(5,60)
division(45,9)