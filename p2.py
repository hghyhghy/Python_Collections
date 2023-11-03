

# clousers in python 

# creating a function 

def outertext(text): # taking one argument 

    def innertext():  # those are called clousers which remembers values

        print(text)

    innertext

if __name__=='__main--':

     outertext("Hey")


# now by using first class func

def offirst(text):

    def ofsecond():

        print(text)
    
    return ofsecond


if __name__=='__main--':

    myfunc=offirst("subham")

    myfunc()
 

# another example 

def facto(num):

    if num==1:

        return 1
    else:

        return num*facto(num-1)
    
print(facto(5))



