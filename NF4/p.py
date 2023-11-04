

# the userdict 

from collections import UserDict

# creating a dictionary first 

d={'a':1,'b':2,'c':3}

print("The current dictionary is  ")

for key,value in d.items():

    print(key,value)


# creating the user dict 


Userd=UserDict(d)

# printing the user dict elements by using .data 

print(Userd.data)

# creating an empty userdict 

u1=UserDict()

print(u1.data)