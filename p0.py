# packing and unpacking arguments 

# creating a function first 

def ofpack(a,b,c,d):

    print(a,b,c,d)

# created a function which takes four arguments 

# creating a list 

my_list=[6,4,3,2,0]

print(*my_list)  

# by using * we unpack all list elements to that func


def ofsum(a,b,c):

    return (a+b+c)

args=[4,5,6]

print(*args)

print(ofsum(3,5,4))
