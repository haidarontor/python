#variable length argument


#def functionname ([formal_argu],*var_args_tuple):
 #   "function docs string"
    
  #  function suite
    
   # return [expresstion]

#calling 

def example(arg1,*vartuple):
    
    print "output is :"
    print arg1
    for var in vartuple:
      print "vartuple value:",var
   
    return

example(100)
example(50,60,70)