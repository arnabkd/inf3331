#Task 6.3 arnabkd (Arnab Kumar Datta)
import numpy

def initial_condition(x):	
	if(str(type(x)) == '<type \'numpy.ndarray\'>'):
		y = x.copy()
		y[0:] = 3.0
		return y
	else:
		return 3.0


#Runtime code	
p1 =  [0, 1.2, 4, -9.1, 5, 8 ]
a = numpy.array(p1)

print initial_condition(a)
print initial_condition(5.0)

#Runtime output
#arnabkd@bounty ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke6 $ python vectorize_function.py 
#[ 3.  3.  3.  3.  3.  3.]
#3.0

