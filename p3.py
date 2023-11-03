

# orderdict  is the subclass of the dictionnary which remenbers the order of insertionn of 

# elements 

# importing orderdict

from collections import OrderedDict

print("The original dictionary is ")


d={}

d['a']=0

d['b']=1

d['c']=2

d['d']=3

d['e']=4

d['f']=6

for key,values in d.items():

    print(key,values)


print("Now the orderdict is ")

od=OrderedDict()

  
od['a']=0

od['b']=1

od['c']=2

od['d']=3

od['e']=4

od['f']=6

for key,values in od.items():

    print(key,values)



