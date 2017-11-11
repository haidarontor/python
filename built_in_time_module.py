#altzone funciton 
#time.altzone

import time

print "time.altzone function: %d" % time.altzone

#asctime function
#time.asctime(t)

t=time.localtime()

print "time.asctime(t):%s" % time.asctime(t)

#gmtime function 
#time.gmtime(sec)

print "time.gmtime():%s" %time.gmtime()

#sleep function
#time.sleep(t)

print "star :%s" % time.ctime()
time.sleep(2)
print "end :$s" % time.ctime()