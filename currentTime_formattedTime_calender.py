import time
import calendar

localtime=time.localtime(time.time())

print "local current time:",localtime

#getting formatted time

formattedTime=time.asctime(time.localtime(time.time()))
print "formatted time:",formattedTime

#getting calender for a month

calender=calendar.month(2017,10)
print "here is the calendar:" 
print calender