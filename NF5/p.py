
import collections 


# creating a dictionary 

dic1={'a':1,'b':2,'c':3}

dic2={'d':11,'e':12,'f':13}

dic3={'g':14,'h':15,'i':16}


# making them the chainmap

cd=collections.ChainMap(dic1,dic2)

print("The newly made chainmp is")

print(cd.maps)

#making the new child of chainmap as dic3

cd1=cd.new_child(dic3)

print("After entering new child the chainmap is ")

print(cd1.maps)

print("The value associated with b is ")

print(cd1['b'])

print("After reversing the chainmap becomes ")

cd1.maps=reversed(cd1.maps)

print(cd1.maps)