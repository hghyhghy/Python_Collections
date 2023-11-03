from collections import defaultdict

# applied using for loop 

d=defaultdict(list)  # creating default dict of list 

for i in range(5):
    
    d[i].append(i)

print("The dictionary with values as list is ")

print(d)