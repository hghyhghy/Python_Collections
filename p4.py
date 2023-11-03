

# updating the value of orderdict 


from collections import OrderedDict


print("The orderdict is ")

od=OrderedDict()

  
od['a']=0

od['b']=1

od['c']=2

od['d']=3

od['e']=4

od['f']=6


for key,value in od.items():

    print(key,value)


print("After changing the orderdict it becomes ")

od['c']=99

for key,value in od.items():

    print(key,value)
