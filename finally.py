try:
    print 'hello '
    print 1/0
except ZeroDivisionError:
    print"Divided by zero!!"
finally:
    print "this code will run no matter what"    