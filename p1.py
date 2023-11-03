

# first class function

# creating a function 

def ofupper(text):

    return text.upper()

print(ofupper("hello"))

# now changing the name of the func which is called first class function 

yell=ofupper

print(yell("subham"))

# python support first class func

# lets see another exmple


def ofadder(x): # takes single argument 

    def subadder(y):

        return x+y

    return subadder

add1=ofadder(15) # changing the fucn name by using first class function

print(add1(10))

