#return statement

def sum(arg1,arg2):
    
    #both argument and return them
    total=arg1+arg2
    print "inside the function :",total
    
    return total
    
#now its part calling 
  
total=sum(50,100)
print "outside the function:",total