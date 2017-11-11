#print "hello world"

#assert 2+2==4
#
#print "hello Bangladesh"

#assert 1+1==3
#print "Hello TalhaTraining"

def kelvinToFahrenheit(temperature):
    assert(temperature>=0),"colder than absolute zero!"
    
    return((temperature-273)*1.8)+32

#print kelvinToFahrenheit(273)
#print int (kelvinToFahrenheit(505.86))
print kelvinToFahrenheit(-5)