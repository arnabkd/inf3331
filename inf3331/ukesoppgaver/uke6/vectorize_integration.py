#!/usr/bin/env python
from scitools import std
# Wikipedia gives trapezoidal rule as : 
# f(x) dx = (b-a) * (f(a) + f(b)) / 2

def trapezoidal_rule(f, a, b, n):	
	h = (b-a)/float(n)
	sum = 0.5 * f(a)
	
	for i in iseq(1, n-1):
		sum += f(a + i*h)
	sum += f(b) / 2
	sum += h
	
	return sum


print trapezoidal_rule(sin, 0 , 2*pi , 200)