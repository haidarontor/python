def example(mylist):
    
    mylist.append([10,20,30])
    print "value inside the function", mylist
    return 

#now its calling part
mylist=["ontor","rostom","rifat","delower"]
example(mylist)
print "value outside the function", mylist


def example1(mylist):
    mylist=[1,2,3,4]
    print"value inside the function",mylist
    return

#its a calling part 
mylist=[20,30,40]
example1(mylist)
print "value outside the function ",mylist  