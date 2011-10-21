filename = "sample.txt"
f = open(filename, 'r')

for line in f:	
	x = line.strip('\n').strip('\r').strip().split(',')
	sum = 0.0
	for i in range (1, len(x)):
		sum += float(x[i])
	print "\"%s\" , %0.5f"%(x[0],sum)

f.close()
