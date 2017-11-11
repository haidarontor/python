x=50
y=51

if( x is y):
    print "have some identity"
else:
    print "do not some identity"
    
if (id(x) == id(y)):   
    print "have some identity"
else:
    print "do not have some identity" 
    
x=100
y=100    
if( x is not y):
    print "do  not have some identity"
    
else:
    print"have some identity"        