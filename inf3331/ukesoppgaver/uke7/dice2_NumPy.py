#Arnab Kumar Datta (arnabkd) - Task 7.3
import random, numpy as np, time as tm

def simulate_probability(n):
	sum = 0
	for x in range(n):
		sum += 1 if(6 == random.randint(1,6) or 6 == random.randint(1,6)) else 0
	return sum/(n+0.0)

def numpy_simulate_probability(n):
	sum = 0
	v = np.random.randint(1,7,n)
	w = np.random.randint(1,7,n)
	for x in range(n):
		sum += 1 if (6 == v[x] or 6 == w[x]) else 0
	return sum/(n+0.0)

num = 100000
t = tm.time()
print "python random simulator probability : ",simulate_probability(num)
print "python random simulator ran in %0.10f s" %(tm.time() - t)

t = tm.time()
print "numpy based random probability : " ,numpy_simulate_probability(num)
print "numpy based simulator ran in %0.10f s" %(tm.time() - t)


#Runtime example
#arnabkd@stcroix ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke7 $ python dice2_NumPy.py
#python random simulator probability :	0.30339
#python random simulator ran in 0.3284871578 s
#numpy based random probability :  0.30565
#numpy based simulator ran in 0.0545580387 s
