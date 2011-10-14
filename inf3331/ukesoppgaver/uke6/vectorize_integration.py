#!/usr/bin/env python
from math import *

# Wikipedia gives trapezoidal rule as : 
# Integral of f(x) from a to b = (h/2)*(f(a) + f(b)) + \
#                              h*sum(i=1,...n-1) f(a+i*h)
def trapz(f , a ,b ,steps):
	h = (b-a)/float(steps-1.0)
	sum = 0.0
	for i in range(steps):
		sum += f(a+ i*h)
	res = h * (sum - f(a)/2 - f(b)/2)
	return res

def f_1(x):
	return 1+x

def sqr(x):
	return x*x
	
print trapz(f_1 , 0, 2, 200) #outputs 4.01005025126

print trapz(sqr, 0, 3, 10000) #outputs 9.000 
#integral (x^2) = (x^3)/3 -> ((3^3)/3) - ((0^3)/3) = 9 - 0 = 9