
try:
    a=1000
    b=int (input("Enter a number:"))
    print a/b
except ZeroDivisionError:
    print "your entered 0 which is not permitted!" 
    
    
try:
    variable=10
    print(variable+"hello")
    print (variable/2)
except ZeroDivisionError:
    print"Divided by zero"
except:
    print"type or value error occurred"        
