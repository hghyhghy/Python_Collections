

from collections import Counter

# creating a list

a=[12,1,2,3,5,4,7,6,8]

# using the counter 

x=Counter(a)

print(x)

# printing the eys of the from the list 


for i in x.keys():
   
    print(i, end=" ")



# making the keys in the list 

x_keys=list(x.keys())

# making the values from the list 

x_values=list(x.values())

print(x_keys)

print(x_values)


