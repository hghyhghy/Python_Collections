from collections import Counter

a=Counter("subhamsarkar")

# using the for loop 

for i in a.elements():

    print(i, end=" ")

# creating  a  dictionary 


d=Counter({'name':67,'roll':2,'id':101})

print("The main elements are ")


for x in d.elements():

    print(x, end=" ")

print()

# creating a list 

l=Counter([12,2,3,3,4,4,78])


for y in l.elements():

    print(y, end=" ")





