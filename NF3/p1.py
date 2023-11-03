


from collections import defaultdict

# the use of --missing--() func

dic={1:"Subham",2:"Loves  His",3:"Mom"}

print("The newly created dictionary is ")

for key,value in dic.items():

    print(key,value)


# creating the deafault dict

def ofdic():

    return "Not found"

d=defaultdict(ofdic)

d['a']=12

d['b']=13

print("the Defaultdict is ")


for key,value in d.items():

    print(key,value)

# using --missing-- func

print(d.__missing__('a'))

print(d.__missing__('b'))


# 3 it will return default value