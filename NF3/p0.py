

from collections import defaultdict

# the default is the subclass of dictionary 

# only exception it never raise error 

# creating a dictionary first 

dic={1:"Subham",2:"Loves  His",3:"Mom"}

print("The newly created dictionary is ")

for key,value in dic.items():

    print(key,value)


# accessing the first element of the dict

print(dic[1])

def ofdict():

    return "Not Present"

d=defaultdict(ofdict)

d['a']=12

d['b']=13

print(d['a'])

print(d['b'])

print(d['c'])

# printing the undefined value and it will  not throw any error 


 
