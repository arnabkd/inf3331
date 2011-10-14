import numpy

def initial_condition(x):	
	print str(type(x))
	print str(type(x)) == 'type<\'numpy.ndarray\'>'
	if(type(x) == '<type \'numpy.ndarray\'>'):
		print "yay"
		y = x.copy()
		print y
		y[0:] = 3.0
		print y
		return y
	else:
		return 3.0
	
p1 =  [0, 1.2, 4, -9.1, 5, 8 ]
a = numpy.array(p1)

initial_condition(a)