# python dictionary 
person ={
    "firstname":"John" ,
    "lastname":"Doe" ,
    "age" : 25 ,
    "colors":["blue" , "green"] ,
    "salary" : 5000
}

# show output 
print(person)

# print age 

print(person["age"])

# print salary 

print(person["salary"])

# update age to 34 
person["age"] = 34

# show output 
print(person)

# delete last name 
del person["lastname"]

# show output 
print(person)