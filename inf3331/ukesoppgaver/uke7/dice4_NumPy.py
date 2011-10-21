#Arnab Kumar Datta  (arnabkd)

import numpy as np, timeit

num = 10000

def numpy_hazard(n):
	v = np.random.randint(1,7,(num,4))
	return v

def balance_numpy(a):
	balance = 1
	for x in a:
		balance += 10 if sum(x) < 9 else -1
	return balance


x = numpy_hazard(num)
el = timeit.Timer(stmt="numpy_hazard(num)", setup = "from __main__ import numpy_hazard , num")
elapsed_numpy = el.timeit(1)

print "Numpy hazard game simulation gives you (%d) in balance after %d dice-throws.\nCalculation time : %0.10f" %(balance_numpy(numpy_hazard(num)), num, elapsed_numpy)

