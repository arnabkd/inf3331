#Task 6.4 arnabkd (Arnab Kumar Datta)
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

#Runtime code
print "trapz(f_1,0,2,200)",trapz(f_1 , 0, 2, 200) #outputs 4.01005025126
#integral (1+x) = (1/2)*x(x+2) -> 1/2*2(2+2) - 1/2*0(0+2) = 1(4) - 0 = 4 

print "trapz(sqr, 0, 3, 10000)",trapz(sqr, 0, 3, 10000) #outputs 9.000 
#integral (x^2) = (x^3)/3 -> ((3^3)/3) - ((0^3)/3) = 9 - 0 = 9

#Runtime output
#arnabkd@bounty ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke6 $ python vectorize_integration.py 
#trapz(f_1,0,2,200) 4.01005025126
#trapz(sqr, 0, 3, 10000) 9.00015006001
