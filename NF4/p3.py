

import collections

# creating a dictionary 

d={'a':1 ,'b':2}

d1={'c':11 ,'c':12}

# making it the chainmap

cd=collections.ChainMap(d,d1)

print("All the chainmap contains are ")

print(cd.maps)

print("All the chainmap contains in list form are ")

print(list(cd.maps))

print("All the chainmap values are ")

print(list(cd.values()))

print("All the chainmap keys are ")

print(list(cd.keys()))
 



