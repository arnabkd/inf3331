#Arnab Kumar Datta (arnabkd)
#Task 5.3 : Estimate the chance of an event in a dice game

import random,sys



#Modified simulator that returns how many throws of the dice is required to get p/n = 0.306
def smart_simulate():
    sum_desirable_res = 0;probabilty = 0;x = 0
    while (not in_range(probabilty)):
        x += 1
	res = [throw_dice() , throw_dice()]        
	if(6 in res):
	    sum_desirable_res += 1
        probabilty = (float(sum_desirable_res) / x)
    #print "For  %d simulations, we got %d favorable results (at least 1 six when throwing 2 dice)" %(x, sum_desirable_res)
    #print "The resulting fraction is %d / %d = %f" %(sum_desirable_res, x , probabilty)
    #print "Required %d simulations to get p/n = 0.306" %(x)
    return x

    
def in_range (n):
    return (n > 0.306) and (n < 0.307)


#Simulates throwing dice-throwing n times and prints out the results
def simulate(n):
    sum_desirable_res = 0
    for x in range(n):
		res = [throw_dice() , throw_dice()]
		print "Simulation #%d: " %(x) , res , "- desirable"
		if(6 in res):
			sum_desirable_res += 1		
    print "For  %d simulations, we got %d favorable results (at least 1 six when throwing 2 dice)" %(n, sum_desirable_res)
    print "The resulting fraction is %d / %d = %f" %(sum_desirable_res, n , (float(sum_desirable_res) / n))
    

#Throw_dice Simulates throwing of one dice
#param a,b
#returns a random number x such that : 1 <= x <= 6
def throw_dice():
    return random.randint(1,6)


try:
    n = int(sys.argv[1])
    simulate(n)
except:
	print "No arguments given, simulating dice throws until p/n equals 0.306. This process will be repeated 10 times."
	sum = 0
	for i in range (10):
		x = smart_simulate()
		print "Number of dice throws required in run #%d is %d" %(i,x)
		sum += x
		average = float(sum) /10
	print "After 10 iterations : average number of dice-throws required to reach p/n = 0.306  is %f" %(average)  
    
