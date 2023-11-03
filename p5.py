# popping the element from the orderdict 


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


print("After popping element from the list it becomes ")

od.pop('c')

for key,value in od.items():

    print(key,value)


# now updating the orderdict and it will save it at the last 

od['c']=100

for key,value in od.items():

    print(key,value)
