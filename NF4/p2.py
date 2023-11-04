

# 3 python contains chainmap which encapsulate dictionary in one unit

# importing chainmap

from collections import ChainMap

# 'creating some dictionaries  

dic={1:"Subham",2:"Loves  His",3:"Mom"}

dic1={1:"black",2:"green",3:"ass"}

dic2={1:"yellow",2:"orange",3:"pineapple"}


# 3 making it chainmap

c=ChainMap(dic,dic1,dic2)

print("The created chainmap is ")

print(c)


