#gloabal and local variables

total =100 #Global variable

def sum (arg1,arg2):
    
    #both the parameters and return them
    
    total=arg1+arg2 #total is  local variable
    
    print "inside the function local total:" ,total
    return total

#calling part

sum(200,100)

print "outside the function global variable total:",total