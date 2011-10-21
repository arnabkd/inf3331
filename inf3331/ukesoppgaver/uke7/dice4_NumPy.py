#Arnab Kumar Datta  (arnabkd) - Task 7.4
import numpy as np, timeit, random

num = 10000

def numpy_hazard(n):
	return np.random.randint(1,7,(num,4))

def balance_numpy(a):
	balance = 1
	for x in a:
		balance += 10 if sum(x) < 9 else -1
	return balance

def plain_hazard(n):
	balance = 0
	for x in range(n):
		balance += 9 if (random.randint(1,6) + random.randint(1,6) + random.randint(1,6) + random.randint(1,6)) < 9 else -1
	return balance

#Runtime code part 1 (Numpy)
x = numpy_hazard(num)
el = timeit.Timer(stmt="numpy_hazard(num)", setup = "from __main__ import numpy_hazard , num")
elapsed_numpy = el.timeit(1)

print "Numpy hazard game simulation gives you %d in balance after %d dice-throws.\nCalculation time : %0.10f" %(balance_numpy(numpy_hazard(num)), num, elapsed_numpy)


#Runtime code part 2 (Plain python)
x = plain_hazard(num)
el = timeit.Timer(stmt="plain_hazard(num)", setup = "from __main__ import plain_hazard , num")
elapsed_plain = el.timeit(1)

print "Plain hazard game simulation gives you %d in balance after %d dice-throws.\nCalculation time : %0.10f" %(plain_hazard(num), num, elapsed_plain)

#arnabkd@stcroix ~/Desktop/uni/inf3331/inf3331/ukesoppgaver/uke7 $ python dice4_NumPy.py 
#Numpy hazard game simulation gives you -4345 in balance after 10000 dice-throws.
#Calculation time : 0.0006830692
#Plain hazard game simulation gives you -4610 in balance after 10000 dice-throws.
#Calculation time : 0.0701119900
