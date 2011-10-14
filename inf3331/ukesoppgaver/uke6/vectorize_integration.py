#!/usr/bin/env python

# Wikipedia gives trapezoidal rule as : 
# f(x) dx = (b-a) * (f(a) + f(b)) / 2

def integrate (function, a, b, desiredSteps):	
	a = float(a)
	b = float(b)
	
	h = (b-a) / desiredSteps
	sum = 0
	for i in xrange(a,b):
		sum += function(i) * h
	print sum
	return sum


print integrate(lambda x: x+1, 0 , 10 , 10000)