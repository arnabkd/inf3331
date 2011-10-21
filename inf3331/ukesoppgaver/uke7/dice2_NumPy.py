#Arnab Kumar Datta (arnabkd)
import random, numpy as np, time as tm

def simulate_probability(n):	
	sum = 0
	for x in range(n):
		sum += 1 if(6 == random.randint(1,7) or 6 == random.randint(1,7)) else 0
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
print "python random simulator : ",simulate_probability(num)
print "python random simulator ran in %0.9f ms" %(tm.time() - t)

t = tm.time()
print "numpy based random : " ,numpy_simulate_probability(num)
print "numpy based simulator ran in %0.9f ms" %(tm.time() - t)
