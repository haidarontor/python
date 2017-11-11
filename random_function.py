import random

#choice(x)

print "choice function:", random.choice([10,20,30,40])

print "choice function string:",random.choice('TalhaTraining')

#randrange function

print "randrange function:",random.randrange(10,100,2)

#random function 

print "random function:",random.random()

#suffle function
list=["dhaka","comilla","Rajshahi"]
random.shuffle(list)
print "shuffle funciton:",list