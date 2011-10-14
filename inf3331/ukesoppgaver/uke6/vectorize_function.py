import numpy

def initial_condition(x):	
	if(x.__class__.__name__ == 'numpy'):
		y = x.copy()
		y[0:] = 3.0
		return y
	else:
		return 3.0
	
p1 =  [0, 1.2, 4, -9.1, 5, 8 ]
a = numpy.array(p1)
print initial_condition(a)