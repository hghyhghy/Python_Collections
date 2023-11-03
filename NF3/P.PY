

from collections import OrderedDict

#creating an oder dict 

myod=OrderedDict([('a',1),('b',2),('c',3)])

print("The newly made order dict is ")

print(myod)

# adding a new item to the orderdict

myod['d']=4

print("After adding new items the order dict becomes ")

for key,value in myod.items():

    print(key,value)


# adding the value by using update 

myod.update([('e',5),('f',6)])


print("After adding new items the order dict becomes ")

for key,value in myod.items():

    print(key,value)


myod.move_to_end('e',last=False)

print("After making  the element e to the first position")


for key,value in myod.items():

    print(key,value)