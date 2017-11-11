#str.capitalize()
from __builtin__ import str

str="we love our country"

print "caplitalize function:", str.capitalize()

# center function
#str.center(width ,fillchar)

name="we love python"

print "center function:", str.center(50,)
#count function
#str.count(sub,start=0,end=len(string))

str ="we want to learn python"

sub='e'

print "count function:", str.count(sub,4,30)
sub ="to"
print "count function :",str.count(sub,0,20)

#decode function
#str.decode(encoding ="UTF-8,errors='strict')

str="rifat, ontor are very good friend"

str=str.encode('base64','strict')
print "endcoded string:" +str
print "decoded string :" +str.decode('base64','strict')
#enocde function

str="i buy a laptop"

print "encoded:" + str.encode('base64','strict')