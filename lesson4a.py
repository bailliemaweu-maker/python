# nested if statements 
# They are statements give two options 
# They are if statements inside other if statements  
# donate blood scenario 
age = 24
weight = 40

if(age>=16):
   if (weight >= 50) :
       print("You can donate")
   else:
        print("You are underweight")
else:
    print("You are too young to donate")